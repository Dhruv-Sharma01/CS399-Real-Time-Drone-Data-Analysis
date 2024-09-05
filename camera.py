from ultralytics import YOLO
import cv2
import math
import time  # Import time for the timer

# Start webcam
cap = cv2.VideoCapture(0)
cap.set(3, 640)  # Set frame width
cap.set(4, 480)  # Set frame height

# Video Writer to save the recording
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Codec for the video format
fps = 20  # Frames per second for video
out = cv2.VideoWriter('recording.avi', fourcc, fps, (640, 480))  # Output file, FPS, frame size

# Model
model = YOLO("yolo-Weights/yolov8n.pt")

# Object classes
classNames = ["person", "bicycle", "car", "motorbike", "aeroplane", "bus", "train", "truck", "boat",
              "traffic light", "fire hydrant", "stop sign", "parking meter", "bench", "bird", "cat",
              "dog", "horse", "sheep", "cow", "elephant", "bear", "zebra", "giraffe", "backpack", "umbrella",
              "handbag", "tie", "suitcase", "frisbee", "skis", "snowboard", "sports ball", "kite", "baseball bat",
              "baseball glove", "skateboard", "surfboard", "tennis racket", "bottle", "wine glass", "cup",
              "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich", "orange", "broccoli",
              "carrot", "hot dog", "pizza", "donut", "cake", "chair", "sofa", "pottedplant", "bed",
              "diningtable", "toilet", "tvmonitor", "laptop", "mouse", "remote", "keyboard", "cell phone",
              "microwave", "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors",
              "teddy bear", "hair drier", "toothbrush"
              ]

# Start the timer
start_time = time.time()

while True:
    success, img = cap.read()

    # Check if 10 seconds have passed
    elapsed_time = time.time() - start_time
    if elapsed_time > 60:
        print("Recording complete.")
        break

    # Run YOLO model for object detection
    results = model(img, stream=True)

    # Coordinates and predictions
    for r in results:
        boxes = r.boxes

        for box in boxes:
            # Bounding box
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)  # Convert to int values

            # Draw bounding box on the image
            cv2.rectangle(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

            # Confidence
            confidence = math.ceil((box.conf[0] * 100)) / 100
            print("Confidence --->", confidence)

            # Class name
            cls = int(box.cls[0])
            print("Class name -->", classNames[cls])

            # Display object details on the image
            org = [x1, y1]
            font = cv2.FONT_HERSHEY_SIMPLEX
            fontScale = 1
            color = (255, 0, 0)
            thickness = 2
            cv2.putText(img, classNames[cls], org, font, fontScale, color, thickness)

    # Save the current frame to the video
    out.write(img)

    # Show the webcam output
    cv2.imshow('Webcam', img)

    # Add a small delay to control the frame rate and ensure it matches the video FPS
    if cv2.waitKey(int(500 / fps)) == ord('q'):
        break

# Release the camera, video writer, and close windows
cap.release()
out.release()  # Save and close the video file
cv2.destroyAllWindows()
