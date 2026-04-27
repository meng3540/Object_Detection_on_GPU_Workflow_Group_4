import sys
# 1. The Sudo Bridge
sys.path.insert(1, '/home/humber/.local/lib/python3.10/site-packages')

import setproctitle
# 2. Force the name change for your professor's jtop screenshot!
setproctitle.setproctitle("yolov8n")

from ultralytics import YOLO
import cv2
import time
import random

# The hardcoded dictionary because TensorRT strips the names
COCO_CLASSES = {
    0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane', 5: 'bus', 
    6: 'train', 7: 'truck', 8: 'boat', 9: 'traffic light', 10: 'fire hydrant', 
    11: 'stop sign', 12: 'parking meter', 13: 'bench', 14: 'bird', 15: 'cat', 
    16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow', 20: 'elephant', 21: 'bear', 
    22: 'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella', 26: 'handbag', 
    27: 'tie', 28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard', 
    32: 'sports ball', 33: 'kite', 34: 'baseball bat', 35: 'baseball glove', 
    36: 'skateboard', 37: 'surfboard', 38: 'tennis racket', 39: 'bottle', 
    40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon', 45: 'bowl', 
    46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange', 50: 'broccoli', 
    51: 'carrot', 52: 'hot dog', 53: 'pizza', 54: 'donut', 55: 'cake', 56: 'chair', 
    57: 'couch', 58: 'potted plant', 59: 'bed', 60: 'dining table', 61: 'toilet', 
    62: 'tv', 63: 'laptop', 64: 'mouse', 65: 'remote', 66: 'keyboard', 67: 'cell phone', 
    68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink', 72: 'refrigerator', 
    73: 'book', 74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear', 
    78: 'hair drier', 79: 'toothbrush'
}

# Generate 80 dynamic, bright colors for our bounding boxes
random.seed(42)
class_colors = {i: (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255)) for i in range(80)}

# Load the GPU-Accelerated Detection Engine
model = YOLO('yolov8n.engine', task='detect') 
cap = cv2.VideoCapture(0)

# Force MJPG to prevent camera bottlenecking
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

print("[INFO] MENG3540 Phase 1: TensorRT GPU Pipeline Active.")
print("[INFO] Press 'q' to quit.")

while cap.isOpened():
    start_time = time.time() # Start FPS stopwatch
    
    success, frame = cap.read()
    if not success:
        break

    # Run AI and hide the default ugly labels
    results = model(frame, verbose=False)
    annotated_frame = frame.copy()
    
    for r in results:
        if r.boxes is None:
            continue
            
        for box in r.boxes:
            x1, y1, x2, y2 = box.xyxy[0]
            x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
            
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            
            # Look up the English name and Color
            class_name = COCO_CLASSES.get(cls_id, "Unknown")
            color = class_colors.get(cls_id, (0, 255, 0)) # Default to green if missing
            
            label_text = f"{class_name} {conf:.2f}"
            
            # Draw the colored bounding box
            cv2.rectangle(annotated_frame, (x1, y1), (x2, y2), color, 2)
            
            # Draw the custom tags
            cv2.rectangle(annotated_frame, (x1, y1 - 25), (x1 + len(label_text) * 12, y1), color, -1)
            cv2.putText(annotated_frame, label_text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

    # Calculate and draw FPS
    fps = 1.0 / (time.time() - start_time)
    cv2.putText(annotated_frame, f"FPS: {fps:.1f}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    cv2.imshow("MENG3540 | Object Detection GPU", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
