import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Dictionary to hold gesture names
gesture_names = {
    "thumbs_up": "Thumbs Up",
    "thumbs_down": "Thumbs Down",
    "peace_sign": "Peace Sign",
    "fist": "Fist",
    "ok": "OK"
}

class GestureDetector:
    def __init__(self):
        self.hands = mp_hands.Hands(static_image_mode=False,
                                     max_num_hands=2,
                                     min_detection_confidence=0.7)

    def detect_gesture(self, landmarks):
        thumb_tip = landmarks[mp_hands.HandLandmark.THUMB_TIP]
        index_tip = landmarks[mp_hands.HandLandmark.INDEX_FINGER_TIP]
        middle_tip = landmarks[mp_hands.HandLandmark.MIDDLE_FINGER_TIP]
        ring_tip = landmarks[mp_hands.HandLandmark.RING_FINGER_TIP]
        pinky_tip = landmarks[mp_hands.HandLandmark.PINKY_TIP]

        if thumb_tip.y < index_tip.y and index_tip.y < middle_tip.y:
            return "thumbs_up"
        if thumb_tip.y > index_tip.y and index_tip.y > middle_tip.y:
            return "thumbs_down"
        if index_tip.y < middle_tip.y and ring_tip.y > middle_tip.y and pinky_tip.y > ring_tip.y:
            return "peace_sign"
        if (thumb_tip.y > index_tip.y and
            thumb_tip.y > middle_tip.y and
            thumb_tip.y > ring_tip.y and
            thumb_tip.y > pinky_tip.y):
            return "fist"
        if (thumb_tip.x > index_tip.x and
            index_tip.y < middle_tip.y and
            middle_tip.x > ring_tip.x and
            ring_tip.y < pinky_tip.y):
            return "ok"

        return None

    def process_frame(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        return results
