# Phase 3: Reflection & Individual Learning Plan

This section provides a critical reflection on the engineering project experience and outlines a strategic plan for future skill acquisition in the field of Mechatronics and Parallel Computing.

---

## 1. Individual Reflection

### New Concepts and Skills Acquired
[cite_start]During this project, I moved beyond high-level programming into **Systems-Level Engineering**[cite: 51]. Key skills learned include:
* [cite_start]**Hardware Acceleration:** Compiling models specifically for NVIDIA’s Ampere architecture using **TensorRT**[cite: 51].
* [cite_start]**Environment Virtualization:** Setting up and managing **WSL 2** and **Ubuntu 22.04** for cross-platform development[cite: 51].
* [cite_start]**Linux Kernel Interaction:** Managing root-level permissions and library path injections to solve "Dependency Hell" conflicts[cite: 51].

### Application of Existing Skills
[cite_start]I effectively applied my prior knowledge of **Electric Circuit Analysis** and **Instrumentation** to manage the hardware peripherals and ensure stable power delivery to the Jetson Orin Nano while under high computational load[cite: 15, 52].

### Challenges and Individual Contributions
[cite_start]The most significant challenge was a critical conflict between the user-space AI libraries and the system’s AI drivers (the `libcudss.so.0` crash)[cite: 55]. [cite_start]I took the lead in developing the **"Sudo Bridge"** solution, manually injecting local library paths into the root environment to allow the system to access necessary packages without compromising security or performance[cite: 55].

---

## 2. Individual Learning Plan

### Knowledge Gaps Identified
[cite_start]While we achieved high performance with object detection, I recognized a gap in my knowledge regarding **Model Pruning** and **Quantization Aware Training (QAT)**[cite: 58]. [cite_start]Understanding these would allow for even more efficient deployment on lower-power microcontrollers[cite: 58].

### Scaling for Industry
[cite_start]If this solution were to be implemented at a larger scale—for example, in my upcoming co-op at **Cenovus Energy**—additional expertise in **Containerization (Docker/Kubernetes)** would be essential to manage AI model updates across hundreds of edge devices simultaneously[cite: 59, 60]. 

### Training and Resources
To bridge these gaps, I plan to access the following resources:
* [cite_start]**NVIDIA Deep Learning Institute (DLI):** Certifications in "Optimizing CUDA Kernels"[cite: 61].
* [cite_start]**Industry Manuals:** Deepening my understanding of **GIS Data Analysis** for drone-based sensor fusion[cite: 61].

---

## 3. Final Project Successes
[cite_start]The project went particularly well in terms of raw performance gains[cite: 54]. [cite_start]By moving from a novice CPU setup to a professional GPU workflow, we achieved a **10x increase in FPS**[cite: 54]. [cite_start]Our strategy of "measure twice, code once"—specifically using **jtop** for constant telemetry—ensured we never moved forward without data-backed results[cite: 54].

---
**Presented by:** Gurshan Singh  
**Course:** MENG3540: Parallel Programming  
**Date:** April 2026
