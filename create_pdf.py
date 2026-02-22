from fpdf import FPDF
import os

class AbstractPDF(FPDF):
    def header(self):
        self.set_font('helvetica', 'B', 15)
        self.cell(0, 10, 'FaceRec Pro: Project Abstract', 0, 1, 'C')
        self.ln(5)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

    def chapter_title(self, label):
        self.set_font('helvetica', 'B', 12)
        self.set_fill_color(200, 220, 255)
        self.cell(0, 10, label, 0, 1, 'L', fill=True)
        self.ln(4)

    def chapter_body(self, text):
        self.set_font('helvetica', '', 11)
        self.multi_cell(0, 8, text)
        self.ln()

    def add_diagram_placeholder(self, title, description):
        self.set_font('helvetica', 'B', 11)
        self.cell(0, 10, title, 0, 1, 'L')
        self.set_font('helvetica', 'I', 10)
        self.multi_cell(0, 6, f"Summary: {description}")
        self.ln(5)

def create_abstract():
    pdf = AbstractPDF()
    pdf.add_page()
    
    # 1. Introduction
    pdf.chapter_title('1. Introduction')
    intro_text = (
        "FaceRec Pro is an AI-driven real-time surveillance and attendance management system "
        "designed to address the challenge of students skipping classes. Unlike traditional "
        "attendance systems that only record presence at the start of a session, FaceRec Pro "
        "provides continuous monitoring using a dual-camera setup. By leveraging state-of-the-art "
        "deep learning models, the system tracks students' movements between classrooms and "
        "corridors, automatically flagging unauthorized absences and notifying authorities in real-time."
    )
    pdf.chapter_body(intro_text)

    # 2. Tech Stack
    pdf.chapter_title('2. Tech Stack')
    tech_stack = (
        "* Frontend: A responsive 'Glassmorphic' web interface developed with Vanilla HTML, CSS, and JavaScript.\n"
        "* Backend: Powered by Python and the Django Web Framework for secure and scalable server-side operations.\n"
        "* Database: MySQL is used for persistent storage of student records, attendance logs, and system alerts.\n"
        "* AI Engine: YOLOv11 for high-speed face detection and face_recognition for precise identification."
    )
    pdf.chapter_body(tech_stack)

    # 3. Working Methodology
    pdf.chapter_title('3. Working Methodology')
    working = (
        "1. Dual-Camera Acquisition: The system captures live video feeds from a 'Classroom' camera and a 'Corridor' camera.\n"
        "2. Face Detection & Recognition: Each frame is processed by YOLOv11 to locate faces, followed by identification using deep learning encodings.\n"
        "3. Presence Tracking: Students in the Classroom are marked 'Present'. If a student is missing for >15s, a 'Missing' state is triggered.\n"
        "4. Automated Alerts: The system monitors the Corridor for the student and sends email alerts to administrators upon confirmed absence.\n"
        "5. Data Logging: All events are recorded in MySQL and displayed on a real-time Dashboard."
    )
    pdf.chapter_body(working)

    # 4. Diagrams Documentation
    pdf.chapter_title('4. System Diagrams (Logical Overview)')
    
    pdf.add_diagram_placeholder(
        "4.1 Data Flow Diagram (DFD Level 0)",
        "The DFD illustrates the flow of student eye/face data from CCTV cameras to the Django Engine. "
        "The engine interacts with the MySQL Database to log attendance and missing events, "
        "while simultaneously updating the Admin Dashboard and sending Email Alerts."
    )

    pdf.add_diagram_placeholder(
        "4.2 Entity-Relationship (ER) Diagram",
        "Entities: PERSON (Student details), FACE_IMAGE (Multiple encodings per student), "
        "ATTENDANCE (Daily logs), MISSING_LOG (Alert history), and DEPARTMENT. "
        "Relationships: A Person HAS many FaceImages, MARKS many Attendance records, and TRIGGERS MissingLogs."
    )

    pdf.add_diagram_placeholder(
        "4.3 System Architecture",
        "Layers: Input Layer (Dual Cameras) -> Processing Layer (OpenCV, YOLOv11, FaceRec) -> "
        "Data Layer (MySQL, Media Repository) -> Presentation Layer (Glassmorphic Web UI, Email Service)."
    )

    # Final Summary
    pdf.chapter_title('5. Conclusion')
    conclusion = (
        "FaceRec Pro provides a automated solution for educational institutions to ensure "
        "student accountability. By combining real-time AI detection with proactive alerting, "
        "it bridges the gap in traditional attendance monitoring."
    )
    pdf.chapter_body(conclusion)

    output_path = 'FaceRec_Pro_Abstract.pdf'
    pdf.output(output_path)
    print(f"PDF successfully generated: {os.path.abspath(output_path)}")

if __name__ == "__main__":
    create_abstract()
