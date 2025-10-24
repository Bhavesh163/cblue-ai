"""Knowledge base with semantic matching for Cblue services"""

KNOWLEDGE_BASE = {
    "services_overview": {
        "keywords": ["your services", "what services", "what do you do", "your solutions", "what solutions", "what are you doing", "who are we", "who are you", "what are your offers", "บริการของคุณคืออะไร", "โซลูชันของคุณคืออะไร", "ข้อเสนอของคุณคืออะไร", "คุณกำลังทำอะไรอยู่", "เราคือใคร", "คุณคือใคร", "你在做什么", "我们是谁", "你是谁", "你们的服务是什么", "你们的解决方案是什么", "你们的产品"],
        "content": """Cblue Thailand offers a comprehensive suite of services focused on AI/Digital Solutions, sustainable technology solutions, and construction, engineering.

The services can be grouped into several key areas:

• Digital Solutions: AI chatbot development, software development, and machine learning.
• Smart Technology & Automation: Building Management Systems (BMS), smart building controls, automation, and energy-saving solutions.
• Renewable Energy & EV Solutions: Solar power, wind turbines, and EV charging stations.
• Design & Engineering: Full architectural, interior, landscape, and detailed engineering design.
• Construction & Specialized Trades: General construction, fit-outs, HVAC, MEP systems, retrofitting, and green building (including vertical gardens).
• Specialized Fabrication: Metal sheet, steel structure, aluminium, and glass work.
• Consulting & Strategy: Market research, economic evaluations, feasibility studies, and project management.

---

Cblue Thailand นำเสนอบริการที่ครอบคลุมและหลากหลาย โดยเน้นโซลูชันด้าน AI/ดิจิทัล โซลูชันเทคโนโลยีที่ยั่งยืน และงานก่อสร้างและวิศวกรรม

บริการสามารถจัดกลุ่มได้เป็นหลายด้านหลัก ดังนี้:

• โซลูชันดิจิทัล: การพัฒนาแชทบอท AI, การพัฒนาซอฟต์แวร์, และการเรียนรู้ของเครื่อง (Machine Learning)
• เทคโนโลยีอัจฉริยะและระบบอัตโนมัติ: ระบบบริหารจัดการอาคาร (BMS), ระบบควบคุมอาคารอัจฉริยะ, ระบบอัตโนมัติ, และโซลูชันประหยัดพลังงาน
• พลังงานหมุนเวียนและโซลูชัน EV: พลังงานแสงอาทิตย์, กังหันลม, และสถานีชาร์จรถยนต์ไฟฟ้า
• การออกแบบและวิศวกรรม: การออกแบบสถาปัตยกรรม, ออกแบบตกแต่งภายใน, ภูมิสถาปัตย์, และการออกแบบวิศวกรรมโดยละเอียดครบวงจร
• งานก่อสร้างและงานช่างเฉพาะทาง: งานก่อสร้างทั่วไป, งานตกแต่งภายใน, ระบบปรับอากาศ, ระบบ MEP (เครื่องกล-ไฟฟ้า-ประปา), งานปรับปรุงอาคาร, และอาคารเขียว (รวมถึงสวนแนวตั้ง)
• งานผลิตเฉพาะทาง: งานแผ่นโลหะ, โครงสร้างเหล็ก, อลูมิเนียม, และงานกระจก
• ที่ปรึกษาและกลยุทธ์: การวิจัยตลาด, การประเมินทางเศรษฐศาสตร์, การศึกษาความเป็นไปได้, และการบริหารโครงการ

---

Cblue Thailand 提供全面的服务套餐，专注于人工智能/数字化解决方案、可持续技术解决方案以及建筑工程。

服务可分为以下几个关键领域:

• 数字化解决方案: AI聊天机器人开发、软件开发和机器学习
• 智能技术与自动化: 楼宇管理系统(BMS)、智能建筑控制、自动化和节能解决方案
• 可再生能源与电动汽车解决方案: 太阳能、风力涡轮机和电动汽车充电站
• 设计与工程: 全方位建筑设计、室内设计、景观设计和详细工程设计
• 建筑与专业工程: 一般建筑施工、装修工程、暖通空调系统、机电管道系统(MEP)、改造工程和绿色建筑(包括垂直花园)
• 专业制造: 金属板材、钢结构、铝材和玻璃工程
• 咨询与策略: 市场研究、经济评估、可行性研究和项目管理"""
    },
    "ai_general": {
        "keywords": ["what is ai", "ai คือ", "artificial intelligence"],
        "content": """Artificial Intelligence (AI)

AI is technology that enables computers to simulate human intelligence, including learning, reasoning, and problem-solving. AI systems can analyze data, recognize patterns, make decisions, and improve performance over time without explicit programming.

Applications:
• Virtual assistants and chatbots
• Image and speech recognition
• Autonomous vehicles
• Predictive analytics
• Natural language processing"""
    },
    "solar": {
        "keywords": ["solar", "solar panel", "solar energy", "solar solution", "photovoltaic", "renewable energy", "พลังงานแสงอาทิตย์", "โซล่าเซลล์"],
        "content": """Solar Solutions

Renewable energy systems using solar panels to convert sunlight into electricity.

Services:
• Solar panels & photovoltaic systems
• Renewable energy integration
• Clean energy technology
• Cost-effective power generation
• Sustainable energy solutions"""
    },
    "ev_charger": {
        "keywords": ["ev charger", "electric vehicle charger", "car charger", "charging station", "เครื่องชาร์จรถยนต์ไฟฟ้า", "ชาร์จรถไฟฟ้า"],
        "content": """EV Charger

Electric vehicle charging stations that replenish EV batteries.

Types:
• Level 1: Standard home outlet (slow, 8-12 hours)
• Level 2: Faster home/public charging (3-8 hours)
• DC Fast Charging: Rapid charging for long trips (30-60 minutes)

Benefits:
• Convenient home or public charging
• Smart charging capabilities
• Renewable energy integration
• Cost-effective operation"""
    },
    "ev": {
        "keywords": ["ev", "electric vehicle", "what is ev", "รถไฟฟ้า"],
        "content": """Electric Vehicle (EV)

A car powered by electric motors using energy stored in rechargeable batteries, instead of gasoline or diesel.

Benefits:
• Zero direct emissions
• Quieter operation
• Lower operating costs
• Reduced maintenance
• Environmentally friendly"""
    },
    "green_architecture": {
        "keywords": ["green architecture", "green architechture", "eco-friendly design", "sustainable architecture", "สถาปัตยกรรมสีเขียว", "อาคารเขียว"],
        "content": """Green Architecture

Eco-friendly buildings harmonizing with nature.

Services:
• Architectural, Interior, Landscape design
• Detailed engineering design
• Energy-efficient systems
• Sustainable materials
• Environmental design"""
    },
    "hvac": {
        "keywords": ["hvac", "air conditioning", "ventilation", "heating", "ระบบปรับอากาศ", "แอร์"],
        "content": """HVAC Solutions (ระบบปรับอากาศ):
- Energy efficiency optimization
- Indoor comfort systems
- System reliability
- Heating, Ventilation, Air Conditioning
- Climate control systems
- Energy-efficient HVAC

Contact: cblue.thailand@gmail.com, +66 (0)81 854 4291"""
    },
    "mep": {
        "keywords": ["mep", "mechanical electrical plumbing", "ระบบไฟฟ้า", "ระบบประปา"],
        "content": """MEP (Mechanical, Electrical, Plumbing):
- Mechanical systems design
- Electrical systems installation
- Plumbing infrastructure
- Building systems integration
- Energy-efficient MEP solutions
- System reliability

Contact: cblue.thailand@gmail.com, +66 (0)81 854 4291"""
    },
    "retrofit": {
        "keywords": ["retrofit", "renovation", "renovate", "upgrade", "what is renovation", "ปรับปรุง", "รีโนเวท"],
        "content": """Retrofit & Renovation Services

Renovation:
The process of improving, updating, or restoring a building or space. Includes repairs, modernization, and aesthetic improvements to enhance functionality, appearance, and value while extending the building's lifespan.

Retrofit:
Upgrading existing buildings with new systems or features to improve energy efficiency, safety, or performance without complete reconstruction.

Services:
• Building retrofit and upgrades
• Energy efficiency improvements
• System modernization
• Building renovation
• Performance optimization"""
    },
    "controls": {
        "keywords": ["controls", "control system", "ระบบควบคุม", "การควบคุม"],
        "content": """Controls (ระบบควบคุม):
- Building control systems
- Automated control solutions
- System monitoring
- Real-time control
- Energy management controls
- Smart control systems

Contact: cblue.thailand@gmail.com, +66 (0)81 854 4291"""
    },
    "automation": {
        "keywords": ["automation", "automated", "ระบบอัตโนมัติ", "อัตโนมัติ"],
        "content": """Automation (ระบบอัตโนมัติ):
- Building automation systems
- Process automation
- Smart automation solutions
- Automated monitoring
- Efficiency through automation
- IoT integration

Contact: cblue.thailand@gmail.com, +66 (0)81 854 4291"""
    },
    "bas": {
        "keywords": ["bas", "building automation system", "ระบบบริหารอาคาร"],
        "content": """BAS (Building Automation System):
- Centralized building management
- Real-time monitoring
- Automated control systems
- Energy optimization
- Predictive maintenance
- Integrated building systems

Contact: cblue.thailand@gmail.com, +66 (0)81 854 4291"""
    },
    "smart_building": {
        "keywords": ["smart building", "intelligent building", "อาคารอัจฉริยะ", "สมาร์ทบิลดิ้ง"],
        "content": """Smart Building (อาคารอัจฉริยะ):
- Building Automation Systems (BAS)
- Real-time monitoring
- Predictive maintenance
- Energy efficiency
- Occupant comfort & security
- IoT integration
- Intelligent building management

Contact: cblue.thailand@gmail.com, +66 (0)81 854 4291"""
    },
    "environmental": {
        "keywords": ["environmental", "environment", "environmental service", "สิ่งแวดล้อม", "บริการสิ่งแวดล้อม"],
        "content": """Environmental Services

Sustainable practices for natural resource management and ecosystem protection.

Services:
• Natural resource management
• Ecosystem restoration
• Biodiversity protection
• Pollution reduction
• Sustainable practices
• Environmental consulting"""
    },
    "energy_saving": {
        "keywords": ["energy saving", "energy efficiency", "save energy", "ประหยัดพลังงาน", "ประหยัดไฟ"],
        "content": """Energy Saving

Solutions to reduce energy consumption and costs while maintaining performance.

Services:
• Energy efficiency solutions
• Cost reduction strategies
• Renewable energy integration
• Energy audits
• Sustainable energy practices
• Energy management systems"""
    },
    "cctv": {
        "keywords": ["cctv", "surveillance", "camera", "security camera", "กล้องวงจรปิด"],
        "content": """CCTV and Surveillance

Video monitoring systems using cameras to record and observe activities in real-time. CCTV provides visual evidence, deters crime, and enables remote monitoring of properties for security purposes."""
    },
    "motion_detector": {
        "keywords": ["motion detector", "motion sensor", "movement sensor", "เซ็นเซอร์ตรวจจับการเคลื่อนไหว"],
        "content": """Motion Detectors

Sensors that detect movement in protected areas, triggering alarms or notifications when unauthorized motion is detected. Used in security systems to alert of intrusions."""
    },
    "fire_alarm": {
        "keywords": ["fire alarm", "smoke detector", "fire detection", "alarm system", "สัญญาณเตือนไฟไหม้"],
        "content": """Fire Alarm Systems

Safety devices that detect smoke, heat, or flames and alert occupants to evacuate immediately. Fire alarms prevent injuries and property damage by providing early warning of fire hazards."""
    },
    "access_detection": {
        "keywords": ["unauthorized access", "access detection", "intrusion detection", "การตรวจจับการเข้าถึง"],
        "content": """Unauthorized Access Detection

Systems that identify and prevent entry by unauthorized persons using access control, sensors, and monitoring technologies. Protects restricted areas from intrusions."""
    },
    "realtime_monitoring": {
        "keywords": ["real-time monitoring", "real time monitoring", "realtime monitoring", "live monitoring", "24/7 monitoring", "การตรวจสอบแบบเรียลไทม์"],
        "content": """Real-Time Monitoring

Continuous surveillance with instant alerts, allowing immediate response to security events 24/7. Provides live visibility and rapid notification of any incidents."""
    },
    "emergency_response": {
        "keywords": ["emergency response", "emergency", "rapid response", "การตอบสนองฉุกเฉิน"],
        "content": """Emergency Response

Rapid reaction protocols connecting to authorities or security teams when threats are detected. Ensures quick action during security incidents or emergencies."""
    },
    "security": {
        "keywords": ["security", "security system", "ระบบรักษาความปลอดภัย", "ความปลอดภัย"],
        "content": """Security System

Comprehensive security solutions for home and business protection including CCTV, motion detectors, fire alarms, access control, and 24/7 monitoring."""
    },
    "access_control": {
        "keywords": ["access control", "access management", "ระบบควบคุมการเข้าถึง", "คอนโทรลเข้าออก"],
        "content": """Access Control (ระบบควบคุมการเข้าถึง):
- Building security
- Authorized access management
- Unauthorized entry prevention
- Tracking and monitoring
- Operational efficiency
- Secure access solutions
- Card access systems

Contact: cblue.thailand@gmail.com, +66 (0)81 854 4291"""
    },
    "fitout": {
        "keywords": ["fit out", "fit-out", "fitout", "what is fit out", "what is fit-out"],
        "content": """Fit Out

The process of making interior spaces ready for occupation by installing fixtures, furniture, equipment, and finishes. Fit out transforms empty spaces into functional environments.

Includes:
• Partitions and walls
• Flooring and ceilings
• Lighting systems
• HVAC installation
• Electrical systems
• Furniture and fixtures"""
    },
    "green_construction": {
        "keywords": ["green construction", "green contruction", "green building", "sustainable construction", "การก่อสร้างสีเขียว", "ก่อสร้างเขียว"],
        "content": """Green Construction

Sustainable building practices that minimize environmental impact through energy-efficient designs, renewable materials, and waste reduction. Creates healthier living environments while conserving resources.

Features:
• Energy-efficient designs
• Renewable and sustainable materials
• Waste minimization
• Environmental impact reduction
• Resource conservation

Services:
• Construction Management
• Project Management & Training
• Office buildings, hotels, housing complexes"""
    },
    "vertical_garden": {
        "keywords": ["vertical garden", "green wall", "living wall", "สวนแนวตั้ง"],
        "content": """Vertical Garden

Living walls or vertical gardens are plant installations on vertical surfaces. They improve air quality, reduce urban heat, provide insulation, and create aesthetic green spaces in limited areas."""
    },
    "smart_home": {
        "keywords": ["smart home", "home automation", "บ้านอัจฉริยะ", "สมาร์ทโฮม"],
        "content": """Smart Home (บ้านอัจฉริยะ):
- Home automation systems
- Remote control capabilities
- Energy efficiency
- Enhanced security
- Smart lighting & thermostat
- IoT home devices
- Connected home solutions

Contact: cblue.thailand@gmail.com, +66 (0)81 854 4291"""
    },
    "smart_farming": {
        "keywords": ["smart farming", "precision agriculture", "เกษตรอัจฉริยะ", "ฟาร์มอัจฉริยะ"],
        "content": """Smart Farming (เกษตรอัจฉริยะ):
- Precision agriculture
- IoT in agriculture
- Crop monitoring
- Irrigation management
- Soil management
- Data-driven farming
- Agricultural technology
- Sustainable farming

Contact: cblue.thailand@gmail.com, +66 (0)81 854 4291"""
    },
    "website_development": {
        "keywords": ["website", "web development", "web design", "พัฒนาเว็บไซต์", "ทำเว็บไซต์"],
        "content": """Website Development (พัฒนาเว็บไซต์):
- Web design & development
- Website maintenance
- Content management
- User-friendly websites
- Responsive design
- SEO optimization
- Web performance optimization

Contact: cblue.thailand@gmail.com, +66 (0)81 854 4291"""
    },
    "machine_learning": {
        "keywords": ["machine learning", "ml", "ai model", "deep learning", "neural network", "แมชชีนเลิร์นนิง", "เรียนรู้ของเครื่อง"],
        "content": """Machine Learning

AI field focused on algorithms that learn from data to recognize patterns and make predictions with minimal human intervention.

Services:
• ML model development & training
• Predictive analytics
• Computer vision & NLP
• Model deployment & optimization"""
    },
    "ai_chatbot": {
        "keywords": ["chatbot", "ai chatbot", "ai chat", "conversational ai", "chat bot", "แชทบอท", "บอทตอบคำถาม", "ai bot"],
        "content": """AI Chatbot Development

Intelligent conversational systems using AI, ML, and NLP for customer support, education, healthcare, and e-commerce.

Services:
• Custom chatbot development
• NLP engine integration
• Multi-language support (Thai, English, Chinese)
• Multi-channel deployment (Web, LINE, WhatsApp)"""
    },
    "software_development": {
        "keywords": ["software development", "software", "programming", "coding", "พัฒนาซอฟต์แวร์", "เขียนโปรแกรม"],
        "content": """Software Development

Systematic process of creating and maintaining software applications.

Services:
• Custom software development
• Web & mobile applications
• System architecture design
• API development & integration
• CI/CD pipeline implementation

Technologies: Python, Java, C++, JavaScript, Git, Docker, Kubernetes"""
    },
    "contact_phone": {
        "keywords": ["your phone number", "phone number", "contact number", "telephone", "เบอร์โทร", "หมายเลขโทรศัพท์"],
        "content": """Contact Phone Number

Phone: +66 (0)81 854 4291

Available for inquiries about our services including solar solutions, green architecture, smart building systems, AI chatbot development, and more."""
    },
    "contact_email": {
        "keywords": ["your email", "email address", "contact email", "อีเมล", "อีเมลติดต่อ"],
        "content": """Contact Email

Email: cblue.thailand@gmail.com

Send us your inquiries about our comprehensive services including construction, engineering, smart technology solutions, and AI development."""
    },
    "bms": {
        "keywords": ["bms", "building management system", "ระบบจัดการอาคาร"],
        "content": """BMS (Building Management System)

Centralized system that monitors and controls building operations including HVAC, lighting, security, and energy management.

Features:
• Real-time monitoring and control
• Energy optimization
• Automated system management
• Predictive maintenance
• Integrated building operations
• Cost reduction through efficiency

Contact: cblue.thailand@gmail.com, +66 (0)81 854 4291"""
    },
    "iot": {
        "keywords": ["iot", "internet of things", "connected devices", "smart devices", "อินเทอร์เน็ตของสรรพสิ่ง"],
        "content": """IoT (Internet of Things)

Network of interconnected devices that collect and exchange data to enable smart automation and monitoring.

Applications:
• Smart building systems
• Industrial automation
• Environmental monitoring
• Asset tracking
• Predictive maintenance
• Remote control and monitoring

Services:
• IoT system design and implementation
• Sensor integration
• Data analytics
• Cloud connectivity
• Mobile app development

Contact: cblue.thailand@gmail.com, +66 (0)81 854 4291"""
    },
    "chatbot_development": {
        "keywords": ["chatbot development", "bot development", "conversational ai development", "พัฒนาแชทบอท"],
        "content": """Chatbot Development

Professional development of intelligent conversational systems for businesses.

Services:
• Custom chatbot design and development
• Natural Language Processing (NLP) integration
• Multi-platform deployment (Web, LINE, WhatsApp, Facebook)
• Multi-language support (Thai, English, Chinese)
• AI training and optimization
• Integration with existing systems
• Maintenance and updates

Use Cases:
• Customer support automation
• Lead generation
• FAQ handling
• Appointment scheduling
• E-commerce assistance

Contact: cblue.thailand@gmail.com, +66 (0)81 854 4291"""
    },
    "ai_chatbot_development": {
        "keywords": ["ai chatbot development", "artificial intelligence chatbot", "intelligent bot development", "พัฒนาแชทบอท ai"],
        "content": """AI Chatbot Development

Advanced artificial intelligence-powered chatbot solutions using machine learning and natural language processing.

Features:
• Advanced AI and machine learning algorithms
• Natural Language Understanding (NLU)
• Context-aware conversations
• Sentiment analysis
• Continuous learning and improvement
• Integration with business systems
• Analytics and reporting

Technologies:
• Machine Learning frameworks
• NLP libraries
• Cloud AI services
• Custom AI models
• Deep learning algorithms

Contact: cblue.thailand@gmail.com, +66 (0)81 854 4291"""
    },
    "green_architect": {
        "keywords": ["green architect", "green architechture", "eco architect", "sustainable architect", "สถาปนิกสีเขียว"],
        "content": """Green Architecture

Eco-friendly buildings harmonizing with nature.

Services:
• Architectural, Interior, Landscape design
• Detailed engineering design
• Energy-efficient systems
• Sustainable materials
• Environmental design"""
    },
    "website_dev": {
        "keywords": ["website development", "web development", "web design", "website design", "พัฒนาเว็บไซต์", "ทำเว็บไซต์"],
        "content": """Website Development

Professional web development services for businesses and organizations.

Services:
• Custom website design and development
• Responsive web design
• E-commerce websites
• Content Management Systems (CMS)
• Web application development
• SEO optimization
• Website maintenance and support
• Performance optimization

Technologies:
• HTML5, CSS3, JavaScript
• React, Vue.js, Angular
• PHP, Python, Node.js
• WordPress, Drupal
• Database integration
• Cloud hosting solutions

Contact: cblue.thailand@gmail.com, +66 (0)81 854 4291"""
    },
    "who_are_you": {
        "keywords": ["who are you", "what is cblue", "about cblue", "cblue thailand", "คุณคือใคร", "cblue คือ"],
        "content": """Cblue Thailand offers a comprehensive suite of services focused on construction, engineering, and sustainable technology solutions."""
    }
}

def detect_language(text: str) -> str:
    """Detect language: th, zh, or en"""
    import re
    thai_chars = len(re.findall(r'[\u0E00-\u0E7F]', text))
    chinese_chars = len(re.findall(r'[\u4E00-\u9FFF]', text))
    total_chars = len(text.strip())
    
    if total_chars == 0:
        return 'en'
    
    if thai_chars / total_chars > 0.3:
        return 'th'
    elif chinese_chars / total_chars > 0.3:
        return 'zh'
    return 'en'

def extract_language_content(content: str, lang: str) -> str:
    """Extract content for specific language from multilingual content"""
    if '---' not in content:
        return content
    
    sections = content.split('---')
    
    if lang == 'en':
        return sections[0].strip()
    elif lang == 'th' and len(sections) > 1:
        return sections[1].strip()
    elif lang == 'zh' and len(sections) > 2:
        return sections[2].strip()
    
    return sections[0].strip()

def find_relevant_content(query: str) -> str:
    """Find relevant content using keyword matching with synonyms"""
    query_lower = query.lower()
    lang = detect_language(query)
    matches = []
    
    for topic, data in KNOWLEDGE_BASE.items():
        for keyword in data["keywords"]:
            if keyword.lower() in query_lower:
                content = extract_language_content(data["content"], lang)
                matches.append(content)
                break
    
    if matches:
        return "\n\n".join(matches)
    
    fallback = {
        'th': """Cblue Thailand ให้บริการ:
- โซลูชันพลังงานแสงอาทิตย์และเครื่องชาร์จ EV
- สถาปัตยกรรมสีเขียวและการก่อสร้างสีเขียว
- HVAC, MEP, Retrofit
- ระบบควบคุม, ระบบอัตโนมัติ, BAS และอาคารอัจฉริยะ
- บริการสิ่งแวดล้อมและประหยัดพลังงาน
- ระบบรักษาความปลอดภัยและควบคุมการเข้าถึง
- บ้านอัจฉริยะและเกษตรอัจฉริยะ
- พัฒนาเว็บไซต์
- พัฒนาแชทบอท AI
- พัฒนาซอฟต์แวร์
- Machine Learning

ติดต่อ: cblue.thailand@gmail.com, +66 (0)81 854 4291""",
        'zh': """Cblue Thailand 提供:
- 太阳能解决方案和电动汽车充电站
- 绿色建筑和绿色施工
- HVAC, MEP, 改造工程
- 控制系统、自动化、BAS和智能建筑
- 环境服务和节能
- 安全系统和门禁控制
- 智能家居和智能农业
- 网站开发
- AI聊天机器人开发
- 软件开发
- 机器学习

联系方式: cblue.thailand@gmail.com, +66 (0)81 854 4291""",
        'en': """Cblue Thailand provides:
- Solar Solutions & EV Chargers
- Green Architecture & Green Construction
- HVAC, MEP, Retrofit
- Controls, Automation, BAS & Smart Building
- Environmental Services & Energy Saving
- Security System & Access Control
- Smart Home & Smart Farming
- Website Development
- AI Chatbot Development
- Software Development
- Machine Learning

Contact: cblue.thailand@gmail.com, +66 (0)81 854 4291"""
    }
    
    return fallback.get(lang, fallback['en'])
