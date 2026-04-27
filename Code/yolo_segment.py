import sys
sys.path.insert(1, '/home/humber/.local/lib/python3.10/site-packages')

import setproctitle
setproctitle.setproctitle("yolov8n-seg")

from ultralytics import YOLO
import cv2
import time

# --- THE MISSING DICTIONARY ---
# TensorRT stripped the names, so we manually provide them here!
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

model = YOLO('yolov8n-seg.engine', task='segment') 
cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

print("[INFO] MENG3540: TensorRT GPU Pipeline Active.")
print("[INFO] Press 'q' to quit.")

while cap.isOpened():
    start_time = time.time() 
    
    success, frame = cap.read()
    if not success:
        break

    results = model(frame, verbose=False)
    annotated_frame = results[0].plot(boxes=False, labels=False)
    
    for r in results:
        if r.boxes is None:
            continue
            
        for box in r.boxes:
            x1, y1 = int(box.xyxy[0][0]), int(box.xyxy[0][1])
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            
            # --- THE FIX ---
            # Ask our dictionary for the name. If it gets confused, it falls back to "Unknown"
            class_name = COCO_CLASSES.get(cls_id, "Unknown")
            
            label_text = f"{class_name} {conf:.2f}"
            
            cv2.rectangle(annotated_frame, (x1, y1 - 25), (x1 + len(label_text) * 12, y1), (0, 0, 0), -1)
            cv2.putText(annotated_frame, label_text, (x1, y1 - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 2)

    fps = 1.0 / (time.time() - start_time)
    cv2.putText(annotated_frame, f"FPS: {fps:.1f}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 3)

    cv2.imshow("MENG3540 | GPU Acceleration", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
