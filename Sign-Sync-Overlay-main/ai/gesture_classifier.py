TIP_IDS = [4, 8, 12, 16, 20]
PIP_IDS = [3, 6, 10, 14, 18]

def detect_gesture(hand_landmarks):

    if hand_landmarks is None:
        return None

    landmarks = hand_landmarks.landmark

    fingers = []

    # Thumb
    if landmarks[TIP_IDS[0]].x > landmarks[PIP_IDS[0]].x:
        fingers.append(1)
    else:
        fingers.append(0)

    # Other fingers
    for i in range(1, 5):
        if landmarks[TIP_IDS[i]].y < landmarks[PIP_IDS[i]].y:
            fingers.append(1)
        else:
            fingers.append(0)

    total = sum(fingers)

    if total == 5:
        return "hello"

    elif total == 0:
        return "yes"

    elif total == 1:
        return "you"

    elif total == 2:
        return "peace"

    elif total == 3:
        return "good"

    return None
