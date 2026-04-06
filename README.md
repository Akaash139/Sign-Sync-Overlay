# ✋ SignSync – Real-Time Sign Language to Text Converter

**Bridging communication gaps using AI-powered gesture recognition**

---

## 🚀 Overview

SignSync is a real-time AI-based system that converts sign language gestures into text using computer vision and machine learning techniques. The project aims to assist individuals with hearing or speech impairments by enabling seamless communication through visual input.

Additionally, an experimental Google Meet extension was explored to integrate real-time sign-to-text translation in video calls, aiming to enhance accessibility in online meetings.

---

## 🎯 Features

* ✋ Real-time hand gesture detection
* 🧠 AI-based gesture classification
* 💬 Instant text output from sign language
* 🎥 Uses webcam for live input
* 🌐 Attempted integration with Google Meet (extension prototype)

---

## 🧠 Tech Stack

* **Python**
* **OpenCV** – video processing
* **MediaPipe** – hand tracking and landmark detection
* **Machine Learning Model** – gesture classification
* **WebSockets** – real-time communication between backend and frontend

---

## 🧱 Project Structure

```text
SignSync/
│
├── ai/
│   ├── gesture_classifier.py     # ML model for gesture recognition
│   ├── mediapipe_detector.py     # Hand tracking using MediaPipe
│
├── backend/
│   └── websocket_server.py       # Real-time communication server
│
├── frontend/                    # UI for displaying output
│
├── main.py                      # Entry point
├── requirements.txt             # Dependencies
└── README.md
```

---

## ⚙️ How It Works

1. Webcam captures live video input
2. MediaPipe detects hand landmarks
3. Extracted features are passed to a trained ML model
4. Model predicts the gesture
5. Output is converted into text and displayed in real-time

---

## 🧪 Experimental Feature (Google Meet Extension)

An extension was explored to integrate SignSync with Google Meet, allowing live sign language translation during video calls.

### Status:

* Prototype stage ⚠️
* Faced limitations due to browser security policies and real-time video stream access

### Future Scope:

* Improved browser integration
* Real-time caption overlay in video conferencing platforms

---

## 📦 Installation

### 1️⃣ Clone the repository

```bash
git clone https://github.com/your-username/signsync.git
cd signsync
```

---

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

### 3️⃣ Run the application

```bash
python main.py
```

---

## 📸 Use Case

* Assist deaf and mute individuals in communication
* Real-time translation in conversations
* Accessibility tool for online meetings

---

## 🔮 Future Improvements

* Full sign language sentence recognition
* Improved model accuracy
* Mobile app version
* Complete browser extension integration
* Multi-language support

---

## 🎤 Project Insight

> This project demonstrates how AI and computer vision can be applied to solve real-world accessibility challenges by enabling real-time interpretation of sign language.

---

## 🙌 Acknowledgements

* MediaPipe by Google
* OpenCV community
* Machine Learning resources

---

## 📄 License

This project is for educational purposes.

---
