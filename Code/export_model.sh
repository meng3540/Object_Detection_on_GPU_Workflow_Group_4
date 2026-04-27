#!/bin/bash
# export_model.sh
# MENG3540: Parallel Programming - TensorRT Export Script

echo "Starting YOLOv8 TensorRT Export..."

# Ensure ultralytics is installed
pip install ultralytics

# Export standard detection model to FP16 TensorRT engine
yolo export model=yolov8n.pt format=engine half=True device=0 workspace=4

# Export advanced segmentation model to FP16 TensorRT engine
yolo export model=yolov8n-seg.pt format=engine half=True device=0 workspace=4

echo "Export complete. .engine files generated for deployment."
