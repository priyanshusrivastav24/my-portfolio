"""
Portfolio Data Configuration - Priyanshu Kumar Srivastav
=========================================================
All information accurately populated from Priyanshu's official resume.
"""

PROFILE = {
    "name": "Priyanshu Kumar Srivastav",
    "short_name": "Priyanshu",
    "title": "Embedded Systems & IoT Engineer",
    "roles": [
        "Embedded Systems Engineer",
        "Firmware & IoT Developer",
        "STM32 & Microcontroller Specialist",
        "Hardware-Software Integration Specialist"
    ],
    "tagline": "Electronics and Communication Engineering student with deep expertise in Embedded Systems, IoT, and Digital Design. Experienced in microcontroller-based system design, sensor interfacing, firmware development, and real-time embedded architectures.",
    "email": "priyanshpriyansh34@gmail.com",
    "phone": "+91 6307858366",
    "location": "Bareilly / Kushinagar, India (Open to Relocation & Remote)",
    "availability_status": "Available for Embedded Systems & IoT Roles",
    "years_experience": "2+",
    "projects_completed": "12+",
    "uptime_rate": "99.9%",
    "code_commits": "500+",
    "resume_filename": "Priyanshu_Kumar_Srivastav_Resume.pdf",
    "resume_url": "/resume",
    "resume_static_url": "static/assets/Priyanshu_Kumar_Srivastav_Resume.pdf",
    "social": {
        "github": "https://github.com",
        "linkedin": "https://linkedin.com",
        "twitter": "https://twitter.com",
        "discord": "https://discord.com",
        "kaggle": "https://kaggle.com"
    }
}

ABOUT = {
    "headline": "Bridging hardware circuits and firmware with precision Embedded C & Microcontroller architectures.",
    "story_paragraphs": [
        "I am an Electronics and Communication Engineering student at Mahatma Jyotiba Phule Rohilkhand University with a passionate drive for Embedded Systems, IoT, and Digital Design.",
        "Having worked as an Embedded Systems Intern at Virtual Forest Private Limited, I specialize in developing microcontroller-based systems using Embedded C, Arduino, STM32, and Raspberry Pi. My technical expertise spans sensor interfacing, hardware-software integration, low-level firmware development, and real-time embedded system design.",
        "As President of the Embedronics Club, I regularly organize technical workshops on Embedded Systems and IoT, mentoring fellow students in microcontroller programming, circuit analysis, and hardware prototyping."
    ],
    "highlights": [
        {
            "icon": "code",
            "title": "Firmware & Embedded C",
            "description": "Writing robust, deterministic low-level firmware in Embedded C, C, and Python for ARM Cortex-M, STM32, and AVR microcontrollers."
        },
        {
            "icon": "zap",
            "title": "Microcontrollers & IoT",
            "description": "Developing real-time systems using STM32, ESP32, Arduino, and Raspberry Pi with sensors and wireless communication."
        },
        {
            "icon": "layers",
            "title": "Hardware-Software Integration",
            "description": "Mastering communication protocols including UART, SPI, and I2C for peripheral control, data acquisition, and module bridging."
        },
        {
            "icon": "shield-check",
            "title": "Testing, Debugging & PCB",
            "description": "Validating prototypes using STM32CubeIDE, EasyEDA, Proteus simulation, logic analyzers, and hardware debugging tools."
        }
    ],
    "terminal_snippets": [
        {"prompt": "priyanshu@embedded-core:~$", "command": "stm32flash -w firmware.bin -v /dev/ttyUSB0"},
        {"prompt": "status:", "command": "Flash Verified • Clock: 72MHz • Peripherals Online"},
        {"prompt": "protocols:", "command": "['UART', 'SPI', 'I2C', 'PWM', 'FreeRTOS']"},
        {"prompt": "target_mcu:", "command": "STM32F103 / ESP32 / Raspberry Pi"}
    ]
}

SKILL_CATEGORIES = [
    {
        "id": "programming-languages",
        "name": "Programming & Firmware",
        "skills": [
            {"name": "Embedded C", "level": 94, "experience": "2+ yrs", "badge": "Core Strength"},
            {"name": "C Programming", "level": 92, "experience": "3+ yrs", "badge": "Proficient"},
            {"name": "C++", "level": 85, "experience": "2+ yrs", "badge": "Intermediate"},
            {"name": "Python (Hardware & Scripts)", "level": 88, "experience": "2+ yrs", "badge": "Advanced"},
            {"name": "FreeRTOS Basics", "level": 82, "experience": "1+ yr", "badge": "Applied"},
            {"name": "Digital Logic & Registers", "level": 90, "experience": "3+ yrs", "badge": "Strong"}
        ]
    },
    {
        "id": "embedded-hardware",
        "name": "Embedded Systems & MCUs",
        "skills": [
            {"name": "STM32 (ARM Cortex-M)", "level": 92, "experience": "2+ yrs", "badge": "Advanced"},
            {"name": "Arduino UNO / Nano", "level": 95, "experience": "3+ yrs", "badge": "Expert"},
            {"name": "ESP32 & IoT Systems", "level": 90, "experience": "2+ yrs", "badge": "Advanced"},
            {"name": "Raspberry Pi", "level": 88, "experience": "2+ yrs", "badge": "Proficient"},
            {"name": "Infineon iMotion Link & MCUs", "level": 86, "experience": "Virtual Forest", "badge": "Specialized"},
            {"name": "Sensor Interfacing (ADC, DAC)", "level": 94, "experience": "2+ yrs", "badge": "Expert"}
        ]
    },
    {
        "id": "tools-protocols",
        "name": "Tools, Protocols & EDA",
        "skills": [
            {"name": "Communication: UART, SPI, I2C", "level": 95, "experience": "2+ yrs", "badge": "Mastery"},
            {"name": "STM32CubeIDE & Keil", "level": 90, "experience": "2+ yrs", "badge": "Advanced"},
            {"name": "Proteus Circuit Simulation", "level": 88, "experience": "2+ yrs", "badge": "Proficient"},
            {"name": "EasyEDA & PCB Design Basics", "level": 84, "experience": "1+ yr", "badge": "Applied"},
            {"name": "Git & VS Code", "level": 88, "experience": "2+ yrs", "badge": "Proficient"},
            {"name": "Hardware Testing & Debugging", "level": 92, "experience": "2+ yrs", "badge": "Advanced"}
        ]
    }
]

TECH_TAGS = [
    "Embedded C", "C/C++", "STM32", "Arduino", "ESP32", "Raspberry Pi",
    "Infineon iMotion", "UART", "SPI", "I2C", "PWM Control", "PID Algorithms",
    "STM32CubeIDE", "EasyEDA", "Proteus", "FreeRTOS", "Sensor Interfacing",
    "IoT Systems", "PCB Design", "Digital Logic", "Firmware Debugging", "Git"
]

PROJECTS = [
    {
        "id": "infineon-gang-programmer",
        "title": "Infineon Gang Programmer Development",
        "category": "embedded",
        "category_badge": "Industrial Embedded",
        "tagline": "Multi-microcontroller simultaneous flashing system built using Raspberry Pi and Infineon iMotion Link.",
        "description": "Developed an industrial Gang Programmer system designed to flash multiple Infineon microcontrollers simultaneously. Engineered for production manufacturing lines to dramatically accelerate unit programming cycles.",
        "highlights": [
            "Flashing multiple Infineon microcontrollers simultaneously to maximize throughput",
            "Built using Raspberry Pi and Infineon iMotion Link for automated production environments",
            "Configured with support for programming both Outdoor AC and Portable AC unit controllers",
            "Integrated support for two different Infineon microcontroller architectures into a single unified setup",
            "Significantly reduced unit programming cycle time and streamlined configuration"
        ],
        "tech_stack": ["Raspberry Pi", "Infineon iMotion Link", "Embedded C", "Python", "Bash", "Hardware Testing"],
        "stats": "Multi-MCU Parallel Flashing • Production Ready",
        "github_url": "https://github.com",
        "demo_url": "https://github.com",
        "accent_gradient": "linear-gradient(135deg, #8B5CF6 0%, #38BDF8 100%)",
        "mockup_type": "industrial"
    },
    {
        "id": "dynamic-ac-programming",
        "title": "Dynamic Programming System for Outdoor & Portable ACs",
        "category": "embedded",
        "category_badge": "Firmware & Automation",
        "tagline": "Automated dynamic programming framework for HVAC embedded controller boards.",
        "description": "Engineered a dynamic embedded programming system using Raspberry Pi and Infineon iMotion Link. Designed to program and verify firmware across outdoor and portable AC unit controller boards with zero hardware mismatch.",
        "highlights": [
            "Dynamic embedded programming system utilizing Raspberry Pi and Infineon iMotion Link",
            "Multi-target support for flashing two distinct Infineon microcontrollers in one integrated setup",
            "Improved firmware deployment efficiency and eliminated manual configuration overhead",
            "Integrated automated firmware integrity check and post-flash validation"
        ],
        "tech_stack": ["Raspberry Pi", "Infineon Programmer", "Embedded C", "UART/SPI", "Linux"],
        "stats": "100% Automated • Zero Configuration Errors",
        "github_url": "https://github.com",
        "demo_url": "https://github.com",
        "accent_gradient": "linear-gradient(135deg, #38BDF8 0%, #8B5CF6 100%)",
        "mockup_type": "firmware"
    },
    {
        "id": "stm32-pid-motor-control",
        "title": "PID Based DC Motor Speed Control using STM32",
        "category": "control",
        "category_badge": "Control Systems & STM32",
        "tagline": "Precision closed-loop DC motor velocity control using STM32 ARM Cortex-M and real-time encoder feedback.",
        "description": "Designed and implemented a closed-loop DC motor speed control system using an STM32 microcontroller. Built a discrete-time PID control algorithm in Embedded C with real-time encoder feedback capture.",
        "highlights": [
            "Designed closed-loop DC motor speed regulation hardware and firmware using STM32",
            "Implemented PID control algorithm in Embedded C using PWM generation and quadrature encoder feedback",
            "Fine-tuned Proportional, Integral, and Derivative gains for rapid response and minimal overshoot",
            "Configured STM32 hardware timers for high-frequency PWM switching and pulse accumulation"
        ],
        "tech_stack": ["STM32", "Embedded C", "PWM", "Optical Encoder", "STM32CubeIDE", "Control Theory"],
        "stats": "Sub-millisecond Feedback • Stable Speed Regulation",
        "github_url": "https://github.com",
        "demo_url": "https://github.com",
        "accent_gradient": "linear-gradient(135deg, #8B5CF6 0%, #06B6D4 100%)",
        "mockup_type": "motor"
    },
    {
        "id": "iot-sensor-telemetry-node",
        "title": "IoT Embedded Telemetry & Monitoring Node",
        "category": "iot",
        "category_badge": "IoT & Sensor Interfacing",
        "tagline": "Multi-sensor hardware data acquisition and wireless telemetry node built with ESP32 and microcontrollers.",
        "description": "Developed an end-to-end IoT sensor interfacing system for real-time environmental monitoring. Communicates with digital and analog sensors over I2C and SPI buses with secure wireless telemetry dispatch.",
        "highlights": [
            "Interfaced analog and digital sensors with calibrate filtering algorithms",
            "Implemented multi-protocol communication using I2C and SPI bus lines",
            "Constructed low-power sleep state cycles for extended battery efficiency",
            "Real-time sensor telemetry transmission with packet validation"
        ],
        "tech_stack": ["ESP32", "Arduino UNO", "Embedded C", "I2C/SPI", "IoT Systems"],
        "stats": "Real-time Telemetry • Low-Power Modes",
        "github_url": "https://github.com",
        "demo_url": "https://github.com",
        "accent_gradient": "linear-gradient(135deg, #38BDF8 0%, #10B981 100%)",
        "mockup_type": "iot"
    },
    {
        "id": "easyeda-pcb-design",
        "title": "Embedded Circuit Simulation & PCB Design",
        "category": "pcb",
        "category_badge": "PCB Design & EDA",
        "tagline": "Schematic capture, circuit simulation, and 2-layer PCB layout using Proteus and EasyEDA.",
        "description": "Designed hardware schematics and printed circuit board layouts for microcontroller breakout and sensor conditioning circuits. Performed simulation in Proteus prior to hardware prototyping.",
        "highlights": [
            "Schematic design and component layout using EasyEDA and Proteus",
            "Simulation of digital logic, transistor switching, and analog signal conditioning",
            "Designed 2-layer PCB layout with optimized trace routing and ground planes",
            "Generated Gerber files and validated Design Rule Checks (DRC)"
        ],
        "tech_stack": ["EasyEDA", "Proteus", "PCB Design", "Digital Logic", "Circuit Analysis"],
        "stats": "Verified Simulation • 2-Layer PCB Layout",
        "github_url": "https://github.com",
        "demo_url": "https://github.com",
        "accent_gradient": "linear-gradient(135deg, #8B5CF6 0%, #EC4899 100%)",
        "mockup_type": "pcb"
    },
    {
        "id": "multi-protocol-comm-bridge",
        "title": "UART, SPI & I2C Protocol Bridge",
        "category": "embedded",
        "category_badge": "Serial Communication",
        "tagline": "Deterministic serial communication bridge for inter-microcontroller data exchange.",
        "description": "Constructed an embedded communication bridge capable of translating and routing packets across UART, SPI, and I2C buses. Includes frame packetization, checksum verification, and error recovery.",
        "highlights": [
            "Multi-bus protocol translation between STM32 and Arduino master/slave nodes",
            "Custom packet framing with CRC error detection and buffer overflow protection",
            "Verified signal timing and bus integrity using oscilloscope and logic analyzer",
            "Deterministic interrupt-driven serial receive/transmit buffers"
        ],
        "tech_stack": ["STM32", "Arduino", "Embedded C", "UART", "SPI", "I2C"],
        "stats": "115200 Baud UART • 400kHz I2C Verified",
        "github_url": "https://github.com",
        "demo_url": "https://github.com",
        "accent_gradient": "linear-gradient(135deg, #6366F1 0%, #38BDF8 100%)",
        "mockup_type": "serial"
    }
]

EDUCATION = [
    {
        "type": "education",
        "title": "B.Tech – Electronics and Communication Engineering",
        "institution": "Mahatma Jyotiba Phule Rohilkhand University, Bareilly",
        "period": "2022 — 2026",
        "badge": "Undergraduate Degree",
        "grade": "B.Tech in ECE (Current)",
        "description": "Focused on Embedded Systems, Microcontrollers (STM32, 8051, AVR), IoT Architectures, Digital Logic Design, and Signal Conditioning.",
        "highlights": [
            "Coursework: Microcontrollers & Microprocessors, Digital Logic, Electronic Circuit Design, Signals & Systems",
            "Hands-on project work in microcontroller programming, firmware development, and hardware-software integration",
            "Active developer and participant in technical embedded prototyping competitions"
        ]
    },
    {
        "type": "education",
        "title": "Intermediate (Senior Secondary)",
        "institution": "Pawanagar Mahaveer Inter College, Kushinagar",
        "period": "2021 — 2022",
        "badge": "Senior Secondary",
        "grade": "PCM (Physics, Chemistry, Mathematics)",
        "description": "Completed Senior Secondary education with foundational focus on Physics, Mathematics, and Analytical Sciences.",
        "highlights": [
            "Core Focus: Physics, Chemistry, and Advanced Mathematics",
            "Developed strong foundation in electrical physics, magnetism, and algebra"
        ]
    },
    {
        "type": "certification",
        "title": "Embedded Systems and PCB Design",
        "institution": "Virtual Forest Private Limited",
        "period": "Internship Certificate",
        "badge": "Industrial Certification",
        "grade": "Certificate Verified",
        "description": "Comprehensive industrial training and internship certification covering microcontroller firmware, sensor interfacing, and hardware prototyping.",
        "highlights": [
            "Embedded firmware development with microcontrollers and Embedded C",
            "Sensor interfacing and hardware-software integration for real-time monitoring",
            "Assisted in hardware debugging, PCB concepts, and prototype validation"
        ]
    }
]

EXPERIENCE = [
    {
        "type": "experience",
        "role": "Embedded Systems Intern",
        "company": "Virtual Forest Private Limited",
        "period": "Internship",
        "badge": "Industry Experience",
        "description": "Developed embedded applications, firmware solutions, and hardware-software integrations for microcontroller-based products.",
        "achievements": [
            "Developed embedded applications using microcontrollers and Embedded C.",
            "Implemented sensor interfacing and hardware-software integration.",
            "Assisted in debugging firmware and validating embedded prototypes.",
            "Worked on IoT-based embedded solutions for real-time monitoring systems."
        ]
    },
    {
        "type": "experience",
        "role": "President – Embedronics Club",
        "company": "Mahatma Jyotiba Phule Rohilkhand University",
        "period": "Leadership",
        "badge": "University Leadership",
        "description": "Lead the university technical student society dedicated to Embedded Systems, Robotics, and IoT technologies.",
        "achievements": [
            "Organized technical workshops on Embedded Systems and IoT for university students.",
            "Mentored students in microcontroller programming (Arduino, STM32) and hardware interfacing.",
            "Promoted hands-on learning through project-based build sessions and competitive hackathons."
        ]
    }
]

CONTACT_INFO = {
    "email": "priyanshpriyansh34@gmail.com",
    "phone": "+91 6307858366",
    "location": "Bareilly / Kushinagar, Uttar Pradesh, India",
    "timezone": "IST (UTC+5:30) • Flexible for Opportunities",
    "responseTime": "Within 24 Hours",
    "status": "Available for Embedded Systems & IoT Roles"
}
