from ultralytics import YOLO
import cv2
import time

model = YOLO('yolov8n.pt') 

cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

print("[INFO] MENG3540: FORCED CPU Baseline Active. Prepare for lag.")
print("[INFO] Press 'q' to quit.")

while cap.isOpened():
    start_time = time.time() 
    
    success, frame = cap.read()
    if not success:
        break

    # --- THE FIX: FORCE CPU ---
    # This explicitly blocks PyTorch from using your Tegra GPU
    results = model(frame, device='cpu', verbose=False)
    
    annotated_frame = results[0].plot()

    # Calculate and draw FPS in RED
    fps = 1.0 / (time.time() - start_time)
    cv2.putText(annotated_frame, f"CPU FPS: {fps:.1f}", (10, 40), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 3)

    cv2.imshow("MENG3540 | CPU Baseline (Bottleneck)", annotated_frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
