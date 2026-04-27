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

Based on research into real-time embedded applications, we selected the following technical stack to satisfy the solution criteria:

| Component | Selection | Rationale |
| :--- | :--- | :--- |
| **Hardware** | **NVIDIA Jetson Orin Nano** | Provides 40 TOPS of AI performance on a low-power, embedded footprint suitable for mobile robotics. |
| **Model** | **YOLOv8 (Single-Pass)** | Industry-standard for balancing speed and accuracy; supports both detection and segmentation. |
| **Framework** | **NVIDIA TensorRT** | Optimizes model layers specifically for the Ampere GPU architecture to maximize FPS through FP16 precision. |
| **Library** | **PyTorch** | A robust, flexible library for model integration, preprocessing, and handling live camera streams. |

---

## 3. Selection Rationale

Our design choices were driven by the requirement for a **repeatable and high-performance workflow**. 

* **Why Jetson Orin Nano?** Unlike standard microcontrollers, the Jetson platform contains a dedicated GPU that allows us to demonstrate true GPU resource utilization in AI workloads.
* **Why YOLOv8?** It is optimized for real-time applications, allowing our prototype to annotate live camera feeds with bounding boxes and class labels with minimal delay.
* **Why TensorRT?** Standard models are often too heavy for edge devices. TensorRT allows us to "compress" the model for the hardware, ensuring the system can handle advanced tasks like Instance Segmentation in real-time.

---

## 4. Project Structure

* **[Workflow](./Workflow):** Detailed system block diagrams, environment setup steps, and performance analysis.
* **[Reflection_LearningPlan](./Reflection_LearningPlan):** Individual project reflections and strategic plans for scaling this solution in industry.
* **[Code](./Code):** Source files for object detection and hardware acceleration scripts.

---
*Deliverable for Step 1 - MENG3540 Parallel Programming*
