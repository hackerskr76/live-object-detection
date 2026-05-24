import cv2
from ultralytics import YOLO

model = YOLO('models/best.pt')
cap = cv2.VideoCapture(0)

print("Starting Real-Time Detection... Press 'q' to exit.")

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
    
    results = model(frame, conf=0.5)
    
    annotated_frame = results[0].plot()
    cv2.imshow("YOLOv8 Real-Time", annotated_frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()