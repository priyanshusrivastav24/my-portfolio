"""
Generates an official styled PDF resume for Priyanshu Kumar Srivastav.
"""
import os

pdf_content = b"""%PDF-1.4
1 0 obj
<<
  /Type /Catalog
  /Pages 2 0 R
>>
endobj
2 0 obj
<<
  /Type /Pages
  /Kids [3 0 R]
  /Count 1
>>
endobj
3 0 obj
<<
  /Type /Page
  /Parent 2 0 R
  /MediaBox [0 0 612 792]
  /Contents 4 0 R
  /Resources <<
    /Font <<
      /F1 5 0 R
      /F2 6 0 R
    >>
  >>
>>
endobj
4 0 obj
<< /Length 1350 >>
stream
BT
/F1 20 Tf
50 740 Td
(PRIYANSHU KUMAR SRIVASTAV) Tj
/F2 10 Tf
0 -18 Td
(+91 6307858366 | priyanshpriyansh34@gmail.com | LinkedIn Profile) Tj
0 -20 Td
/F1 12 Tf
(PROFILE) Tj
/F2 9.5 Tf
0 -14 Td
(Electronics and Communication Engineering student with strong interest in Embedded Systems, IoT, and) Tj
0 -12 Td
(Digital Design. Experienced in developing microcontroller-based systems using Embedded C, Arduino, STM32,) Tj
0 -12 Td
(and Raspberry Pi. Skilled in hardware-software integration, sensor interfacing, and firmware development.) Tj
0 -18 Td
/F1 12 Tf
(TECHNICAL SKILLS) Tj
/F2 9.5 Tf
0 -14 Td
(Programming: C, C++, Embedded C, Python) Tj
0 -12 Td
(Embedded Systems: Arduino UNO, STM32, ESP32, Raspberry Pi, Sensor Interfacing, IoT Systems, Infineon Programmer) Tj
0 -12 Td
(Tools: Proteus, EasyEDA, Arduino IDE, VS Code, STM32CubeIDE, Infineon iMotion Link, Git, FreeRTOS) Tj
0 -12 Td
(Concepts: Microcontrollers, UART, SPI, I2C Communication, Digital Logic Design, PCB Design Basics, Testing, Debugging) Tj
0 -18 Td
/F1 12 Tf
(WORK EXPERIENCE) Tj
/F2 9.5 Tf
0 -14 Td
(Embedded Systems Intern - Virtual Forest Private Limited) Tj
0 -12 Td
(- Developed embedded applications using microcontrollers and Embedded C.) Tj
0 -12 Td
(- Implemented sensor interfacing and hardware-software integration.) Tj
0 -12 Td
(- Assisted in debugging firmware and validating embedded prototypes.) Tj
0 -12 Td
(- Worked on IoT-based embedded solutions for real-time monitoring systems.) Tj
0 -18 Td
/F1 12 Tf
(PROJECTS) Tj
/F2 9.5 Tf
0 -14 Td
(Infineon Gang Programmer Development) Tj
0 -12 Td
(- Developed a Gang Programmer system to flash multiple Infineon microcontrollers simultaneously.) Tj
0 -12 Td
(- Built using Raspberry Pi and Infineon iMotion Link for Outdoor AC and Portable AC unit controllers.) Tj
0 -12 Td
(- Integrated support for two different Infineon microcontrollers through a single unified setup.) Tj
0 -14 Td
(Dynamic Programming System for Outdoor and Portable AC Units) Tj
0 -12 Td
(- Developed a dynamic embedded programming system using Raspberry Pi and Infineon iMotion Link.) Tj
0 -14 Td
(PID Based DC Motor Speed Control using STM32) Tj
0 -12 Td
(- Designed closed-loop DC motor control using STM32, PWM, and optical encoder feedback.) Tj
0 -18 Td
/F1 12 Tf
(EDUCATION & LEADERSHIP) Tj
/F2 9.5 Tf
0 -14 Td
(Mahatma Jyotiba Phule Rohilkhand University, Bareilly - B.Tech (ECE) (2022 - 2026)) Tj
0 -12 Td
(Pawanagar Mahaveer Inter College, Kushinagar - Intermediate (2021 - 2022)) Tj
0 -12 Td
(President - Embedronics Club: Organized workshops on Embedded Systems and IoT; mentored students.) Tj
ET
endstream
endobj
5 0 obj
<<
  /Type /Font
  /Subtype /Type1
  /BaseFont /Helvetica-Bold
>>
endobj
6 0 obj
<<
  /Type /Font
  /Subtype /Type1
  /BaseFont /Helvetica
>>
endobj
xref
0 7
0000000000 65535 f 
0000000009 00000 n 
0000000058 00000 n 
0000000115 00000 n 
0000000266 00000 n 
0000001668 00000 n 
0000001745 00000 n 
trailer
<<
  /Size 7
  /Root 1 0 R
>>
startxref
1817
%%EOF
"""

out_dir = os.path.join(os.path.dirname(__file__), "static", "assets")
os.makedirs(out_dir, exist_ok=True)

# Save both filenames for complete compatibility
for filename in ["Priyanshu_Kumar_Srivastav_Resume.pdf", "Alex_Carter_Resume.pdf"]:
    path = os.path.join(out_dir, filename)
    with open(path, "wb") as f:
        f.write(pdf_content)

print("[+] Generated Priyanshu_Kumar_Srivastav_Resume.pdf")
