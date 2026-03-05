import cv2
cap = cv2.VideoCapture(0)
ret, frame = cap.read()
if ret:
    print("✅ Camera working!")
    cv2.imshow('Test', frame)
    cv2.waitKey(2000)
    cv2.destroyAllWindows()
else:
    print("❌ Camera not working")
cap.release()