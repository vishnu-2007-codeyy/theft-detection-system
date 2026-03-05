"""
Main script for real-time human activity detection using webcam.
"""

import cv2
import mediapipe as mp
import numpy as np
from activity_classifier import ActivityClassifier
from telegram_notifier import TelegramNotifier
import time

class ActivityDetector:
    def __init__(self, telegram_token=None, chat_id=None):
        """Initialize the activity detector."""
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(
            static_image_mode=False,
            model_complexity=1,
            smooth_landmarks=True,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.mp_drawing = mp.solutions.drawing_utils
        self.classifier = ActivityClassifier()
        self.notifier = TelegramNotifier(telegram_token, chat_id)
        self.current_activity = "unknown"
        self.last_notification_time = 0
        self.notification_cooldown = 5
        
    def process_frame(self, frame):
        """Process a single frame."""
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        rgb_frame.flags.writeable = False
        results = self.pose.process(rgb_frame)
        rgb_frame.flags.writeable = True
        frame = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2BGR)
        
        if results.pose_landmarks:
            self.mp_drawing.draw_landmarks(
                frame, results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS,
                self.mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2),
                self.mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2)
            )
            
            landmarks = np.array([[lm.x, lm.y, lm.z, lm.visibility] 
                                 for lm in results.pose_landmarks.landmark])
            new_activity = self.classifier.classify(landmarks)
            
            if new_activity != self.current_activity:
                self.current_activity = new_activity
                current_time = time.time()
                if current_time - self.last_notification_time > self.notification_cooldown:
                    self.notifier.send_notification(
                        f"Activity changed to: {self.current_activity}", 
                        frame.copy()
                    )
                    self.last_notification_time = current_time
            
            # Display activity
            cv2.rectangle(frame, (10, 10), (300, 80), (0, 0, 0), -1)
            cv2.putText(frame, f"Activity: {self.current_activity}", (20, 50),
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
        
        return frame
    
    def run(self):
        """Main loop for real-time detection."""
        cap = cv2.VideoCapture(0)
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        print("Starting activity detection... Press 'q' to quit")
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            processed_frame = self.process_frame(frame)
            cv2.imshow('Activity Detection', processed_frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()
        self.pose.close()

def main():
    """Main function to run the activity detector."""
    TELEGRAM_TOKEN = "8736399122:AAFg2X2kMO5CSSQDFMhLdNoH0ry98vWZXr4"
    CHAT_ID = "7137955785"
    
    detector = ActivityDetector(TELEGRAM_TOKEN, CHAT_ID)
    detector.run()

if __name__ == "__main__":
    main()