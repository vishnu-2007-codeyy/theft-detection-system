"""
Theft Detection System - COMPLETE FIXED VERSION
"""

import cv2
import numpy as np
import time
from datetime import datetime
import os

class TheftDetector:
    def __init__(self, notifier):
        """Initialize theft detector"""
        self.notifier = notifier
        
        # Initialize face detector
        self.face_cascade = cv2.CascadeClassifier(
            cv2.data.haarcascades + 'haarcascade_frontalface_default.xml'
        )
        
        # Motion detection
        self.back_subtractor = cv2.createBackgroundSubtractorMOG2()
        self.min_area = 5000
        
        # Alert variables
        self.last_alert_time = 0
        self.alert_cooldown = 15  # Seconds between alerts
        
        # Create intruder folder
        self.intruder_dir = "intruders"
        if not os.path.exists(self.intruder_dir):
            os.makedirs(self.intruder_dir)
        
        print("🔒 Theft Detection System Initialized")
        print(f"⏱️ Alert Cooldown: {self.alert_cooldown} seconds")
    
    def detect_faces(self, frame):
        """Detect faces in frame - FIXED VERSION"""
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Improved face detection parameters
        faces = self.face_cascade.detectMultiScale(
            gray, 
            scaleFactor=1.1,
            minNeighbors=5,
            minSize=(80, 80)  # Minimum face size
        )
        
        # Draw RED boxes for faces
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 3)
            cv2.putText(frame, "INTRUDER!", (x, y-10),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 255), 2)
            
        # Show face count on screen
        if len(faces) > 0:
            cv2.putText(frame, f"Faces: {len(faces)}", (10, 60),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
        
        return faces, frame
    
    def detect_motion(self, frame):
        """Detect motion in frame - GREEN boxes"""
        fg_mask = self.back_subtractor.apply(frame)
        thresh = cv2.threshold(fg_mask, 25, 255, cv2.THRESH_BINARY)[1]
        thresh = cv2.dilate(thresh, None, iterations=2)
        
        contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
        motion_detected = False
        for contour in contours:
            if cv2.contourArea(contour) > self.min_area:
                motion_detected = True
                (x, y, w, h) = cv2.boundingRect(contour)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        
        return motion_detected, frame
    
    def send_alert(self, frame, faces):
        """Send Telegram alert with photo - FIXED"""
        current_time = time.time()
        
        # Show cooldown on screen
        time_left = max(0, self.alert_cooldown - (current_time - self.last_alert_time))
        cv2.putText(frame, f"Next alert: {int(time_left)}s", (10, 90),
                   cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 0), 2)
        
        # Check if face detected AND cooldown passed
        if len(faces) > 0 and (current_time - self.last_alert_time) > self.alert_cooldown:
            print("🚨 INTRUDER DETECTED! Sending alert...")
            
            # Add timestamp to frame
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            cv2.putText(frame, timestamp, (10, 30),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 255), 2)
            
            # Send to Telegram
            message = f"🚨 INTRUDER DETECTED!\n📍 Time: {timestamp}"
            success = self.notifier.send_notification(message, frame)
            
            if success:
                # Save photo locally
                filename = f"intruders/intruder_{int(time.time())}.jpg"
                cv2.imwrite(filename, frame)
                print(f"✅ Alert sent! Photo saved: {filename}")
                self.last_alert_time = current_time
            else:
                print("❌ Failed to send Telegram alert")
            
            return True
        
        return False
    
    def run(self):
        """Main detection loop"""
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("❌ Camera not found!")
            return
        
        print("\n" + "="*50)
        print("🚨 THEFT DETECTION SYSTEM RUNNING")
        print("="*50)
        print("🟢 GREEN box = Motion")
        print("🔴 RED box = Face (INTRUDER)")
        print("📸 Photo sent to Telegram when RED box appears")
        print("⏱️ Alert cooldown: 15 seconds")
        print("="*50)
        print("Press 'q' to quit")
        print("Press 't' for test alert")
        print("="*50)
        
        frame_count = 0
        
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
            
            frame_count += 1
            display_frame = frame.copy()
            
            # Detect motion (GREEN boxes)
            motion_detected, display_frame = self.detect_motion(frame)
            
            # Detect faces (RED boxes) - every 3rd frame for speed
            if frame_count % 3 == 0:
                faces, display_frame = self.detect_faces(display_frame)
                self.send_alert(display_frame, faces)
            
            # Show frame count
            cv2.putText(display_frame, f"Frame: {frame_count}", (10, 120),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            
            # Show instructions
            cv2.putText(display_frame, "Q:Quit T:Test", (10, 140),
                       cv2.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 1)
            
            cv2.imshow('Theft Detection System', display_frame)
            
            key = cv2.waitKey(1) & 0xFF
            if key == ord('q'):
                break
            elif key == ord('t'):
                print("🧪 Sending test alert...")
                dummy_faces = [(100, 100, 200, 200)]
                self.send_alert(frame, dummy_faces)
        
        cap.release()
        cv2.destroyAllWindows()
        print("\n🔒 Theft Detection Stopped")