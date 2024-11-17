
# CS399 - Real-Time Drone Data Analysis

## Real-Time Drone Data Analysis and Object Detection

This repository contains the implementation of a **real-time drone data analysis** framework that processes video feeds from multiple drones, stitches their frames together, and performs object detection. The project is optimized for real-time processing through efficient local inference and keypoint matching techniques.

---

## Overview

The project demonstrates the following key features:

1. **Local Inference on Intersecting Drones:**  
   - Detect intersections between drones' fields of view based on their positions. This is performed locally on drones for efficiency.
   
2. **Keypoint Extraction:**  
   - Extract and match keypoints from overlapping video frames using advanced feature-matching algorithms.
   
3. **Image Stitching:**  
   - Seamlessly combine frames from multiple drones into a composite image at the central server.
   
4. **Object Detection:**  
   - Apply object detection algorithms to stitched images to identify and annotate objects.

---

## Pipeline

### High-Level Workflow:
1. **Drone Positions and Local Inference:**  
   - Identify drones with overlapping fields of view. This is determined by finding drones within the range of \( h \cdot \tan(\theta) \), where:  
     - \( h \): Height of the drone.  
     - \( \theta \): Angle of the camera relative to the ground.
     
2. **Keypoint Extraction:**  
   - Extract features using techniques such as **SIFT** (Scale-Invariant Feature Transform).
   
3. **Image Stitching:**  
   - Perform feature matching and alignment using **homography estimation** for seamless transitions between frames.
   
4. **Object Detection:**  
   - Apply object detection models to stitched panoramas and annotate detected objects.

![Drone Positons (2)](https://github.com/user-attachments/assets/c581be6f-705c-4483-aa71-6aca9135f5f1)#

---

## Features

- **Drone Position Simulation:**  
  Simulate drone positions and movements to visualize the network of drones and overlapping fields of view.  
  ![simulation](https://github.com/user-attachments/assets/23c6e071-2996-489e-b475-0b0899a7bd03)

- **Keypoint Matching Visualization:**  
  Debug and validate matched features across frames to ensure stitching accuracy.

- **Real-Time Image Stitching:**  
  Align and blend frames efficiently using **feature matching** and **homography estimation**.

- **Object Detection:**  
  Detect and annotate objects in stitched images using pre-trained object detection models such as **YOLO**, **SSD**, or **R-CNN**.

---

## Project Details

### 1. Local Inference on Drones  
   - Identify overlapping fields of view locally using drone positional data.  
   - Only overlapping frames are sent for stitching, reducing computational overhead.
   
### 2. Keypoint Extraction and Matching  
   - Extract visual features using **SIFT**.  
   - Perform matching with **FLANN-based matcher** for accurate alignment.

### 3. Image Stitching  
   - Use matched features to compute **homography** for aligning frames.  
   - Blend frames smoothly with **alpha blending** for high-quality panoramas.

### 4. Object Detection  
   - Annotate stitched images with bounding boxes and labels for detected objects.  
   - Models like **YOLO**, **SSD**, and **R-CNN** are supported for object detection.

---

## Installation

1. Clone the repository:  
   ```bash
   git clone https://github.com/Dhruv-Sharma01/CS399-Real-Time-Drone-Data-Analysis.git
   cd CS399-Real-Time-Drone-Data-Analysis
   ```

2. Install dependencies:  
   ```bash
   pip install -r requirements.txt
   ```

## Results

- The pipeline produces high-quality stitched panoramas with accurately detected and annotated objects.  
![Object Detection](https://github.com/user-attachments/assets/e9449978-acbf-4ec6-b488-24cbce8eaa7d)


## Future Work

- Extend the pipeline with:  
  - Distributed processing on drones for low-latency analysis.  
  - Advanced drone navigation and control systems.  
  - Real-time optimizations for object detection in resource-constrained environments.  

---

## Contributing

Contributions are welcome! Fork the repository and submit a pull request to suggest improvements or add new features.

---

## Acknowledgments

Special thanks to **Professor Anirban Dasgupta** for his guidance and support throughout the project.

---

## Contact

For questions or suggestions, please reach out to **Dhruv Sharma** at dhruv.sharma@iitgn.ac.in.
