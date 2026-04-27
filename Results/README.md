# Prototype Validation & Performance Results

This section provides visual and data-backed evidence of the project's success in implementing hardware-accelerated AI inferencing.

---

## 1. Hardware Telemetry (jtop Analysis)
To verify that our workflow successfully utilizes the **NVIDIA Jetson Orin Nano** GPU cores, we used the `jtop` telemetry suite.



**Observations:**
* **GPU Utilization:** Stabilized at ~75.8% during active inference, confirming successful parallel offloading.
* **Thermal Management:** The system maintained an average temperature of 42°C, well within the safe operational limits for mechatronics applications.
* **Power Efficiency:** The Jetson Orin Nano consumed approximately 10-15W while delivering real-time results, proving its suitability for mobile edge deployment.

---

## 2. Real-Time Object Detection Results
The following screenshot demonstrates the primary workflow: a live camera feed annotated with bounding boxes and high-confidence class labels.



**Technical Highlights:**
* **Steady Frame Rate:** Consistently achieved **25.8 FPS** using the optimized TensorRT engine.
* **Precision:** High accuracy in a dynamic environment, even with overlapping objects.

---

## 3. Advanced Prototype: Instance Segmentation
This result validates our advanced prototype, moving beyond boxes to pixel-level polygon masks.



**Technical Highlights:**
* **Pixel-Perfect Accuracy:** The system identifies the exact contours of objects, essential for advanced robotics tasks like bin-picking.
* **Fluid Performance:** Maintained **17.3 FPS**, proving that our parallel optimization can handle complex, high-fidelity AI tasks.

---

## 4. Performance Comparison Summary
Our final analysis confirms that AI inferencing is a parallel computation problem that requires specialized accelerators.

| Implementation | Frame Rate (FPS) | CPU Load | GPU Status |
| :--- | :--- | :--- | :--- |
| **Novice (CPU Only)** | 2.4 FPS | > 90% (Saturated) | 0% (Idle) |
| **Professional (GPU Optimized)** | **25.8 FPS** | < 15% (Idle) | **75.8% (Active)** |

**Conclusion:** By transitioning to a hardware-accelerated pipeline, we achieved a **10x increase in performance**, meeting all project criteria for real-time embedded applications.

---
*Results Documentation - MENG3540 Parallel Programming*
