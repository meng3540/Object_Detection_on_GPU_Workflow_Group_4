# Phase 3: Reflection & Individual Learning Plan

This section provides a critical analysis of the project experience and outlines a roadmap for future technical growth in Mechatronics and AI.

---

## A) Individual Reflection

### 1. New Concepts, Skills, and Tools
Throughout this project, I moved beyond high-level software development into **Hardware-Level Optimization**. Key skills learned include:
* **TensorRT Acceleration:** Mastering model compilation specifically for NVIDIA's Ampere architecture.
* **Linux Environment Management:** Configuring **WSL 2** and **Ubuntu 22.04** to handle complex parallel programming dependencies.
* **Real-Time Telemetry:** Using tools like **jtop** to monitor GPU resource utilization and power consumption.

### 2. Improved Existing Skills
I effectively applied and improved my existing knowledge of **Instrumentation and Measurement** and **Electronic Circuit Analysis** to ensure hardware stability during high-load AI processing. These skills will be directly applicable to my future career as a Mechatronics Engineer, specifically in my upcoming **12-month co-op with Cenovus Energy**.

### 3. Project Successes and Strategies
The most successful aspect of the project was the **10x performance gain** achieved by moving from CPU to GPU inferencing. The strategy that helped achieve this was a "data-first" approach—constantly measuring performance metrics at every stage of the code pipeline.

### 4. Challenges and Individual Contributions
The primary challenge was a critical library conflict between the user-space and root-space environments. I contributed to solving this by implementing a **"Sudo Bridge"** that injected specific user-library paths into the root environment, allowing the hardware-accelerated code to run seamlessly.

---

## B) Individual Learning Plan

### 1. Identified Knowledge Gaps
As we worked through the project, it became evident that I have a knowledge gap in **Model Quantization and Pruning**. While we optimized for FP16, learning INT8 quantization would allow for even more efficient deployment on lower-power microcontrollers.

### 2. Scaling for Industry
To scale this solution for a larger project or a professional industrial setting—such as autonomous safety monitoring in the energy sector—expertise in **Containerization (Docker)** and **Edge Orchestration** would be necessary to manage AI model deployment across multiple devices simultaneously.

### 3. Training and Resources
To equip myself with these additional skills, I plan to access the following resources:
* **NVIDIA Deep Learning Institute (DLI):** Specifically for "Optimization of AI Models on Jetson".
* **Industrial Documentation:** Further study into **ROS 2 (Robot Operating System)** for advanced multi-sensor fusion.

---
**Presented by:** Gurshan Singh  
**Course:** MENG3540: Parallel Programming  
**Institution:** Humber Polytechnic
