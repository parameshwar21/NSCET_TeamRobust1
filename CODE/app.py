import cv2
import mediapipe as mp
from model import GestureDetector, gesture_names

# Initialize Mediapipe hands and drawing module
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

def main():
    detector = GestureDetector()
    cap = cv2.VideoCapture(0)  # Change to 1 if you have multiple cameras

    if not cap.isOpened():
        print("Error: Could not open camera.")
        return

    while True:
        ret, frame = cap.read()
        if not ret or frame is None:  # Check if the frame is valid
            print("Error: Failed to capture image")
            break

        results = detector.process_frame(frame)

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                gesture = detector.detect_gesture(hand_landmarks.landmark)
                if gesture:
                    print(f"Detected Gesture: {gesture_names.get(gesture, 'Unknown')}")

        cv2.imshow("Hand Gesture Detection", frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
