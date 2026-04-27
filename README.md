# Object Detection & Instance Segmentation on GPU Edge Device

**Course:** MENG3540: Parallel Programming  
**Institution:** Humber Polytechnic  
**Presenters:** Hrishikesh Patel & Gurshan Singh

---

## 1. Introduction & Problem Statement

### The Challenge
In modern mechatronics and industrial automation, real-time decision-making is critical. Traditional AI workloads often suffer from high latency when processed on standard CPUs or via cloud-based systems. This project addresses the need for **low-latency, on-premise AI inferencing** by developing a hardware-accelerated workflow on an embedded edge device.

### AI Inferencing as a Parallel Problem
AI inferencing is fundamentally a parallel computation problem involving millions of simultaneous matrix multiplications. By utilizing an **NVIDIA Jetson GPU**, we can execute these operations across hundreds of CUDA cores in parallel rather than sequentially on a CPU, achieving the frame rates required for real-time robotic or drone navigation.

---

## 2. Hardware & Software Selection

Based on research into real-time embedded applications, we selected the following stack:

| Component | Selection | Rationale |
| :--- | :--- | :--- |
| **Hardware** | **NVIDIA Jetson Orin Nano** | Provides 40 TOPS of AI performance on a low-power, embedded footprint. |
| **Model** | **YOLOv8 (Single-Pass)** | Industry-standard for balancing speed and accuracy in object detection. |
| **Framework** | **NVIDIA TensorRT** | Optimizes model layers for the Ampere GPU architecture to maximize FPS. |
| **Library** | **PyTorch** | Robust library for model integration and preprocessing. |

---

## 3. System Workflow & Data Pipeline

The following steps illustrate our complete data flow pipeline:

**Data Flow Pipeline:**
1. **Input Stage:** Live Video Stream capture via USB Camera.
2. **Preprocessing:** Image resizing and normalization on the ARM CPU.
3. **Memory Transfer:** Host-to-Device (H2D) transfer to Jetson GPU Memory.
4. **Inference:** Parallel computation using the **YOLOv8 TensorRT Engine**.
5. **Post-processing:** Non-Maximum Suppression (NMS) and Bounding Box annotation.
6. **Output Stage:** Real-time display of annotated frames with **FPS Metrics**.

---

## 4. System Integration & Commands

To overcome OS-level dependency conflicts and achieve hardware acceleration, the following integration steps were performed:

### Sudo Bridge & Native OS Injection
We bypassed library conflicts by injecting user paths into the root environment and installing the `setproctitle` library natively for telemetry:

```bash
# Bypass Python pip conflicts
sudo -E python3 -m pip install setproctitle
