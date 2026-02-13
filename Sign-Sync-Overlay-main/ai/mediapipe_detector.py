import cv2
import mediapipe as mp
import time
from gesture_classifier import detect_gesture

mp_holistic = mp.solutions.holistic
mp_drawing = mp.solutions.drawing_utils

cap = cv2.VideoCapture(0)

gesture_buffer = []
BUFFER_SIZE = 15

last_output = None
last_output_time = 0

COOLDOWN = 2  # seconds

with mp_holistic.Holistic(
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
) as holistic:

    while cap.isOpened():

        ret, frame = cap.read()

        if not ret:
            break

        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        results = holistic.process(image)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        gesture = None

        if results.right_hand_landmarks:
            gesture = detect_gesture(results.right_hand_landmarks)

        elif results.left_hand_landmarks:
            gesture = detect_gesture(results.left_hand_landmarks)

        if gesture:

            gesture_buffer.append(gesture)

            if len(gesture_buffer) > BUFFER_SIZE:
                gesture_buffer.pop(0)

            # majority vote
            most_common = max(set(gesture_buffer), key=gesture_buffer.count)

            count = gesture_buffer.count(most_common)

            current_time = time.time()

            if count > BUFFER_SIZE * 0.8:

                if most_common != last_output or current_time - last_output_time > COOLDOWN:

                    print("\nSTABLE DETECTED:", most_common)

                    last_output = most_common
                    last_output_time = current_time

                    gesture_buffer.clear()

        # draw landmarks
        if results.right_hand_landmarks:
            mp_drawing.draw_landmarks(
                image,
                results.right_hand_landmarks,
                mp_holistic.HAND_CONNECTIONS)

        if results.face_landmarks:
            mp_drawing.draw_landmarks(
                image,
                results.face_landmarks,
                mp_holistic.FACEMESH_CONTOURS)

        cv2.imshow("Sign Sync Detector", image)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

cap.release()
cv2.destroyAllWindows()
