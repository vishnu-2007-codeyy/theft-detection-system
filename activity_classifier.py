"""
Activity classifier for sitting, standing, walking detection.
"""

import numpy as np
from collections import deque

class ActivityClassifier:
    def __init__(self, history_size=10):
        """Initialize the activity classifier."""
        self.LANDMARKS = {
            'nose': 0, 'left_shoulder': 11, 'right_shoulder': 12,
            'left_elbow': 13, 'right_elbow': 14, 'left_wrist': 15,
            'right_wrist': 16, 'left_hip': 23, 'right_hip': 24,
            'left_knee': 25, 'right_knee': 26, 'left_ankle': 27,
            'right_ankle': 28, 'left_heel': 29, 'right_heel': 30,
            'left_foot_index': 31, 'right_foot_index': 32
        }
        
        self.position_history = deque(maxlen=history_size)
        self.SITTING_ANGLE_THRESHOLD = 110
        self.STANDING_ANGLE_THRESHOLD = 160
        self.WALKING_MOVEMENT_THRESHOLD = 0.02
        
    def calculate_angle(self, p1, p2, p3):
        """Calculate angle between three points."""
        v1 = np.array(p1) - np.array(p2)
        v2 = np.array(p3) - np.array(p2)
        cos_angle = np.dot(v1, v2) / (np.linalg.norm(v1) * np.linalg.norm(v2))
        cos_angle = np.clip(cos_angle, -1.0, 1.0)
        return np.degrees(np.arccos(cos_angle))
    
    def extract_key_points(self, landmarks):
        """Extract key body points from landmarks."""
        points = {}
        for name, idx in self.LANDMARKS.items():
            if idx < len(landmarks):
                points[name] = landmarks[idx][:2]
        return points
    
    def detect_sitting(self, points):
        """Detect if person is sitting."""
        try:
            left_angle = self.calculate_angle(
                points['left_hip'], points['left_knee'], points['left_ankle']
            )
            right_angle = self.calculate_angle(
                points['right_hip'], points['right_knee'], points['right_ankle']
            )
            avg_angle = (left_angle + right_angle) / 2
            return avg_angle < self.SITTING_ANGLE_THRESHOLD
        except:
            return False
    
    def detect_standing(self, points):
        """Detect if person is standing."""
        try:
            left_angle = self.calculate_angle(
                points['left_hip'], points['left_knee'], points['left_ankle']
            )
            right_angle = self.calculate_angle(
                points['right_hip'], points['right_knee'], points['right_ankle']
            )
            avg_angle = (left_angle + right_angle) / 2
            return avg_angle > self.STANDING_ANGLE_THRESHOLD
        except:
            return False
    
    def detect_walking(self, points):
        """Detect if person is walking."""
        if len(self.position_history) < 5:
            return False
        
        try:
            movements = []
            history = list(self.position_history)[-5:]
            
            for i in range(1, len(history)):
                if 'left_ankle' in history[i] and 'left_ankle' in history[i-1]:
                    move = np.linalg.norm(
                        np.array(history[i]['left_ankle']) - 
                        np.array(history[i-1]['left_ankle'])
                    )
                    movements.append(move)
            
            if movements:
                return np.mean(movements) > self.WALKING_MOVEMENT_THRESHOLD
        except:
            pass
        
        return False
    
    def classify(self, landmarks):
        """Classify the current activity."""
        points = self.extract_key_points(landmarks)
        
        current_positions = {}
        for name, coords in points.items():
            current_positions[name] = coords
        self.position_history.append(current_positions)
        
        if self.detect_walking(points):
            return "walking"
        elif self.detect_standing(points):
            return "standing"
        elif self.detect_sitting(points):
            return "sitting"
        else:
            return "unknown"