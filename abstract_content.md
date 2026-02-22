# Abstract: FaceRec Pro - Anti-Class Skipping System

## 1. Introduction
FaceRec Pro is an AI-driven real-time surveillance and attendance management system designed to address the challenge of students skipping classes. Unlike traditional attendance systems that only record presence at the start of a session, FaceRec Pro provides continuous monitoring using a dual-camera setup. By leveraging state-of-the-art deep learning models, the system tracks students' movements between classrooms and corridors, automatically flagging unauthorized absences and notifying authorities in real-time.

## 2. Tech Stack
The project is built using a modern and robust technology stack:
*   **Frontend:** A responsive "Glassmorphic" web interface developed with Vanilla HTML, CSS, and JavaScript.
*   **Backend:** Powered by Python and the Django Web Framework for secure and scalable server-side operations.
*   **Database:** MySQL is used for persistent storage of student records, attendance logs, and system alerts.
*   **AI Engine:** 
    *   **YOLOv11:** For high-speed and accurate face detection.
    *   **face_recognition:** A deep learning-based library for precise face identification and encoding.

## 3. Working Methodology
FaceRec Pro operates on a multi-stage pipeline:
1.  **Dual-Camera Acquisition:** The system simultaneously captures live video feeds from a "Classroom" camera (Zone 1) and a "Corridor" camera (Zone 2).
2.  **Face Detection & Recognition:** Each frame is processed by the YOLOv11 model to locate faces. Detected faces are then compared against a pre-encoded database of student faces.
3.  **Presence Tracking:** 
    *   If a target student is detected in the **Classroom**, they are marked "Present".
    *   If a student is missing from the Classroom for more than a set threshold (e.g., 15 seconds), the system triggers a "Missing" state.
    *   The **Corridor** camera monitors if the "missing" student is wandering outside.
4.  **Automated Alerts:** Upon confirming an unauthorized absence, the system automatically sends an email notification to the administrator, including timestamps and location details.
5.  **Data Logging:** All events (attendance, missing logs, corridor sightings) are recorded in the database and accessible via a real-time management dashboard.

## 4. System Architecture
(Diagram to be inserted)
The system follows a modular architecture where the CCTV feeds are piped into a processing engine (Django + OpenCV), which interacts with the AI models and the MySQL database to serve the Web Dashboard.

## 5. DFD (Data Flow Diagram) - Level 0
(Diagram to be inserted)
The DFD illustrates the flow of student face data and video streams from cameras to the processing unit, resulting in attendance records, log entries, and email alerts for the admin.

## 6. ER (Entity-Relationship) Diagram
(Diagram to be inserted)
The database schema consists of key entities:
*   **Person:** Stores student details (Name, Class, Dept).
*   **FaceImage:** Stores multiple face encodings per student for robust recognition.
*   **Attendance:** Records the daily "Time In" for each student.
*   **MissingLog:** Captures instances of students missing or found in corridors.
*   **Department:** Categorizes students.
