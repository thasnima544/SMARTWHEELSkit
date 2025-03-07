from ultralytics import YOLO
import cv2

# Load the trained YOLOv8 model
model = YOLO(r'C:\Users\mehaj\OneDrive\Desktop\best.pt')

# Open webcam (source=0 means default webcam)
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Starting webcam for obstacle detection...")

while True:
    ret, frame = cap.read()
    if not ret:
        print("Failed to grab frame.")
        break
    
    # Run YOLOv8 detection on the frame
    results = model(frame)
    
    # Plot the detections on the frame
    annotated_frame = results[0].plot()
    
    # Display the result
    cv2.imshow('YOLOv8 Obstacle Detection', annotated_frame)
    
    # Press 'q' to quit
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release resources
cap.release()
cv2.destroyAllWindows()