"""Knowledge base with semantic matching for Cblue services"""

KNOWLEDGE_BASE = {
    "ai_general": {
        "keywords": ["what is ai", "ai คือ", "ai คืออะไร", "ai是什么", "什么是ai", "什么是人工智能"],
        "content": """AI (Artificial Intelligence) is the simulation of human intelligence in machines that are programmed to think, reason, learn, and make decisions like humans.

---

AI (ปัญญาประดิษฐ์) คือการจำลองความฉลาดของมนุษย์ในเครื่องจักรที่ถูกโปรแกรมให้สามารถคิด วิเคราะห์ เรียนรู้ และตัดสินใจได้เหมือนมนุษย์

---

人工智能（AI）是指在机器中模拟人类智能的技术，使其能够像人类一样思考、推理、学习和做出决策。"""
    },
    "chatbot_definition": {
        "keywords": ["what is a chatbot", "what is chatbot", "chatbot คือ", "แชตบอทคือ", "แชตบอทคืออะไร", "什么是聊天机器人"],
        "content": """A chatbot is a software application that can converse with users through text or voice, often used to provide information or automate customer service tasks.

---

แชตบอทคือโปรแกรมซอฟต์แวร์ที่สามารถสนทนากับผู้ใช้งานผ่านข้อความหรือเสียง มักใช้เพื่อให้ข้อมูลหรือช่วยงานบริการลูกค้าแบบอัตโนมัติ

---

聊天机器人是一种软件应用程序，可以通过文字或语音与用户进行对话，通常用于提供信息或自动化客户服务任务。"""
    },
    "ai_chatbot_development": {
        "keywords": ["what is ai chatbot development", "ai chatbot development คือ", "การพัฒนาแชตบอท ai คืออะไร", "什么是ai聊天机器人开发"],
        "content": """AI chatbot development is the process of building chatbots that use artificial intelligence and natural language processing (NLP) to understand, learn from, and respond intelligently to user inputs.

---

การพัฒนาแชตบอท AI คือกระบวนการสร้างแชตบอทที่ใช้เทคโนโลยีปัญญาประดิษฐ์และการประมวลผลภาษาธรรมชาติ (NLP) เพื่อให้เข้าใจ เรียนรู้ และตอบสนองต่อผู้ใช้อย่างชาญฉลาด

---

AI聊天机器人开发是构建使用人工智能和自然语言处理（NLP）技术的聊天机器人的过程，使其能够理解、学习并智能地回应用户输入。"""
    },
    "chatbot_development": {
        "keywords": ["what is chatbot development", "chatbot development คือ", "การพัฒนาแชตบอทคืออะไร", "什么是聊天机器人开发"],
        "content": """Chatbot development is the creation of automated conversational programs that can interact with users through predefined rules, scripts, or AI-based understanding.

---

การพัฒนาแชตบอทคือการสร้างโปรแกรมสนทนาอัตโนมัติที่สามารถโต้ตอบกับผู้ใช้ได้ตามกฎที่ตั้งไว้ล่วงหน้า หรือโดยใช้ความเข้าใจจาก AI

---

聊天机器人开发是创建能通过预设规则、脚本或基于AI理解与用户互动的自动化对话程序的过程。"""
    },
    "software_definition": {
        "keywords": ["what is software", "software คือ", "ซอฟต์แวร์คือ", "ซอฟต์แวร์คืออะไร", "什么是软件"],
        "content": """Software is a set of instructions, programs, or data that tell a computer how to perform specific tasks or functions.

---

ซอฟต์แวร์คือชุดคำสั่ง โปรแกรม หรือข้อมูลที่บอกคอมพิวเตอร์ให้ทำงานหรือดำเนินการตามที่กำหนดไว้

---

软件是一组指令、程序或数据，用来告诉计算机如何执行特定任务或功能。"""
    },
    "software_development": {
        "keywords": ["what is software development", "software development คือ", "การพัฒนาซอฟต์แวร์คืออะไร", "พัฒนาซอฟต์แวร์คืออะไร", "什么是软件开发"],
        "content": """Software development is the process of designing, coding, testing, and maintaining applications, systems, or programs to meet user needs.

---

การพัฒนาซอฟต์แวร์คือกระบวนการออกแบบ เขียนโค้ด ทดสอบ และดูแลรักษาโปรแกรมหรือระบบ เพื่อให้ตอบสนองความต้องการของผู้ใช้งาน

---

软件开发是设计、编程、测试和维护应用程序、系统或程序的过程，以满足用户需求。"""
    },
    "machine_learning": {
        "keywords": ["what is machine learning", "machine learning คือ", "การเรียนรู้ของเครื่องคืออะไร", "แมชชีนเลิร์นนิงคืออะไร", "什么是机器学习"],
        "content": """Machine Learning (ML) is a branch of AI that enables computers to learn from data and improve their performance without being explicitly programmed.

---

การเรียนรู้ของเครื่อง (Machine Learning - ML) คือสาขาหนึ่งของ AI ที่ทำให้คอมพิวเตอร์สามารถเรียนรู้จากข้อมูลและปรับปรุงประสิทธิภาพได้โดยไม่ต้องเขียนโปรแกรมใหม่ทั้งหมด

---

机器学习（ML）是人工智能的一个分支，使计算机能够从数据中学习并不断提高性能，而无需明确编程。"""
    },
    "ml_definition": {
        "keywords": ["what is ml", "ml คือ", "ml คืออะไร", "什么是ml"],
        "content": """ML stands for Machine Learning — a field of AI that allows computers to automatically learn patterns and make predictions from data.

---

ML คือคำย่อของ Machine Learning ซึ่งเป็นเทคโนโลยี AI ที่ช่วยให้คอมพิวเตอร์เรียนรู้รูปแบบข้อมูลและสามารถคาดการณ์หรือวิเคราะห์ได้โดยอัตโนมัติ

---

ML是机器学习（Machine Learning）的缩写，是人工智能的一个领域，使计算机能够自动学习数据模式并进行预测。"""
    },
    "machine_definition": {
        "keywords": ["what is a machine", "machine คือ", "เครื่องจักรคือ", "เครื่องจักรคืออะไร", "什么是机器"],
        "content": """A machine is a device or system that performs work or processes tasks using mechanical, electrical, or computational power.

---

เครื่องจักรคืออุปกรณ์หรือระบบที่ทำงานหรือประมวลผลโดยใช้พลังงานกล ไฟฟ้า หรือการคำนวณ

---

机器是使用机械、电气或计算能力来执行工作或处理任务的装置或系统。"""
    },
    "learning_definition": {
        "keywords": ["what is learning", "learning คือ", "การเรียนรู้คือ", "การเรียนรู้คืออะไร", "什么是学习"],
        "content": """Learning is the process of acquiring knowledge, understanding, or skills through study, experience, or teaching.

---

การเรียนรู้คือกระบวนการได้รับความรู้ ความเข้าใจ หรือทักษะ ผ่านการศึกษา ประสบการณ์ หรือการฝึกสอน

---

学习是通过学习、经验或教学获得知识、理解或技能的过程。"""
    },
    "artificial_intelligence": {
        "keywords": ["what is artificial intelligence", "artificial intelligence คือ", "ปัญญาประดิษฐ์คืออะไร", "ปัญญาประดิษฐ์คือ", "什么是人工智能"],
        "content": """Artificial intelligence is the ability of machines or computers to perform tasks that normally require human intelligence, such as reasoning, perception, and problem-solving.

---

ปัญญาประดิษฐ์คือความสามารถของเครื่องจักรหรือคอมพิวเตอร์ในการทำงานที่ต้องใช้ความฉลาดของมนุษย์ เช่น การให้เหตุผล การรับรู้ และการแก้ปัญหา

---

人工智能是机器或计算机执行通常需要人类智能的任务的能力，例如推理、感知和解决问题。"""
    },
    "computer_definition": {
        "keywords": ["what is computers", "what are computers", "คอมพิวเตอร์คือ", "คอมพิวเตอร์คืออะไร", "什么是计算机"],
        "content": """Computers are electronic devices that process data using instructions (software) to perform calculations, store information, and execute tasks.

---

คอมพิวเตอร์คืออุปกรณ์อิเล็กทรอนิกส์ที่ประมวลผลข้อมูลตามคำสั่ง (ซอฟต์แวร์) เพื่อคำนวณ จัดเก็บข้อมูล และดำเนินการต่าง ๆ

---

计算机是一种电子设备，通过执行指令（软件）来处理数据、进行计算、存储信息并执行任务。"""
    },
    "data_definition": {
        "keywords": ["what is data", "data คือ", "ข้อมูลคือ", "ข้อมูลคืออะไร", "什么是数据"],
        "content": """Data is information in raw or structured form, such as numbers, text, or images, that can be processed or analyzed by computers.

---

ข้อมูลคือข้อเท็จจริงหรือสารสนเทศในรูปแบบดิบหรือโครงสร้าง เช่น ตัวเลข ข้อความ หรือภาพ ที่สามารถนำไปประมวลผลหรือวิเคราะห์ได้

---

数据是以原始或结构化形式存在的信息，如数字、文本或图像，计算机可以处理或分析这些信息。"""
    },
    "solar": {
        "keywords": ["what is solar", "solar คือ", "พลังงานแสงอาทิตย์คืออะไร", "พลังงานจากแสงอาทิตย์คืออะไร", "พลังงานจากดวงอาทิตย์คืออะไร", "什么是太阳能"],
        "content": """Solar refers to energy derived from the sun's radiation, which can be converted into electricity or heat.

---

พลังงานแสงอาทิตย์หมายถึงพลังงานที่ได้จากรังสีของดวงอาทิตย์ ซึ่งสามารถเปลี่ยนเป็นพลังงานไฟฟ้าหรือความร้อนได้

---

太阳能指来自太阳辐射的能量，可以转化为电能或热能。"""
    },
    "solar_solutions": {
        "keywords": ["what is solar solutions", "solar solutions คือ", "โซลูชันพลังงานแสงอาทิตย์คืออะไร", "什么是太阳能解决方案"],
        "content": """Solar Solutions are systems or services that use solar energy technologies (like solar panels or solar water heaters) to provide renewable power or heating.

---

โซลูชันพลังงานแสงอาทิตย์หมายถึงระบบหรือบริการที่ใช้เทคโนโลยีพลังงานแสงอาทิตย์ (เช่น แผงโซลาร์เซลล์ หรือเครื่องทำน้ำร้อนพลังงานแสงอาทิตย์) เพื่อผลิตพลังงานหมุนเวียนหรือให้ความร้อน

---

太阳能解决方案是利用太阳能技术（如太阳能电池板或太阳能热水器）来提供可再生能源或供热的系统或服务。"""
    },
    "technologies": {
        "keywords": ["what is technologies", "what are technologies", "เทคโนโลยีคือ", "เทคโนโลยีคืออะไร", "什么是技术"],
        "content": """Technologies are tools, systems, or methods developed using scientific knowledge to solve problems or improve human life.

---

เทคโนโลยีคือเครื่องมือ ระบบ หรือวิธีการที่ถูกพัฒนาด้วยความรู้ทางวิทยาศาสตร์ เพื่อแก้ปัญหาหรือพัฒนาคุณภาพชีวิตมนุษย์

---

技术是利用科学知识开发的工具、系统或方法，用于解决问题或改善人类生活。"""
    },
    "ev": {
        "keywords": ["what is ev", "ev คือ", "ev คืออะไร", "什么是ev"],
        "content": """EV stands for Electric Vehicle — a vehicle powered by electricity stored in batteries instead of fossil fuels.

---

EV ย่อมาจาก Electric Vehicle หมายถึงยานพาหนะที่ขับเคลื่อนด้วยพลังงานไฟฟ้าที่เก็บในแบตเตอรี่แทนน้ำมันเชื้อเพลิง

---

EV是电动汽车（Electric Vehicle）的缩写，指使用储存在电池中的电能而非化石燃料驱动的车辆。"""
    },
    "ev_charger": {
        "keywords": ["what is ev charger", "ev charger คือ", "เครื่องชาร์จรถยนต์ไฟฟ้าคืออะไร", "เครื่องชาร์จไฟฟ้าคืออะไร", "ที่ชาร์จรถยนต์ไฟฟ้าคืออะไร", "什么是ev充电器"],
        "content": """An EV charger is a device that supplies electric energy to recharge the battery of an electric vehicle.

---

เครื่องชาร์จรถยนต์ไฟฟ้าคืออุปกรณ์ที่จ่ายพลังงานไฟฟ้าเพื่อชาร์จแบตเตอรี่ของรถยนต์ไฟฟ้า

---

电动汽车充电器是一种为电动车电池充电的设备。"""
    },
    "wifi_definition": {
        "keywords": ["what is wifi", "what is wi-fi", "wifi คือ", "wi-fi คืออะไร", "什么是wifi"],
        "content": """Wi-Fi is a wireless networking technology that allows devices to connect to the internet or communicate without physical cables.

---

Wi-Fi คือเทคโนโลยีเครือข่ายไร้สายที่ช่วยให้อุปกรณ์เชื่อมต่ออินเทอร์เน็ตหรือสื่อสารกันได้โดยไม่ต้องใช้สายเคเบิล

---

Wi-Fi是一种无线网络技术，允许设备在不使用物理电缆的情况下连接到互联网或进行通信。"""
    },
    "green_architecture": {
        "keywords": ["what is green architecture", "green architecture คือ", "สถาปัตยกรรมสีเขียวคืออะไร", "สถาปัตยกรรมเขียวคืออะไร", "什么是绿色建筑"],
        "content": """Green Architecture is an environmentally conscious design approach that reduces energy use, minimizes waste, and promotes sustainability in building construction.

---

สถาปัตยกรรมสีเขียวคือแนวคิดการออกแบบอาคารที่คำนึงถึงสิ่งแวดล้อม เน้นการประหยัดพลังงาน ลดของเสีย และสร้างความยั่งยืน

---

绿色建筑是一种注重环境保护的设计方法，旨在减少能源消耗、减少浪费并促进建筑可持续性。"""
    },
    "ecofriendly_definition": {
        "keywords": ["what is eco-friendly", "what is eco friendly", "what is ecofriendly", "eco-friendly คือ", "eco friendly คือ", "เป็นมิตรต่อสิ่งแวดล้อมหมายถึงอะไร", "มิตรต่อสิ่งแวดล้อมคืออะไร", "เป็นมิตรกับสิ่งแวดล้อมคืออะไร", "什么是环保"],
        "content": """Eco-friendly refers to products, practices, or systems that cause minimal harm to the environment.

---

เป็นมิตรต่อสิ่งแวดล้อมหมายถึงผลิตภัณฑ์หรือวิธีการที่ส่งผลกระทบต่อสิ่งแวดล้อมน้อยที่สุด

---

环保是指对环境危害最小的产品、做法或系统。"""
    },
    "hvac": {
        "keywords": ["what is hvac", "hvac คือ", "hvac คืออะไร", "什么是hvac"],
        "content": """HVAC stands for Heating, Ventilation, and Air Conditioning — systems used to regulate indoor climate and air quality.

---

HVAC ย่อมาจาก Heating, Ventilation, and Air Conditioning คือระบบที่ควบคุมอุณหภูมิ การระบายอากาศ และคุณภาพอากาศภายในอาคาร

---

HVAC是供暖（Heating）、通风（Ventilation）和空调（Air Conditioning）的缩写，用于调节室内气候和空气质量的系统。"""
    },
    "mep": {
        "keywords": ["what is mep", "mep คือ", "mep คืออะไร", "什么是mep"],
        "content": """MEP stands for Mechanical, Electrical, and Plumbing — the essential engineering systems integrated into building design and construction.

---

MEP ย่อมาจาก Mechanical, Electrical, and Plumbing คือระบบวิศวกรรมสำคัญที่ใช้ในการออกแบบและก่อสร้างอาคาร

---

MEP代表机械（Mechanical）、电气（Electrical）和管道（Plumbing）工程，是建筑设计和施工中不可或缺的系统。"""
    },
    "retrofit": {
        "keywords": ["what is retrofit", "retrofit คือ", "การปรับปรุงระบบ (retrofit) คืออะไร", "什么是改造"],
        "content": """Retrofit means upgrading or modifying existing buildings or systems to improve energy efficiency, performance, or sustainability.

---

การปรับปรุงระบบ (Retrofit) หมายถึงการอัปเกรดหรือปรับเปลี่ยนสิ่งปลูกสร้างหรือระบบเดิมให้มีประสิทธิภาพและประหยัดพลังงานมากขึ้น

---

改造是指升级或修改现有建筑或系统，以提高能源效率、性能或可持续性。"""
    },
    "controls": {
        "keywords": ["what is controls", "what are controls", "controls คือ", "ระบบควบคุมคืออะไร", "什么是控制系统"],
        "content": """Controls refer to systems or devices that manage and regulate equipment operations, such as temperature, lighting, or security systems.

---

ระบบควบคุมหมายถึงอุปกรณ์หรือระบบที่ใช้ในการจัดการและควบคุมการทำงานของอุปกรณ์ เช่น ระบบไฟฟ้า อุณหภูมิ หรือระบบรักษาความปลอดภัย

---

控制系统是用于管理和调节设备运行（如温度、照明或安全系统）的系统或装置。"""
    },
    "automation": {
        "keywords": ["what is automation", "automation คือ", "ระบบอัตโนมัติคืออะไร", "อัตโนมัติคืออะไร", "什么是自动化"],
        "content": """Automation is the use of technology to perform tasks automatically without human intervention.

---

ระบบอัตโนมัติหมายถึงการใช้เทคโนโลยีเพื่อให้เครื่องจักรหรือระบบทำงานได้โดยไม่ต้องมีการควบคุมจากมนุษย์

---

自动化是利用技术以最少的人工干预执行任务的过程。"""
    },
    "bas": {
        "keywords": ["what is bas", "bas คือ", "bas คืออะไร", "什么是bas"],
        "content": """BAS stands for Building Automation System — a centralized system that monitors and controls building functions like HVAC, lighting, and security.

---

BAS ย่อมาจาก Building Automation System คือระบบควบคุมส่วนกลางที่ใช้ในการตรวจสอบและจัดการการทำงานต่าง ๆ ของอาคาร เช่น HVAC แสงสว่าง และระบบความปลอดภัย

---

BAS是楼宇自动化系统（Building Automation System）的缩写，是一个集中控制HVAC、照明和安全等建筑功能的系统。"""
    },
    "smart_building": {
        "keywords": ["what is smart building", "smart building คือ", "อาคารอัจฉริยะคืออะไร", "อาคารสมาร์ทคืออะไร", "什么是智慧建筑"],
        "content": """A Smart Building uses technology and sensors to automatically control and optimize operations such as lighting, temperature, and energy use for efficiency and comfort.

---

อาคารอัจฉริยะคืออาคารที่ใช้เทคโนโลยีและเซนเซอร์เพื่อควบคุมและเพิ่มประสิทธิภาพการทำงาน เช่น ระบบไฟฟ้า อุณหภูมิ และการใช้พลังงาน

---

智慧建筑利用技术和传感器自动控制与优化照明、温度和能源使用等操作，以提高效率和舒适度。"""
    },
    "realtime_monitoring": {
        "keywords": ["what is real-time monitoring", "what is real time monitoring", "what is realtime monitoring", "real-time monitoring คือ", "real time monitoring คือ", "การตรวจสอบแบบเรียลไทม์คืออะไร", "การตรวจสอบเรียลไทม์คืออะไร", "什么是实时监控"],
        "content": """Real-time monitoring is the continuous observation and tracking of systems or data as events happen, allowing immediate response or adjustments.

---

การตรวจสอบแบบเรียลไทม์คือการติดตามและเฝ้าดูระบบหรือข้อมูลแบบต่อเนื่องในขณะที่เหตุการณ์กำลังเกิดขึ้น เพื่อให้สามารถตอบสนองหรือปรับเปลี่ยนได้ทันที

---

实时监控是对系统或数据进行持续观察和跟踪的过程，以便在事件发生时立即响应或调整。"""
    },
    "predictive_maintenance": {
        "keywords": ["what is predictive maintenance", "predictive maintenance คือ", "การบำรุงรักษาเชิงคาดการณ์คืออะไร", "什么是预测性维护"],
        "content": """Predictive maintenance uses data and AI to predict when equipment will fail, allowing maintenance before a breakdown occurs.

---

การบำรุงรักษาเชิงคาดการณ์คือการใช้ข้อมูลและ AI เพื่อทำนายการเสียของอุปกรณ์ และซ่อมแซมก่อนที่ความเสียหายจะเกิดขึ้นจริง

---

预测性维护利用数据和人工智能预测设备故障的时间，从而在设备损坏前进行维护。"""
    },
    "occupant_comfort": {
        "keywords": ["what is occupant comfort", "occupant comfort คือ", "ความสบายของผู้ใช้อาคารคืออะไร", "什么是居住者舒适度"],
        "content": """Occupant comfort refers to the physical and psychological well-being of people inside a building, influenced by factors like temperature, lighting, and air quality.

---

ความสบายของผู้ใช้อาคารหมายถึงความเป็นอยู่ที่ดีทั้งทางกายภาพและจิตใจของผู้อยู่อาศัย เช่น อุณหภูมิ แสง และคุณภาพอากาศ

---

居住者舒适度指建筑内部人员的身心舒适度，受温度、照明和空气质量等因素影响。"""
    },
    "environmental_services": {
        "keywords": ["what is environmental services", "what are environmental services", "environmental services คือ", "บริการด้านสิ่งแวดล้อมคืออะไร", "什么是环境服务"],
        "content": """Environmental services involve managing and protecting natural resources through waste management, pollution control, and sustainability programs.

---

บริการด้านสิ่งแวดล้อมคือการจัดการและปกป้องทรัพยากรธรรมชาติ เช่น การจัดการของเสีย การควบคุมมลพิษ และการพัฒนาอย่างยั่งยืน

---

环境服务包括通过废物管理、污染控制和可持续发展计划来管理和保护自然资源。"""
    },
    "energy_saving": {
        "keywords": ["what is energy saving", "energy saving คือ", "การประหยัดพลังงานคืออะไร", "ประหยัดพลังงานคืออะไร", "什么是节能"],
        "content": """Energy saving means reducing energy use through efficient technologies, behavior, or design, to lower costs and environmental impact.

---

การประหยัดพลังงานหมายถึงการลดการใช้พลังงานผ่านเทคโนโลยีที่มีประสิทธิภาพ พฤติกรรมที่เหมาะสม หรือการออกแบบที่ดี

---

节能是通过高效技术、行为或设计减少能源使用，从而降低成本和环境影响。"""
    },
    "environmental_footprints": {
        "keywords": ["what is environmental footprints", "what are environmental footprints", "environmental footprints คือ", "รอยเท้าสิ่งแวดล้อมคืออะไร", "什么是环境足迹"],
        "content": """Environmental footprints measure the total impact of human activities on the environment, including energy use, emissions, and resource consumption.

---

รอยเท้าสิ่งแวดล้อมหมายถึงผลกระทบทั้งหมดที่กิจกรรมของมนุษย์มีต่อสิ่งแวดล้อม เช่น การใช้พลังงาน การปล่อยคาร์บอน และการใช้ทรัพยากร

---

环境足迹衡量人类活动对环境的总影响，包括能源使用、排放和资源消耗。"""
    },
    "security_system": {
        "keywords": ["what is security system", "security system คือ", "ระบบรักษาความปลอดภัยคืออะไร", "ระบบความปลอดภัยคืออะไร", "什么是安防系统"],
        "content": """A security system is a set of devices and software designed to protect buildings or data from unauthorized access, theft, or harm.

---

ระบบรักษาความปลอดภัยคือชุดอุปกรณ์และซอฟต์แวร์ที่ออกแบบมาเพื่อป้องกันอาคารหรือข้อมูลจากการเข้าถึงโดยไม่ได้รับอนุญาตหรือการโจรกรรม

---

安防系统是一组设备和软件，用于保护建筑或数据免受未经授权的访问、盗窃或破坏。"""
    },
    "access_control": {
        "keywords": ["what is access control", "access control คือ", "การควบคุมการเข้าถึงคืออะไร", "ควบคุมการเข้าถึงคืออะไร", "什么是门禁控制"],
        "content": """Access control is a security process that restricts or grants entry to specific areas, systems, or information based on authorization.

---

การควบคุมการเข้าถึงคือกระบวนการรักษาความปลอดภัยที่จำกัดหรืออนุญาตให้บุคคลเข้าถึงพื้นที่หรือข้อมูลตามสิทธิ์ที่กำหนด

---

门禁控制是一种安全管理过程，根据授权限制或允许进入特定区域、系统或信息。"""
    },
    "green_construction": {
        "keywords": ["what is green construction", "green construction คือ", "การก่อสร้างสีเขียวคืออะไร", "การก่อสร้างเขียวคืออะไร", "什么是绿色施工"],
        "content": """Green construction involves building practices that are sustainable, energy-efficient, and environmentally responsible.

---

การก่อสร้างสีเขียวคือแนวทางการก่อสร้างที่ยั่งยืน มีประสิทธิภาพด้านพลังงาน และเป็นมิตรต่อสิ่งแวดล้อม

---

绿色施工是指可持续、节能且对环境负责的建筑实践。"""
    },
    "fitout": {
        "keywords": ["what is fit out", "what is fitout", "what is fit-out", "fit out คือ", "fit-out คือ", "งานตกแต่งภายในคืออะไร", "什么是室内装修"],
        "content": """Fit Out refers to the process of furnishing and equipping interior spaces to make them functional and ready for use.

---

งานตกแต่งภายใน (Fit Out) หมายถึงกระบวนการตกแต่งและติดตั้งอุปกรณ์ภายในอาคารให้พร้อมใช้งาน

---

室内装修是为使空间具备功能性并可投入使用而进行的布置与设备安装过程。"""
    },
    "renovation": {
        "keywords": ["what is renovation", "renovation คือ", "การปรับปรุงหรือรีโนเวทคืออะไร", "รีโนเวทคืออะไร", "การรีโนเวทคืออะไร", "什么是翻新"],
        "content": """Renovation means restoring, repairing, or upgrading existing buildings to improve functionality or appearance.

---

การปรับปรุงหรือรีโนเวทคือการซ่อมแซมหรือปรับปรุงอาคารเดิมให้ดีขึ้นทั้งในด้านรูปลักษณ์และการใช้งาน

---

翻新是修复、改进或升级现有建筑的过程，以提升功能或外观。"""
    },
    "reinstatement": {
        "keywords": ["what is reinstatement", "reinstatement คือ", "การคืนสภาพคืออะไร", "什么是恢复原状"],
        "content": """Reinstatement is the process of returning a property to its original condition, often after a lease ends or construction work is completed.

---

การคืนสภาพคือการนำทรัพย์สินหรืออาคารกลับคืนสู่สภาพเดิม มักทำหลังจากหมดสัญญาเช่าหรือหลังงานก่อสร้างเสร็จสิ้น

---

恢复原状是将物业恢复至原始状态的过程，通常发生在租约结束或施工完成后。"""
    },
    "vertical_garden": {
        "keywords": ["what is vertical garden", "vertical garden คือ", "สวนแนวตั้งคืออะไร", "什么是垂直花园"],
        "content": """A Vertical Garden is a structure where plants grow on vertically suspended panels, used for aesthetics, insulation, and air purification.

---

สวนแนวตั้งคือโครงสร้างที่ปลูกต้นไม้ในแนวตั้ง เพื่อความสวยงาม ฉนวนกันความร้อน และช่วยฟอกอากาศ

---

垂直花园是一种植物在垂直悬挂面板上生长的结构，用于美化、隔热和净化空气。"""
    },
    "smart_home": {
        "keywords": ["what is smart home", "smart home คือ", "บ้านอัจฉริยะคืออะไร", "บ้านสมาร์ทคืออะไร", "什么是智能家居"],
        "content": """A Smart Home uses interconnected devices and automation systems to control lighting, temperature, appliances, and security remotely.

---

บ้านอัจฉริยะคือบ้านที่ใช้เทคโนโลยีและระบบอัตโนมัติในการควบคุมไฟฟ้า อุณหภูมิ เครื่องใช้ไฟฟ้า และระบบรักษาความปลอดภัยได้จากระยะไกล

---

智能家居通过互联设备和自动化系统远程控制照明、温度、电器和安防系统。"""
    },
    "smart_farming": {
        "keywords": ["what is smart farming", "smart farming คือ", "เกษตรอัจฉริยะคืออะไร", "เกษตรสมาร์ทคืออะไร", "การเกษตรอัจฉริยะคืออะไร", "什么是智慧农业"],
        "content": """Smart farming uses IoT, sensors, and AI technologies to optimize agricultural production, reduce waste, and improve efficiency.

---

เกษตรอัจฉริยะคือการใช้เทคโนโลยี IoT เซนเซอร์ และ AI เพื่อเพิ่มประสิทธิภาพการผลิต ลดของเสีย และเพิ่มผลผลิตทางการเกษตร

---

智慧农业利用物联网（IoT）、传感器和人工智能技术优化农业生产、减少浪费并提高效率。"""
    },
    "website": {
        "keywords": ["what is a website", "website คือ", "เว็บไซต์คืออะไร", "什么是网站"],
        "content": """A website is a collection of web pages accessible via the internet, typically under a single domain name.

---

เว็บไซต์คือชุดของหน้าเว็บที่สามารถเข้าถึงได้ผ่านอินเทอร์เน็ต ภายใต้ชื่อโดเมนเดียวกัน

---

网站是一组网页的集合，可通过互联网访问，通常位于同一个域名下。"""
    },
    "website_development": {
        "keywords": ["what is website development", "website development คือ", "การพัฒนาเว็บไซต์คืออะไร", "พัฒนาเว็บไซต์คืออะไร", "什么是网站开发"],
        "content": """Website development is the process of designing, coding, and maintaining websites to ensure functionality, accessibility, and performance.

---

การพัฒนาเว็บไซต์คือกระบวนการออกแบบ เขียนโค้ด และดูแลเว็บไซต์ให้สามารถทำงานได้อย่างมีประสิทธิภาพและเข้าถึงได้ง่าย

---

网站开发是设计、编程和维护网站的过程，以确保其功能性、可访问性和性能。"""
    },
    "seo_definition": {
        "keywords": ["what is seo", "seo คือ", "seo คืออะไร", "什么是seo"],
        "content": """SEO (Search Engine Optimization) is the practice of improving a website's visibility in search engine results to attract more organic traffic.

---

SEO (Search Engine Optimization) คือการปรับปรุงเว็บไซต์ให้ติดอันดับสูงในการค้นหาผ่านเสิร์ชเอนจิน เพื่อเพิ่มจำนวนผู้เข้าชมแบบธรรมชาติ

---

SEO（搜索引擎优化）是提高网站在搜索引擎结果中可见度的实践，以吸引更多自然流量。"""
    },
    "coding_definition": {
        "keywords": ["what is coding", "coding คือ", "การเขียนโค้ดคืออะไร", "什么是编程"],
        "content": """Coding is the process of writing instructions in a programming language to create software, applications, or websites.

---

การเขียนโค้ดคือกระบวนการเขียนคำสั่งด้วยภาษาคอมพิวเตอร์เพื่อสร้างซอฟต์แวร์ แอปพลิเคชัน หรือเว็บไซต์

---

编程是用编程语言编写指令的过程，用于创建软件、应用程序或网站。"""
    },
    "contact_phone": {
        "keywords": ["what is your phone number", "your phone number", "phone number", "เบอร์โทร", "หมายเลขโทรศัพท์ของคุณคืออะไร", "เบอร์โทรศัพท์คืออะไร", "เบอร์ติดต่อ", "你的电话号码"],
        "content": """You can contact us at +66 (0)81 854 4291

---

คุณสามารถติดต่อฉันได้ที่ +66 (0)81 854 4291

---

您可以拨打 +66 (0)81 854 4291 联系我们。"""
    },
    "contact_email": {
        "keywords": ["what is your email", "your email", "email address", "อีเมล", "อีเมลของคุณคืออะไร", "อีเมลคืออะไร", "อีเมลติดต่อ", "你的电子邮件"],
        "content": """You can email me through cblue.thailand@gmail.com

---

คุณสามารถส่งอีเมลถึงฉันได้ที่ cblue.thailand@gmail.com

---

您可以通过 cblue.thailand@gmail.com 给我发送电子邮件。"""
    },
    "green_architecture_alt1": {
        "keywords": ["สถาปัตยกรรมที่เป็นมิตรต่อสิ่งแวดล้อมคืออะไร", "สถาปัตยกรรมที่เป็นมิตรต่อสิ่งแวดล้อม", "อะไรคือสถาปัตยกรรมที่เป็นมิตรต่อสิ่งแวดล้อม"],
        "content": """Green Architecture is an environmentally conscious design approach that reduces energy use, minimizes waste, and promotes sustainability in building construction.

---

สถาปัตยกรรมสีเขียวคือแนวคิดการออกแบบอาคารที่คำนึงถึงสิ่งแวดล้อม เน้นการประหยัดพลังงาน ลดของเสีย และสร้างความยั่งยืน

---

绿色建筑是一种注重环境保护的设计方法，旨在减少能源消耗、减少浪费并促进建筑可持续性。"""
    },
    "eco_friendly_construction": {
        "keywords": ["การก่อสร้างที่เป็นมิตรต่อสิ่งแวดล้อมคืออะไร", "ก่อสร้างที่เป็นมิตรต่อสิ่งแวดล้อมคืออะไร", "การก่อสร้างสีเขียวคืออะไร", "ก่อสร้างสีเขียวคืออะไร", "การก่อสร้างเขียวคืออะไร", "ก่อสร้างเขียวคืออะไร", "อะไรคือการก่อสร้างที่เป็นมิตรต่อสิ่งแวดล้อม", "อะไรคือก่อสร้างที่เป็นมิตรต่อสิ่งแวดล้อม", "อะไรคือการก่อสร้างสีเขียว", "อะไรคือก่อสร้างสีเขียว", "อะไรคือการก่อสร้างเขียว", "อะไรคือก่อสร้างเขียว", "เป็นมิตรต่อสิ่งแวดล้อมหมายถึง", "อะไรคือเป็นมิตรต่อสิ่งแวดล้อมหมายถึง"],
        "content": """Eco-friendly refers to products or practices that cause minimal harm to the environment.

---

เป็นมิตรต่อสิ่งแวดล้อมหมายถึงผลิตภัณฑ์หรือวิธีการที่ส่งผลกระทบต่อสิ่งแวดล้อมน้อยที่สุด

---

环保是指对环境危害最小的产品、做法或系统。"""
    },
    "ai_variations_th": {
        "keywords": ["ปัญญาประดิษฐ์คืออะไร", "เอไอคืออะไร", "อะไรคือปัญญาประดิษฐ์", "อะไรคือเอไอ", "ปัญญาประดิษฐ์", "เอไอ"],
        "content": """AI (Artificial Intelligence) is the simulation of human intelligence in machines that are programmed to think, reason, learn, and make decisions like humans.

---

ปัญญาประดิษฐ์ คือการจำลองความฉลาดของมนุษย์ในเครื่องจักรที่ถูกโปรแกรมให้สามารถคิด วิเคราะห์ เรียนรู้ และตัดสินใจได้เหมือนมนุษย์

---

人工智能（AI）是指在机器中模拟人类智能的技术，使其能够像人类一样思考、推理、学习和做出决策。"""
    },
    "chatbot_variations_th": {
        "keywords": ["แชตบอท", "อะไรคือแชตบอท"],
        "content": """A chatbot is a software application that can converse with users through text or voice, often used to provide information or automate customer service tasks.

---

แชตบอทคือโปรแกรมซอฟต์แวร์ที่สามารถสนทนากับผู้ใช้งานผ่านข้อความหรือเสียง มักใช้เพื่อให้ข้อมูลหรือช่วยงานบริการลูกค้าแบบอัตโนมัติ

---

聊天机器人是一种软件应用程序，可以通过文字或语音与用户进行对话，通常用于提供信息或自动化客户服务任务。"""
    },
    "ai_chatbot_dev_variations_th": {
        "keywords": ["การพัฒนาแชตบอท AI", "อะไรคือการพัฒนาแชตบอท AI"],
        "content": """AI chatbot development is the process of building chatbots that use artificial intelligence and natural language processing (NLP) to understand, learn from, and respond intelligently to user inputs.

---

การพัฒนาแชตบอท AI คือกระบวนการสร้างแชตบอทที่ใช้เทคโนโลยีปัญญาประดิษฐ์และการประมวลผลภาษาธรรมชาติ (NLP) เพื่อให้เข้าใจ เรียนรู้ และตอบสนองต่อผู้ใช้อย่างชาญฉลาด

---

AI聊天机器人开发是构建使用人工智能和自然语言处理（NLP）技术的聊天机器人的过程，使其能够理解、学习并智能地回应用户输入。"""
    },
    "chatbot_dev_variations_th": {
        "keywords": ["การพัฒนาแชตบอท", "อะไรคือการพัฒนาแชตบอท"],
        "content": """Chatbot development is the creation of automated conversational programs that can interact with users through predefined rules, scripts, or AI-based understanding.

---

การพัฒนาแชตบอทคือการสร้างโปรแกรมสนทนาอัตโนมัติที่สามารถโต้ตอบกับผู้ใช้ได้ตามกฎที่ตั้งไว้ล่วงหน้า หรือโดยใช้ความเข้าใจจาก AI

---

聊天机器人开发是创建能通过预设规则、脚本或基于AI理解与用户互动的自动化对话程序的过程。"""
    },
    "software_variations_th": {
        "keywords": ["ซอฟต์แวร์", "อะไรคือซอฟต์แวร์"],
        "content": """Software is a set of instructions, programs, or data that tell a computer how to perform specific tasks or functions.

---

ซอฟต์แวร์คือชุดคำสั่ง โปรแกรม หรือข้อมูลที่บอกคอมพิวเตอร์ให้ทำงานหรือดำเนินการตามที่กำหนดไว้

---

软件是一组指令、程序或数据，用来告诉计算机如何执行特定任务或功能。"""
    },
    "software_dev_variations_th": {
        "keywords": ["การพัฒนาซอฟต์แวร์", "อะไรคือการพัฒนาซอฟต์แวร์"],
        "content": """Software development is the process of designing, coding, testing, and maintaining applications, systems, or programs to meet user needs.

---

การพัฒนาซอฟต์แวร์คือกระบวนการออกแบบ เขียนโค้ด ทดสอบ และดูแลรักษาโปรแกรมหรือระบบ เพื่อให้ตอบสนองความต้องการของผู้ใช้งาน

---

软件开发是设计、编程、测试和维护应用程序、系统或程序的过程，以满足用户需求。"""
    },
    "machine_learning_variations_th": {
        "keywords": ["การเรียนรู้ของเครื่อง", "อะไรคือการเรียนรู้ของเครื่อง"],
        "content": """Machine Learning (ML) is a branch of AI that enables computers to learn from data and improve their performance without being explicitly programmed.

---

การเรียนรู้ของเครื่อง (Machine Learning - ML) คือสาขาหนึ่งของ AI ที่ทำให้คอมพิวเตอร์สามารถเรียนรู้จากข้อมูลและปรับปรุงประสิทธิภาพได้โดยไม่ต้องเขียนโปรแกรมใหม่ทั้งหมด

---

机器学习（ML）是人工智能的一个分支，使计算机能够从数据中学习并不断提高性能，而无需明确编程。"""
    },
    "ml_variations_th": {
        "keywords": ["ML", "อะไรคือML"],
        "content": """ML stands for Machine Learning — a field of AI that allows computers to automatically learn patterns and make predictions from data.

---

ML คือคำย่อของ Machine Learning ซึ่งเป็นเทคโนโลยี AI ที่ช่วยให้คอมพิวเตอร์เรียนรู้รูปแบบข้อมูลและสามารถคาดการณ์หรือวิเคราะห์ได้โดยอัตโนมัติ

---

ML是机器学习（Machine Learning）的缩写，是人工智能的一个领域，使计算机能够自动学习数据模式并进行预测。"""
    },
    "machine_variations_th": {
        "keywords": ["เครื่องจักร", "อะไรคือเครื่องจักร"],
        "content": """A machine is a device or system that performs work or processes tasks using mechanical, electrical, or computational power.

---

เครื่องจักรคืออุปกรณ์หรือระบบที่ทำงานหรือประมวลผลโดยใช้พลังงานกล ไฟฟ้า หรือการคำนวณ

---

机器是使用机械、电气或计算能力来执行工作或处理任务的装置或系统。"""
    },
    "learning_variations_th": {
        "keywords": ["การเรียนรู้", "อะไรคือการเรียนรู้"],
        "content": """Learning is the process of acquiring knowledge, understanding, or skills through study, experience, or teaching.

---

การเรียนรู้คือกระบวนการได้รับความรู้ ความเข้าใจ หรือทักษะ ผ่านการศึกษา ประสบการณ์ หรือการฝึกสอน

---

学习是通过研究、经验或教学获得知识、理解或技能的过程。"""
    },
    "computer_variations_th": {
        "keywords": ["คอมพิวเตอร์", "อะไรคือคอมพิวเตอร์"],
        "content": """Computers are electronic devices that process data using instructions (software) to perform calculations, store information, and execute tasks.

---

คอมพิวเตอร์คืออุปกรณ์อิเล็กทรอนิกส์ที่ประมวลผลข้อมูลตามคำสั่ง (ซอฟต์แวร์) เพื่อคำนวณ จัดเก็บข้อมูล และดำเนินการต่าง ๆ

---

计算机是一种电子设备，通过执行指令（软件）来处理数据、进行计算、存储信息并执行任务。"""
    },
    "data_variations_th": {
        "keywords": ["ข้อมูล", "อะไรคือข้อมูล"],
        "content": """Data is information in raw or structured form, such as numbers, text, or images, that can be processed or analyzed by computers.

---

ข้อมูลคือข้อเท็จจริงหรือสารสนเทศในรูปแบบดิบหรือโครงสร้าง เช่น ตัวเลข ข้อความ หรือภาพ ที่สามารถนำไปประมวลผลหรือวิเคราะห์ได้

---

数据是以原始或结构化形式存在的信息，如数字、文本或图像，计算机可以处理或分析这些信息。"""
    },
    "solar_variations_th": {
        "keywords": ["พลังงานแสงอาทิตย์", "อะไรคือพลังงานแสงอาทิตย์"],
        "content": """Solar refers to energy derived from the sun's radiation, which can be converted into electricity or heat.

---

พลังงานแสงอาทิตย์หมายถึงพลังงานที่ได้จากรังสีของดวงอาทิตย์ ซึ่งสามารถเปลี่ยนเป็นพลังงานไฟฟ้าหรือความร้อนได้

---

太阳能指来自太阳辐射的能量，可以转化为电能或热能。"""
    },
    "solar_solutions_variations_th": {
        "keywords": ["โซลูชันพลังงานแสงอาทิตย์", "อะไรคือโซลูชันพลังงานแสงอาทิตย์"],
        "content": """Solar Solutions are systems or services that use solar energy technologies (like solar panels or solar water heaters) to provide renewable power or heating.

---

โซลูชันพลังงานแสงอาทิตย์หมายถึงระบบหรือบริการที่ใช้เทคโนโลยีพลังงานแสงอาทิตย์ (เช่น แผงโซลาร์เซลล์ หรือเครื่องทำน้ำร้อนพลังงานแสงอาทิตย์) เพื่อผลิตพลังงานหมุนเวียนหรือให้ความร้อน

---

太阳能解决方案是利用太阳能技术（如太阳能电池板或太阳能热水器）来提供可再生能源或供热的系统或服务。"""
    },
    "technology_variations_th": {
        "keywords": ["เทคโนโลยี", "อะไรคือเทคโนโลยี"],
        "content": """Technologies are tools, systems, or methods developed using scientific knowledge to solve problems or improve human life.

---

เทคโนโลยีคือเครื่องมือ ระบบ หรือวิธีการที่ถูกพัฒนาด้วยความรู้ทางวิทยาศาสตร์ เพื่อแก้ปัญหาหรือพัฒนาคุณภาพชีวิตมนุษย์

---

技术是利用科学知识开发的工具、系统或方法，用于解决问题或改善人类生活。"""
    },
    "ev_variations_th": {
        "keywords": ["EV", "อะไรคือEV"],
        "content": """EV stands for Electric Vehicle — a vehicle powered by electricity stored in batteries instead of fossil fuels.

---

EV ย่อมาจาก Electric Vehicle หมายถึงยานพาหนะที่ขับเคลื่อนด้วยพลังงานไฟฟ้าที่เก็บในแบตเตอรี่แทนน้ำมันเชื้อเพลิง

---

EV是电动汽车（Electric Vehicle）的缩写，指使用储存在电池中的电能而非化石燃料驱动的车辆。"""
    },
    "ev_charger_variations_th": {
        "keywords": ["เครื่องชาร์จรถยนต์ไฟฟ้า", "อะไรคือเครื่องชาร์จรถยนต์ไฟฟ้า"],
        "content": """An EV charger is a device that supplies electric energy to recharge the battery of an electric vehicle.

---

เครื่องชาร์จรถยนต์ไฟฟ้าคืออุปกรณ์ที่จ่ายพลังงานไฟฟ้าเพื่อชาร์จแบตเตอรี่ของรถยนต์ไฟฟ้า

---

电动车充电器是一种为电动车电池充电的设备。"""
    },
    "wifi_variations_th": {
        "keywords": ["Wi-Fi", "อะไรคือWi-Fi"],
        "content": """Wi-Fi is a wireless networking technology that allows devices to connect to the internet or communicate without physical cables.

---

Wi-Fi คือเทคโนโลยีเครือข่ายไร้สายที่ช่วยให้อุปกรณ์เชื่อมต่ออินเทอร์เน็ตหรือสื่อสารกันได้โดยไม่ต้องใช้สายเคเบิล

---

Wi-Fi是一种无线网络技术，允许设备在不使用物理电缆的情况下连接到互联网或进行通信。"""
    },
    "green_arch_combined_th": {
        "keywords": ["สถาปัตยกรรมสีเขียว สถาปัตยกรรมเขียว", "อะไรคือสถาปัตยกรรมสีเขียว อะไรคือสถาปัตยกรรมเขียว"],
        "content": """Green Architecture is an environmentally conscious design approach that reduces energy use, minimizes waste, and promotes sustainability in building construction.

---

สถาปัตยกรรมสีเขียวคือแนวคิดการออกแบบอาคารที่คำนึงถึงสิ่งแวดล้อม เน้นการประหยัดพลังงาน ลดของเสีย และสร้างความยั่งยืน

---

绿色建筑是一种注重环境保护的设计方法，旨在减少能源消耗、减少浪费并促进建筑可持续性。"""
    },
    "hvac_variations_th": {
        "keywords": ["HVAC", "อะไรคือHVAC"],
        "content": """HVAC stands for Heating, Ventilation, and Air Conditioning — systems used to regulate indoor climate and air quality.

---

HVAC ย่อมาจาก Heating, Ventilation, and Air Conditioning คือระบบที่ควบคุมอุณหภูมิ การระบายอากาศ และคุณภาพอากาศภายในอาคาร

---

HVAC是供暖（Heating）、通风（Ventilation）和空调（Air Conditioning）的缩写，用于调节室内气候和空气质量的系统。"""
    },
    "mep_variations_th": {
        "keywords": ["MEP", "อะไรคือMEP"],
        "content": """MEP stands for Mechanical, Electrical, and Plumbing — the essential engineering systems integrated into building design and construction.

---

MEP ย่อมาจาก Mechanical, Electrical, and Plumbing คือระบบวิศวกรรมสำคัญที่ใช้ในการออกแบบและก่อสร้างอาคาร

---

MEP代表机械（Mechanical）、电气（Electrical）和管道（Plumbing）工程，是建筑设计和施工中不可或缺的系统。"""
    },
    "retrofit_variations_th": {
        "keywords": ["การปรับปรุงระบบ", "อะไรคือการปรับปรุงระบบ"],
        "content": """Retrofit means upgrading or modifying existing buildings or systems to improve energy efficiency, performance, or sustainability.

---

การปรับปรุงระบบ หมายถึงการอัปเกรดหรือปรับเปลี่ยนสิ่งปลูกสร้างหรือระบบเดิมให้มีประสิทธิภาพและประหยัดพลังงานมากขึ้น

---

改造是指升级或修改现有建筑或系统，以提高能源效率、性能或可持续性。"""
    },
    "controls_variations_th": {
        "keywords": ["ระบบควบคุม", "อะไรคือระบบควบคุม"],
        "content": """Controls refer to systems or devices that manage and regulate equipment operations, such as temperature, lighting, or security systems.

---

ระบบควบคุมหมายถึงอุปกรณ์หรือระบบที่ใช้ในการจัดการและควบคุมการทำงานของอุปกรณ์ เช่น ระบบไฟฟ้า อุณหภูมิ หรือระบบรักษาความปลอดภัย

---

控制系统是用于管理和调节设备运行（如温度、照明或安全系统）的系统或装置。"""
    },
    "automation_variations_th": {
        "keywords": ["ระบบอัตโนมัติ", "อะไรคือระบบอัตโนมัติ"],
        "content": """Automation is the use of technology to perform tasks automatically without human intervention.

---

ระบบอัตโนมัติหมายถึงการใช้เทคโนโลยีเพื่อให้เครื่องจักรหรือระบบทำงานได้โดยไม่ต้องมีการควบคุมจากมนุษย์

---

自动化是利用技术自动执行任务的过程，无需人工干预。"""
    },
    "bas_variations_th": {
        "keywords": ["BAS", "อะไรคือBAS"],
        "content": """BAS stands for Building Automation System — a centralized system that monitors and controls building functions like HVAC, lighting, and security.

---

BAS ย่อมาจาก Building Automation System คือระบบควบคุมส่วนกลางที่ใช้ในการตรวจสอบและจัดการการทำงานต่าง ๆ ของอาคาร เช่น HVAC แสงสว่าง และระบบความปลอดภัย

---

BAS是楼宇自动化系统（Building Automation System）的缩写，是一个集中控制HVAC、照明和安全等建筑功能的系统。"""
    },
    "smart_building_variations_th": {
        "keywords": ["อาคารอัจฉริยะ", "อะไรคืออาคารอัจฉริยะ"],
        "content": """A Smart Building uses technology and sensors to automatically control and optimize operations such as lighting, temperature, and energy use for efficiency and comfort.

---

อาคารอัจฉริยะคืออาคารที่ใช้เทคโนโลยีและเซนเซอร์เพื่อควบคุมและเพิ่มประสิทธิภาพการทำงาน เช่น ระบบไฟฟ้า อุณหภูมิ และการใช้พลังงาน

---

智慧建筑利用技术和传感器自动控制与优化照明、温度和能源使用等操作，以提高效率和舒适度。"""
    },
    "realtime_monitoring_variations_th": {
        "keywords": ["การตรวจสอบแบบเรียลไทม์", "อะไรคือการตรวจสอบแบบเรียลไทม์"],
        "content": """Real-time monitoring is the continuous observation and tracking of systems or data as events happen, allowing immediate response or adjustments.

---

การตรวจสอบแบบเรียลไทม์คือการติดตามและเฝ้าดูระบบหรือข้อมูลแบบต่อเนื่องในขณะที่เหตุการณ์กำลังเกิดขึ้น เพื่อให้สามารถตอบสนองหรือปรับเปลี่ยนได้ทันที

---

实时监控是对系统或数据进行持续观察和跟踪的过程，以便在事件发生时立即响应或调整。"""
    },
    "predictive_maintenance_variations_th": {
        "keywords": ["การบำรุงรักษาเชิงคาดการณ์", "อะไรคือการบำรุงรักษาเชิงคาดการณ์"],
        "content": """Predictive maintenance uses data and AI to predict when equipment will fail, allowing maintenance before a breakdown occurs.

---

การบำรุงรักษาเชิงคาดการณ์คือการใช้ข้อมูลและ AI เพื่อทำนายการเสียของอุปกรณ์ และซ่อมแซมก่อนที่ความเสียหายจะเกิดขึ้นจริง

---

预测性维护利用数据和人工智能预测设备故障的时间，从而在设备损坏前进行维护。"""
    },
    "occupant_comfort_variations_th": {
        "keywords": ["ความสบายของผู้ใช้อาคาร", "อะไรคือความสบายของผู้ใช้อาคาร"],
        "content": """Occupant comfort refers to the physical and psychological well-being of people inside a building, influenced by factors like temperature, lighting, and air quality.

---

ความสบายของผู้ใช้อาคารหมายถึงความเป็นอยู่ที่ดีทั้งทางกายภาพและจิตใจของผู้อยู่อาศัย เช่น อุณหภูมิ แสง และคุณภาพอากาศ

---

居住舒适度指建筑内部人员的身心舒适度，受温度、照明和空气质量等因素影响。"""
    },
    "environmental_services_variations_th": {
        "keywords": ["บริการด้านสิ่งแวดล้อม", "อะไรคือบริการด้านสิ่งแวดล้อม"],
        "content": """Environmental services involve managing and protecting natural resources through waste management, pollution control, and sustainability programs.

---

บริการด้านสิ่งแวดล้อมคือการจัดการและปกป้องทรัพยากรธรรมชาติ เช่น การจัดการของเสีย การควบคุมมลพิษ และการพัฒนาอย่างยั่งยืน

---

环境服务包括通过废物管理、污染控制和可持续发展计划来管理和保护自然资源。"""
    },
    "energy_saving_variations_th": {
        "keywords": ["การประหยัดพลังงาน", "อะไรคือการประหยัดพลังงาน"],
        "content": """Energy saving means reducing energy use through efficient technologies, behavior, or design, to lower costs and environmental impact.

---

การประหยัดพลังงานหมายถึงการลดการใช้พลังงานผ่านเทคโนโลยีที่มีประสิทธิภาพ พฤติกรรมที่เหมาะสม หรือการออกแบบที่ดี

---

节能是通过高效技术、行为或设计减少能源使用，从而降低成本和环境影响。"""
    },
    "environmental_footprint_variations_th": {
        "keywords": ["รอยเท้าสิ่งแวดล้อม", "อะไรคือรอยเท้าสิ่งแวดล้อม"],
        "content": """Environmental footprints measure the total impact of human activities on the environment, including energy use, emissions, and resource consumption.

---

รอยเท้าสิ่งแวดล้อมหมายถึงผลกระทบทั้งหมดที่กิจกรรมของมนุษย์มีต่อสิ่งแวดล้อม เช่น การใช้พลังงาน การปล่อยคาร์บอน และการใช้ทรัพยากร

---

环境足迹衡量人类活动对环境的总影响，包括能源使用、排放和资源消耗。"""
    },
    "security_system_variations_th": {
        "keywords": ["ระบบรักษาความปลอดภัย", "อะไรคือระบบรักษาความปลอดภัย"],
        "content": """A security system is a set of devices and software designed to protect buildings or data from unauthorized access, theft, or harm.

---

ระบบรักษาความปลอดภัยคือชุดอุปกรณ์และซอฟต์แวร์ที่ออกแบบมาเพื่อป้องกันอาคารหรือข้อมูลจากการเข้าถึงโดยไม่ได้รับอนุญาตหรือการโจรกรรม

---

安防系统是一组设备和软件，用于保护建筑或数据免受未经授权的访问、盗窃或破坏。"""
    },
    "access_control_variations_th": {
        "keywords": ["การควบคุมการเข้าถึง", "อะไรคือการควบคุมการเข้าถึง"],
        "content": """Access control is a security process that restricts or grants entry to specific areas, systems, or information based on authorization.

---

การควบคุมการเข้าถึงคือกระบวนการรักษาความปลอดภัยที่จำกัดหรืออนุญาตให้บุคคลเข้าถึงพื้นที่หรือข้อมูลตามสิทธิ์ที่กำหนด

---

门禁控制是一种安全管理过程，根据授权限制或允许进入特定区域、系统或信息。"""
    },
    "green_construction_variations_th": {
        "keywords": ["การก่อสร้างสีเขียว", "อะไรคือการก่อสร้างสีเขียว"],
        "content": """Green construction involves building practices that are sustainable, energy-efficient, and environmentally responsible.

---

การก่อสร้างสีเขียวคือแนวทางการก่อสร้างที่ยั่งยืน มีประสิทธิภาพด้านพลังงาน และเป็นมิตรต่อสิ่งแวดล้อม

---

绿色施工是指可持续、节能且对环境负责的建筑实践。"""
    },
    "fitout_variations_th": {
        "keywords": ["งานตกแต่งภายใน", "อะไรคืองานตกแต่งภายใน"],
        "content": """Fit Out refers to the process of furnishing and equipping interior spaces to make them functional and ready for use.

---

งานตกแต่งภายใน หมายถึงกระบวนการตกแต่งและติดตั้งอุปกรณ์ภายในอาคารให้พร้อมใช้งาน

---

室内装修是为使空间具备功能性并可投入使用而进行的布置与设备安装过程。"""
    },
    "renovation_variations_th": {
        "keywords": ["การปรับปรุงหรือรีโนเวท", "อะไรคือการปรับปรุงหรือรีโนเวท"],
        "content": """Renovation means restoring, repairing, or upgrading existing buildings to improve functionality or appearance.

---

การปรับปรุงหรือรีโนเวทคือการซ่อมแซมหรือปรับปรุงอาคารเดิมให้ดีขึ้นทั้งในด้านรูปลักษณ์และการใช้งาน

---

翻新是修复、改进或升级现有建筑的过程，以提升功能或外观。"""
    },
    "reinstatement_variations_th": {
        "keywords": ["การคืนสภาพ", "อะไรคือการคืนสภาพ"],
        "content": """Reinstatement is the process of returning a property to its original condition, often after a lease ends or construction work is completed.

---

การคืนสภาพคือการนำทรัพย์สินหรืออาคารกลับคืนสู่สภาพเดิม มักทำหลังจากหมดสัญญาเช่าหรือหลังงานก่อสร้างเสร็จสิ้น

---

恢复原状是将物业恢复至原始状态的过程，通常发生在租约结束或施工完成后。"""
    },
    "vertical_garden_variations_th": {
        "keywords": ["สวนแนวตั้ง", "อะไรคือสวนแนวตั้ง"],
        "content": """A Vertical Garden is a structure where plants grow on vertically suspended panels, used for aesthetics, insulation, and air purification.

---

สวนแนวตั้งคือโครงสร้างที่ปลูกต้นไม้ในแนวตั้ง เพื่อความสวยงาม ฉนวนกันความร้อน และช่วยฟอกอากาศ

---

垂直花园是一种植物在垂直悬挂面板上生长的结构，用于美化、隔热和净化空气。"""
    },
    "smart_home_variations_th": {
        "keywords": ["บ้านอัจฉริยะ", "อะไรคือบ้านอัจฉริยะ"],
        "content": """A Smart Home uses interconnected devices and automation systems to control lighting, temperature, appliances, and security remotely.

---

บ้านอัจฉริยะคือบ้านที่ใช้เทคโนโลยีและระบบอัตโนมัติในการควบคุมไฟฟ้า อุณหภูมิ เครื่องใช้ไฟฟ้า และระบบรักษาความปลอดภัยได้จากระยะไกล

---

智能家居通过互联设备和自动化系统远程控制照明、温度、电器和安防系统。"""
    },
    "smart_farming_variations_th": {
        "keywords": ["เกษตรอัจฉริยะ", "อะไรคือเกษตรอัจฉริยะ"],
        "content": """Smart farming uses IoT, sensors, and AI technologies to optimize agricultural production, reduce waste, and improve efficiency.

---

เกษตรอัจฉริยะคือการใช้เทคโนโลยี IoT เซนเซอร์ และ AI เพื่อเพิ่มประสิทธิภาพการผลิต ลดของเสีย และเพิ่มผลผลิตทางการเกษตร

---

智慧农业利用物联网（IoT）、传感器和人工智能技术优化农业生产、减少浪费并提高效率。"""
    },
    "website_variations_th": {
        "keywords": ["เว็บไซต์คื", "อะไรคือเว็บไซต์คื"],
        "content": """A website is a collection of web pages accessible via the internet, typically under a single domain name.

---

เว็บไซต์คือชุดของหน้าเว็บที่สามารถเข้าถึงได้ผ่านอินเทอร์เน็ต ภายใต้ชื่อโดเมนเดียวกัน

---

网站是一组网页的集合，可通过互联网访问，通常位于同一个域名下。"""
    },
    "website_dev_variations_th": {
        "keywords": ["การพัฒนาเว็บไซต์", "อะไรคือการพัฒนาเว็บไซต์"],
        "content": """Website development is the process of designing, coding, and maintaining websites to ensure functionality, accessibility, and performance.

---

การพัฒนาเว็บไซต์คือกระบวนการออกแบบ เขียนโค้ด และดูแลเว็บไซต์ให้สามารถทำงานได้อย่างมีประสิทธิภาพและเข้าถึงได้ง่าย

---

网站开发是设计、编程和维护网站的过程，以确保其功能性、可访问性和性能。"""
    },
    "seo_variations_th": {
        "keywords": ["SEO", "อะไรคือSEO"],
        "content": """SEO (Search Engine Optimization) is the practice of improving a website's visibility in search engine results to attract more organic traffic.

---

SEO (Search Engine Optimization) คือการปรับปรุงเว็บไซต์ให้ติดอันดับสูงในการค้นหาผ่านเสิร์ชเอนจิน เพื่อเพิ่มจำนวนผู้เข้าชมแบบธรรมชาติ

---

SEO（搜索引擎优化）是提高网站在搜索引擎结果中可见度的实践，以吸引更多自然流量。"""
    },
    "coding_variations_th": {
        "keywords": ["การเขียนโค้ด", "อะไรคือการเขียนโค้ด"],
        "content": """Coding is the process of writing instructions in a programming language to create software, applications, or websites.

---

การเขียนโค้ดคือกระบวนการเขียนคำสั่งด้วยภาษาคอมพิวเตอร์เพื่อสร้างซอฟต์แวร์ แอปพลิเคชัน หรือเว็บไซต์

---

编程是用编程语言编写指令的过程，用于创建软件、应用程序或网站。"""
    },
    "phone_variations_th": {
        "keywords": ["หมายเลขโทรศัพท์ของคุณค", "อะไรคือหมายเลขโทรศัพท์ของคุณค"],
        "content": """You can contact us at +66 (0)81 854 4291

---

คุณสามารถติดต่อฉันได้ที่ +66 (0)81 854 4291

---

您可以拨打 +66 (0)81 854 4291 联系我们。"""
    },
    "email_variations_th": {
        "keywords": ["อีเมลของคุณค", "อะไรคืออีเมลของคุณค"],
        "content": """You can email me through cblue.thailand@gmail.com

---

คุณสามารถส่งอีเมลถึงฉันได้ที่ cblue.thailand@gmail.com

---

您可以通过 cblue.thailand@gmail.com 给我发送电子邮件。"""
    },
    "ai_chinese": {
        "keywords": ["人工智能（AI）", "人工智能", "什么是人工智能"],
        "content": """AI (Artificial Intelligence) is the simulation of human intelligence in machines that are programmed to think, reason, learn, and make decisions like humans.

---

ปัญญาประดิษฐ์ คือการจำลองความฉลาดของมนุษย์ในเครื่องจักรที่ถูกโปรแกรมให้สามารถคิด วิเคราะห์ เรียนรู้ และตัดสินใจได้เหมือนมนุษย์

---

人工智能（AI，Artificial Intelligence）是指在机器中模拟人类智能的技术，使其能够像人类一样思考、推理、学习和做出决策。"""
    },
    "chatbot_chinese": {
        "keywords": ["聊天机器人（Chatbot）", "聊天机器人", "什么是聊天机器人"],
        "content": """A chatbot is a software application that can converse with users through text or voice, often used to provide information or automate customer service tasks.

---

แชตบอทคือโปรแกรมซอฟต์แวร์ที่สามารถสนทนากับผู้ใช้งานผ่านข้อความหรือเสียง มักใช้เพื่อให้ข้อมูลหรือช่วยงานบริการลูกค้าแบบอัตโนมัติ

---

聊天机器人是一种软件应用程序，可以通过文字或语音与用户进行对话，通常用于提供信息或自动化客户服务任务。"""
    },
    "ai_chatbot_dev_chinese": {
        "keywords": ["AI聊天机器人开发", "什么是AI聊天机器人开发"],
        "content": """AI chatbot development is the process of building chatbots that use artificial intelligence and natural language processing (NLP) to understand, learn from, and respond intelligently to user inputs.

---

การพัฒนาแชตบอท AI คือกระบวนการสร้างแชตบอทที่ใช้เทคโนโลยีปัญญาประดิษฐ์และการประมวลผลภาษาธรรมชาติ (NLP) เพื่อให้เข้าใจ เรียนรู้ และตอบสนองต่อผู้ใช้อย่างชาญฉลาด

---

AI聊天机器人开发是构建使用人工智能和自然语言处理（NLP）技术的聊天机器人的过程，使其能够理解、学习并智能地回应用户输入。"""
    },
    "chatbot_dev_chinese": {
        "keywords": ["聊天机器人开发", "什么是聊天机器人开发"],
        "content": """Chatbot development is the creation of automated conversational programs that can interact with users through predefined rules, scripts, or AI-based understanding.

---

การพัฒนาแชตบอทคือการสร้างโปรแกรมสนทนาอัตโนมัติที่สามารถโต้ตอบกับผู้ใช้ได้ตามกฎที่ตั้งไว้ล่วงหน้า หรือโดยใช้ความเข้าใจจาก AI

---

聊天机器人开发是创建能通过预设规则、脚本或基于AI理解与用户互动的自动化对话程序的过程。"""
    },
    "software_chinese": {
        "keywords": ["软件（Software）", "软件", "什么是软件"],
        "content": """Software is a set of instructions, programs, or data that tell a computer how to perform specific tasks or functions.

---

ซอฟต์แวร์คือชุดคำสั่ง โปรแกรม หรือข้อมูลที่บอกคอมพิวเตอร์ให้ทำงานหรือดำเนินการตามที่กำหนดไว้

---

软件是一组指令、程序或数据，用来告诉计算机如何执行特定任务或功能。"""
    },
    "software_dev_chinese": {
        "keywords": ["软件开发", "什么是软件开发"],
        "content": """Software development is the process of designing, coding, testing, and maintaining applications, systems, or programs to meet user needs.

---

การพัฒนาซอฟต์แวร์คือกระบวนการออกแบบ เขียนโค้ด ทดสอบ และดูแลรักษาโปรแกรมหรือระบบ เพื่อให้ตอบสนองความต้องการของผู้ใช้งาน

---

软件开发是设计、编程、测试和维护应用程序、系统或程序的过程，以满足用户需求。"""
    },
    "machine_learning_chinese": {
        "keywords": ["机器学习（Machine Learning, ML）", "机器学习", "什么是机器学习"],
        "content": """Machine Learning (ML) is a branch of AI that enables computers to learn from data and improve their performance without being explicitly programmed.

---

การเรียนรู้ของเครื่อง (Machine Learning - ML) คือสาขาหนึ่งของ AI ที่ทำให้คอมพิวเตอร์สามารถเรียนรู้จากข้อมูลและปรับปรุงประสิทธิภาพได้โดยไม่ต้องเขียนโปรแกรมใหม่ทั้งหมด

---

机器学习（ML）是人工智能的一个分支，使计算机能够从数据中学习并不断提高性能，而无需明确编程。"""
    },
    "ml_chinese": {
        "keywords": ["ML", "什么是ML"],
        "content": """ML stands for Machine Learning — a field of AI that allows computers to automatically learn patterns and make predictions from data.

---

ML คือคำย่อของ Machine Learning ซึ่งเป็นเทคโนโลยี AI ที่ช่วยให้คอมพิวเตอร์เรียนรู้รูปแบบข้อมูลและสามารถคาดการณ์หรือวิเคราะห์ได้โดยอัตโนมัติ

---

ML是机器学习（Machine Learning）的缩写，是人工智能的一个领域，使计算机能够自动学习数据模式并进行预测。"""
    },
    "machine_chinese": {
        "keywords": ["机器", "什么是机器"],
        "content": """A machine is a device or system that performs work or processes tasks using mechanical, electrical, or computational power.

---

เครื่องจักรคืออุปกรณ์หรือระบบที่ทำงานหรือประมวลผลโดยใช้พลังงานกล ไฟฟ้า หรือการคำนวณ

---

机器是使用机械、电气或计算能力来执行工作或处理任务的装置或系统。"""
    },
    "learning_chinese": {
        "keywords": ["学习", "什么是学习"],
        "content": """Learning is the process of acquiring knowledge, understanding, or skills through study, experience, or teaching.

---

การเรียนรู้คือกระบวนการได้รับความรู้ ความเข้าใจ หรือทักษะ ผ่านการศึกษา ประสบการณ์ หรือการฝึกสอน

---

学习是通过研究、经验或教学获得知识、理解或技能的过程。"""
    },
    "computer_chinese": {
        "keywords": ["计算机", "什么是计算机"],
        "content": """Computers are electronic devices that process data using instructions (software) to perform calculations, store information, and execute tasks.

---

คอมพิวเตอร์คืออุปกรณ์อิเล็กทรอนิกส์ที่ประมวลผลข้อมูลตามคำสั่ง (ซอฟต์แวร์) เพื่อคำนวณ จัดเก็บข้อมูล และดำเนินการต่าง ๆ

---

计算机是一种电子设备，通过执行指令（软件）来处理数据、进行计算、存储信息并执行任务。"""
    },
    "data_chinese": {
        "keywords": ["数据", "什么是数据"],
        "content": """Data is information in raw or structured form, such as numbers, text, or images, that can be processed or analyzed by computers.

---

ข้อมูลคือข้อเท็จจริงหรือสารสนเทศในรูปแบบดิบหรือโครงสร้าง เช่น ตัวเลข ข้อความ หรือภาพ ที่สามารถนำไปประมวลผลหรือวิเคราะห์ได้

---

数据是以原始或结构化形式存在的信息，如数字、文本或图像，计算机可以处理或分析这些信息。"""
    },
    "solar_chinese": {
        "keywords": ["太阳能（Solar）", "太阳能", "什么是太阳能"],
        "content": """Solar refers to energy derived from the sun's radiation, which can be converted into electricity or heat.

---

พลังงานแสงอาทิตย์หมายถึงพลังงานที่ได้จากรังสีของดวงอาทิตย์ ซึ่งสามารถเปลี่ยนเป็นพลังงานไฟฟ้าหรือความร้อนได้

---

太阳能指来自太阳辐射的能量，可以转化为电能或热能。"""
    },
    "solar_solutions_chinese": {
        "keywords": ["太阳能解决方案（Solar Solutions）", "太阳能解决方案", "什么是太阳能解决方案"],
        "content": """Solar Solutions are systems or services that use solar energy technologies (like solar panels or solar water heaters) to provide renewable power or heating.

---

โซลูชันพลังงานแสงอาทิตย์หมายถึงระบบหรือบริการที่ใช้เทคโนโลยีพลังงานแสงอาทิตย์ (เช่น แผงโซลาร์เซลล์ หรือเครื่องทำน้ำร้อนพลังงานแสงอาทิตย์) เพื่อผลิตพลังงานหมุนเวียนหรือให้ความร้อน

---

太阳能解决方案是利用太阳能技术（如太阳能电池板或太阳能热水器）来提供可再生能源或供热的系统或服务。"""
    },
    "technology_chinese": {
        "keywords": ["技术（Technologies）", "技术", "什么是技术"],
        "content": """Technologies are tools, systems, or methods developed using scientific knowledge to solve problems or improve human life.

---

เทคโนโลยีคือเครื่องมือ ระบบ หรือวิธีการที่ถูกพัฒนาด้วยความรู้ทางวิทยาศาสตร์ เพื่อแก้ปัญหาหรือพัฒนาคุณภาพชีวิตมนุษย์

---

技术是利用科学知识开发的工具、系统或方法，用于解决问题或改善人类生活。"""
    },
    "ev_chinese": {
        "keywords": ["电动车（EV）", "电动车", "什么是电动车"],
        "content": """EV stands for Electric Vehicle — a vehicle powered by electricity stored in batteries instead of fossil fuels.

---

EV ย่อมาจาก Electric Vehicle หมายถึงยานพาหนะที่ขับเคลื่อนด้วยพลังงานไฟฟ้าที่เก็บในแบตเตอรี่แทนน้ำมันเชื้อเพลิง

---

EV是电动汽车（Electric Vehicle）的缩写，指使用储存在电池中的电能而非化石燃料驱动的车辆。"""
    },
    "ev_charger_chinese": {
        "keywords": ["电动车充电器（EV Charger）", "电动车充电器", "什么是电动车充电器"],
        "content": """An EV charger is a device that supplies electric energy to recharge the battery of an electric vehicle.

---

เครื่องชาร์จรถยนต์ไฟฟ้าคืออุปกรณ์ที่จ่ายพลังงานไฟฟ้าเพื่อชาร์จแบตเตอรี่ของรถยนต์ไฟฟ้า

---

电动车充电器是一种为电动车电池充电的设备。"""
    },
    "wifi_chinese": {
        "keywords": ["无线网", "什么是无线网"],
        "content": """Wi-Fi is a wireless networking technology that allows devices to connect to the internet or communicate without physical cables.

---

Wi-Fi คือเทคโนโลยีเครือข่ายไร้สายที่ช่วยให้อุปกรณ์เชื่อมต่ออินเทอร์เน็ตหรือสื่อสารกันได้โดยไม่ต้องใช้สายเคเบิล

---

Wi-Fi是一种无线网络技术，允许设备在不使用物理电缆的情况下连接到互联网或进行通信。"""
    },
    "green_architecture_chinese": {
        "keywords": ["绿色建筑（Green Architecture）", "绿色建筑", "什么是绿色建筑"],
        "content": """Green Architecture is an environmentally conscious design approach that reduces energy use, minimizes waste, and promotes sustainability in building construction.

---

สถาปัตยกรรมสีเขียวคือแนวคิดการออกแบบอาคารที่คำนึงถึงสิ่งแวดล้อม เน้นการประหยัดพลังงาน ลดของเสีย และสร้างความยั่งยืน

---

绿色建筑是一种注重环境保护的设计方法，旨在减少能源消耗、减少浪费并促进建筑可持续性。"""
    },
    "eco_friendly_chinese": {
        "keywords": ["环保（Eco-friendly）", "环保", "什么是环保"],
        "content": """Eco-friendly refers to products, practices, or systems that cause minimal harm to the environment.

---

เป็นมิตรต่อสิ่งแวดล้อมหมายถึงผลิตภัณฑ์หรือวิธีการที่ส่งผลกระทบต่อสิ่งแวดล้อมน้อยที่สุด

---

环保是指对环境危害最小的产品、做法或系统。"""
    },
    "hvac_chinese": {
        "keywords": ["暖通空调", "什么是暖通空调"],
        "content": """HVAC stands for Heating, Ventilation, and Air Conditioning — systems used to regulate indoor climate and air quality.

---

HVAC ย่อมาจาก Heating, Ventilation, and Air Conditioning คือระบบที่ควบคุมอุณหภูมิ การระบายอากาศ และคุณภาพอากาศภายในอาคาร

---

HVAC是供暖（Heating）、通风（Ventilation）和空调（Air Conditioning）的缩写，用于调节室内气候和空气质量的系统。"""
    },
    "mep_chinese": {
        "keywords": ["机电水", "什么是机电水"],
        "content": """MEP stands for Mechanical, Electrical, and Plumbing — the essential engineering systems integrated into building design and construction.

---

MEP ย่อมาจาก Mechanical, Electrical, and Plumbing คือระบบวิศวกรรมสำคัญที่ใช้ในการออกแบบและก่อสร้างอาคาร

---

MEP代表机械（Mechanical）、电气（Electrical）和管道（Plumbing）工程，是建筑设计和施工中不可或缺的系统。"""
    },
    "retrofit_chinese": {
        "keywords": ["改造（Retrofit）", "改造", "什么是改造"],
        "content": """Retrofit means upgrading or modifying existing buildings or systems to improve energy efficiency, performance, or sustainability.

---

การปรับปรุงระบบ หมายถึงการอัปเกรดหรือปรับเปลี่ยนสิ่งปลูกสร้างหรือระบบเดิมให้มีประสิทธิภาพและประหยัดพลังงานมากขึ้น

---

改造是指升级或修改现有建筑或系统，以提高能源效率、性能或可持续性。"""
    },
    "controls_chinese": {
        "keywords": ["控制系统（Controls）", "控制系统", "什么是控制系统"],
        "content": """Controls refer to systems or devices that manage and regulate equipment operations, such as temperature, lighting, or security systems.

---

ระบบควบคุมหมายถึงอุปกรณ์หรือระบบที่ใช้ในการจัดการและควบคุมการทำงานของอุปกรณ์ เช่น ระบบไฟฟ้า อุณหภูมิ หรือระบบรักษาความปลอดภัย

---

控制系统是用于管理和调节设备运行（如温度、照明或安全系统）的系统或装置。"""
    },
    "automation_chinese": {
        "keywords": ["自动化（Automation）", "自动化", "什么是自动化"],
        "content": """Automation is the use of technology to perform tasks automatically without human intervention.

---

ระบบอัตโนมัติหมายถึงการใช้เทคโนโลยีเพื่อให้เครื่องจักรหรือระบบทำงานได้โดยไม่ต้องมีการควบคุมจากมนุษย์

---

自动化是利用技术自动执行任务的过程，无需人工干预。"""
    },
    "bas_chinese": {
        "keywords": ["楼宇自动化系统", "什么是楼宇自动化系统"],
        "content": """BAS stands for Building Automation System — a centralized system that monitors and controls building functions like HVAC, lighting, and security.

---

BAS ย่อมาจาก Building Automation System คือระบบควบคุมส่วนกลางที่ใช้ในการตรวจสอบและจัดการการทำงานต่าง ๆ ของอาคาร เช่น HVAC แสงสว่าง และระบบความปลอดภัย

---

BAS是楼宇自动化系统（Building Automation System）的缩写，是一个集中控制HVAC、照明和安全等建筑功能的系统。"""
    },
    "smart_building_chinese": {
        "keywords": ["智慧建筑（Smart Building）", "智慧建筑", "什么是智慧建筑"],
        "content": """A Smart Building uses technology and sensors to automatically control and optimize operations such as lighting, temperature, and energy use for efficiency and comfort.

---

อาคารอัจฉริยะคืออาคารที่ใช้เทคโนโลยีและเซนเซอร์เพื่อควบคุมและเพิ่มประสิทธิภาพการทำงาน เช่น ระบบไฟฟ้า อุณหภูมิ และการใช้พลังงาน

---

智慧建筑利用技术和传感器自动控制与优化照明、温度和能源使用等操作，以提高效率和舒适度。"""
    },
    "realtime_monitoring_chinese": {
        "keywords": ["实时监控（Real-time Monitoring）", "实时监控", "什么是实时监控"],
        "content": """Real-time monitoring is the continuous observation and tracking of systems or data as events happen, allowing immediate response or adjustments.

---

การตรวจสอบแบบเรียลไทม์คือการติดตามและเฝ้าดูระบบหรือข้อมูลแบบต่อเนื่องในขณะที่เหตุการณ์กำลังเกิดขึ้น เพื่อให้สามารถตอบสนองหรือปรับเปลี่ยนได้ทันที

---

实时监控是对系统或数据进行持续观察和跟踪的过程，以便在事件发生时立即响应或调整。"""
    },
    "predictive_maintenance_chinese": {
        "keywords": ["预测性维护（Predictive Maintenance）", "预测性维护", "什么是预测性维护"],
        "content": """Predictive maintenance uses data and AI to predict when equipment will fail, allowing maintenance before a breakdown occurs.

---

การบำรุงรักษาเชิงคาดการณ์คือการใช้ข้อมูลและ AI เพื่อทำนายการเสียของอุปกรณ์ และซ่อมแซมก่อนที่ความเสียหายจะเกิดขึ้นจริง

---

预测性维护利用数据和人工智能预测设备故障的时间，从而在设备损坏前进行维护。"""
    },
    "occupant_comfort_chinese": {
        "keywords": ["居住舒适度（Occupant Comfort）", "居住舒适度", "什么是居住舒适度"],
        "content": """Occupant comfort refers to the physical and psychological well-being of people inside a building, influenced by factors like temperature, lighting, and air quality.

---

ความสบายของผู้ใช้อาคารหมายถึงความเป็นอยู่ที่ดีทั้งทางกายภาพและจิตใจของผู้อยู่อาศัย เช่น อุณหภูมิ แสง และคุณภาพอากาศ

---

居住舒适度指建筑内部人员的身心舒适度，受温度、照明和空气质量等因素影响。"""
    },
    "environmental_services_chinese": {
        "keywords": ["环境服务（Environmental Services）", "环境服务", "什么是环境服务"],
        "content": """Environmental services involve managing and protecting natural resources through waste management, pollution control, and sustainability programs.

---

บริการด้านสิ่งแวดล้อมคือการจัดการและปกป้องทรัพยากรธรรมชาติ เช่น การจัดการของเสีย การควบคุมมลพิษ และการพัฒนาอย่างยั่งยืน

---

环境服务包括通过废物管理、污染控制和可持续发展计划来管理和保护自然资源。"""
    },
    "energy_saving_chinese": {
        "keywords": ["节能（Energy Saving）", "节能", "什么是节能"],
        "content": """Energy saving means reducing energy use through efficient technologies, behavior, or design, to lower costs and environmental impact.

---

การประหยัดพลังงานหมายถึงการลดการใช้พลังงานผ่านเทคโนโลยีที่มีประสิทธิภาพ พฤติกรรมที่เหมาะสม หรือการออกแบบที่ดี

---

节能是通过高效技术、行为或设计减少能源使用，从而降低成本和环境影响。"""
    },
    "environmental_footprint_chinese": {
        "keywords": ["环境足迹（Environmental Footprints）", "环境足迹", "什么是环境足迹"],
        "content": """Environmental footprints measure the total impact of human activities on the environment, including energy use, emissions, and resource consumption.

---

รอยเท้าสิ่งแวดล้อมหมายถึงผลกระทบทั้งหมดที่กิจกรรมของมนุษย์มีต่อสิ่งแวดล้อม เช่น การใช้พลังงาน การปล่อยคาร์บอน และการใช้ทรัพยากร

---

环境足迹衡量人类活动对环境的总影响，包括能源使用、排放和资源消耗。"""
    },
    "security_system_chinese": {
        "keywords": ["安防系统（Security System）", "安防系统", "什么是安防系统"],
        "content": """A security system is a set of devices and software designed to protect buildings or data from unauthorized access, theft, or harm.

---

ระบบรักษาความปลอดภัยคือชุดอุปกรณ์และซอฟต์แวร์ที่ออกแบบมาเพื่อป้องกันอาคารหรือข้อมูลจากการเข้าถึงโดยไม่ได้รับอนุญาตหรือการโจรกรรม

---

安防系统是一组设备和软件，用于保护建筑或数据免受未经授权的访问、盗窃或破坏。"""
    },
    "access_control_chinese": {
        "keywords": ["门禁控制（Access Control）", "门禁控制", "什么是门禁控制"],
        "content": """Access control is a security process that restricts or grants entry to specific areas, systems, or information based on authorization.

---

การควบคุมการเข้าถึงคือกระบวนการรักษาความปลอดภัยที่จำกัดหรืออนุญาตให้บุคคลเข้าถึงพื้นที่หรือข้อมูลตามสิทธิ์ที่กำหนด

---

门禁控制是一种安全管理过程，根据授权限制或允许进入特定区域、系统或信息。"""
    },
    "green_construction_chinese": {
        "keywords": ["绿色施工（Green Construction）", "绿色施工", "什么是绿色施工"],
        "content": """Green construction involves building practices that are sustainable, energy-efficient, and environmentally responsible.

---

การก่อสร้างสีเขียวคือแนวทางการก่อสร้างที่ยั่งยืน มีประสิทธิภาพด้านพลังงาน และเป็นมิตรต่อสิ่งแวดล้อม

---

绿色施工是指可持续、节能且对环境负责的建筑实践。"""
    },
    "fitout_chinese": {
        "keywords": ["室内装修（Fit Out）", "室内装修", "什么是室内装修"],
        "content": """Fit Out refers to the process of furnishing and equipping interior spaces to make them functional and ready for use.

---

งานตกแต่งภายใน หมายถึงกระบวนการตกแต่งและติดตั้งอุปกรณ์ภายในอาคารให้พร้อมใช้งาน

---

室内装修是为使空间具备功能性并可投入使用而进行的布置与设备安装过程。"""
    },
    "renovation_chinese": {
        "keywords": ["翻新（Renovation）", "翻新", "什么是翻新"],
        "content": """Renovation means restoring, repairing, or upgrading existing buildings to improve functionality or appearance.

---

การปรับปรุงหรือรีโนเวทคือการซ่อมแซมหรือปรับปรุงอาคารเดิมให้ดีขึ้นทั้งในด้านรูปลักษณ์และการใช้งาน

---

翻新是修复、改进或升级现有建筑的过程，以提升功能或外观。"""
    },
    "reinstatement_chinese": {
        "keywords": ["恢复原状（Reinstatement）", "恢复原状", "什么是恢复原状"],
        "content": """Reinstatement is the process of returning a property to its original condition, often after a lease ends or construction work is completed.

---

การคืนสภาพคือการนำทรัพย์สินหรืออาคารกลับคืนสู่สภาพเดิม มักทำหลังจากหมดสัญญาเช่าหรือหลังงานก่อสร้างเสร็จสิ้น

---

恢复原状是将物业恢复至原始状态的过程，通常发生在租约结束或施工完成后。"""
    },
    "vertical_garden_chinese": {
        "keywords": ["垂直花园（Vertical Garden）", "垂直花园", "什么是垂直花园"],
        "content": """A Vertical Garden is a structure where plants grow on vertically suspended panels, used for aesthetics, insulation, and air purification.

---

สวนแนวตั้งคือโครงสร้างที่ปลูกต้นไม้ในแนวตั้ง เพื่อความสวยงาม ฉนวนกันความร้อน และช่วยฟอกอากาศ

---

垂直花园是一种植物在垂直悬挂面板上生长的结构，用于美化、隔热和净化空气。"""
    },
    "smart_home_chinese": {
        "keywords": ["智能家居（Smart Home）", "智能家居", "什么是智能家居"],
        "content": """A Smart Home uses interconnected devices and automation systems to control lighting, temperature, appliances, and security remotely.

---

บ้านอัจฉริยะคือบ้านที่ใช้เทคโนโลยีและระบบอัตโนมัติในการควบคุมไฟฟ้า อุณหภูมิ เครื่องใช้ไฟฟ้า และระบบรักษาความปลอดภัยได้จากระยะไกล

---

智能家居通过互联设备和自动化系统远程控制照明、温度、电器和安防系统。"""
    },
    "smart_farming_chinese": {
        "keywords": ["智慧农业（Smart Farming）", "智慧农业", "什么是智慧农业"],
        "content": """Smart farming uses IoT, sensors, and AI technologies to optimize agricultural production, reduce waste, and improve efficiency.

---

เกษตรอัจฉริยะคือการใช้เทคโนโลยี IoT เซนเซอร์ และ AI เพื่อเพิ่มประสิทธิภาพการผลิต ลดของเสีย และเพิ่มผลผลิตทางการเกษตร

---

智慧农业利用物联网（IoT）、传感器和人工智能技术优化农业生产、减少浪费并提高效率。"""
    },
    "website_chinese": {
        "keywords": ["网站（Website）", "网站", "什么是网站"],
        "content": """A website is a collection of web pages accessible via the internet, typically under a single domain name.

---

เว็บไซต์คือชุดของหน้าเว็บที่สามารถเข้าถึงได้ผ่านอินเทอร์เน็ต ภายใต้ชื่อโดเมนเดียวกัน

---

网站是一组网页的集合，可通过互联网访问，通常位于同一个域名下。"""
    },
    "website_dev_chinese": {
        "keywords": ["网站开发（Website Development）", "网站开发", "什么是网站开发"],
        "content": """Website development is the process of designing, coding, and maintaining websites to ensure functionality, accessibility, and performance.

---

การพัฒนาเว็บไซต์คือกระบวนการออกแบบ เขียนโค้ด และดูแลเว็บไซต์ให้สามารถทำงานได้อย่างมีประสิทธิภาพและเข้าถึงได้ง่าย

---

网站开发是设计、编程和维护网站的过程，以确保其功能性、可访问性和性能。"""
    },
    "seo_chinese": {
        "keywords": ["搜索引擎优化", "什么是搜索引擎优化"],
        "content": """SEO (Search Engine Optimization) is the practice of improving a website's visibility in search engine results to attract more organic traffic.

---

SEO (Search Engine Optimization) คือการปรับปรุงเว็บไซต์ให้ติดอันดับสูงในการค้นหาผ่านเสิร์ชเอนจิน เพื่อเพิ่มจำนวนผู้เข้าชมแบบธรรมชาติ

---

SEO（搜索引擎优化）是提高网站在搜索引擎结果中可见度的实践，以吸引更多自然流量。"""
    },
    "coding_chinese": {
        "keywords": ["编程（Coding）", "编程", "什么是编程"],
        "content": """Coding is the process of writing instructions in a programming language to create software, applications, or websites.

---

การเขียนโค้ดคือกระบวนการเขียนคำสั่งด้วยภาษาคอมพิวเตอร์เพื่อสร้างซอฟต์แวร์ แอปพลิเคชัน หรือเว็บไซต์

---

编程是用编程语言编写指令的过程，用于创建软件、应用程序或网站。"""
    },
    "phone_chinese": {
        "keywords": ["话号码是什么", "电话号码", "你的电话号码"],
        "content": """You can contact us at +66 (0)81 854 4291

---

คุณสามารถติดต่อฉันได้ที่ +66 (0)81 854 4291

---

您可以拨打 +66 (0)81 854 4291 联系我们。"""
    },
    "email_chinese": {
        "keywords": ["子邮件是什么", "电子邮件", "你的电子邮件"],
        "content": """You can email me through cblue.thailand@gmail.com

---

คุณสามารถส่งอีเมลถึงฉันได้ที่ cblue.thailand@gmail.com

---

您可以发送邮件至 cblue.thailand@gmail.com。"""
    },
    "green_architecture_th": {
        "keywords": ["สถาปัตยกรรมสีเขียวคืออะไร"],
        "content": """สถาปัตยกรรมสีเขียวคือแนวคิดการออกแบบอาคารที่คำนึงถึงสิ่งแวดล้อม เน้นการประหยัดพลังงาน ลดของเสีย และสร้างความยั่งยืน"""
    },
    "cctv": {
        "keywords": ["what is cctv", "cctv คือ", "cctv คืออะไร", "กล้องวงจรปิด", "กล้องวงจรปิดคืออะไร", "什么是cctv", "闭路电视", "闭路电视是什么"],
        "content": """CCTV (Closed-Circuit Television) is a video surveillance system that monitors and records activities in specific areas for security purposes.

---

กล้องวงจรปิดคือระบบเฝ้าระวังด้วยวิดีโอที่ติดตามและบันทึกกิจกรรมในพื้นที่เฉพาะเพื่อวัตถุประสงค์ด้านความปลอดภัย

---

闭路电视是一种视频监控系统，用于监控和记录特定区域的活动以实现安全目的。"""
    },
    "alarm_systems": {
        "keywords": ["what is alarm systems", "what are alarm systems", "alarm systems คือ", "ระบบเตือนภัย", "ระบบเตือนภัยคืออะไร", "什么是报警系统", "报警系统", "报警系统是什么"],
        "content": """Alarm systems are security systems that detect unauthorized entry, fire, or other emergencies and alert users through sounds, notifications, or signals.

---

ระบบเตือนภัยคือระบบรักษาความปลอดภัยที่ตรวจจับการบุกรุก ไฟไหม้ หรือเหตุฉุกเฉินอื่นๆ และแจ้งเตือนผู้ใช้ผ่านเสียง การแจ้งเตือน หรือสัญญาณ

---

报警系统是检测未经授权进入、火灾或其他紧急情况并通过声音、通知或信号提醒用户的安全系统。"""
    },
    "intrusion_detection": {
        "keywords": ["what is intrusion detection", "intrusion detection คือ", "การตรวจจับการบุกรุก", "การตรวจจับการบุกรุกคืออะไร", "什么是入侵检测", "入侵检测", "入侵检测是什么"],
        "content": """Intrusion detection is technology that monitors networks or systems to identify unauthorized access attempts or security breaches.

---

การตรวจจับการบุกรุกคือเทคโนโลยีที่ตรวจสอบเครือข่ายหรือระบบเพื่อระบุความพยายามเข้าถึงโดยไม่ได้รับอนุญาตหรือการละเมิดความปลอดภัย

---

入侵检测是监控网络或系统以识别未经授权的访问尝试或安全漏洞的技术。"""
    },
    "motion_detectors": {
        "keywords": ["what is motion detectors", "what are motion detectors", "motion detectors คือ", "เครื่องตรวจจับการเคลื่อนไหว", "เครื่องตรวจจับการเคลื่อนไหวคืออะไร", "什么是运动探测器", "运动探测器", "运动探测器是什么"],
        "content": """Motion detectors are devices that sense movement in an area and trigger alarms or automated responses for security or automation purposes.

---

เครื่องตรวจจับการเคลื่อนไหวคืออุปกรณ์ที่รับรู้การเคลื่อนไหวในพื้นที่และกระตุ้นสัญญาณเตือนหรือการตอบสนองอัตโนมัติเพื่อความปลอดภัยหรือระบบอัตโนมัติ

---

运动探测器是感应区域内运动并触发警报或自动响应以实现安全或自动化目的的设备。"""
    },
    "motion_sensors": {
        "keywords": ["what is motion sensors", "what are motion sensors", "motion sensors คือ", "เซ็นเซอร์ตรวจจับการเคลื่อนไหว", "เซ็นเซอร์ตรวจจับการเคลื่อนไหวคืออะไร", "什么是运动传感器", "运动传感器", "运动传感器是什么"],
        "content": """Motion sensors are electronic devices that detect physical movement using infrared, microwave, or other technologies to activate lights, alarms, or systems.

---

เซ็นเซอร์ตรวจจับการเคลื่อนไหวคืออุปกรณ์อิเล็กทรอนิกส์ที่ตรวจจับการเคลื่อนไหวทางกายภาพโดยใช้อินฟราเรด ไมโครเวฟ หรือเทคโนโลยีอื่นๆ เพื่อเปิดไฟ สัญญาณเตือน หรือระบบต่างๆ

---

运动传感器是使用红外线、微波或其他技术检测物理运动以激活灯光、警报或系统的电子设备。"""
    },
    "cybersecurity": {
        "keywords": ["what is cybersecurity", "cybersecurity คือ", "ความปลอดภัยทางไซเบอร์", "ความปลอดภัยทางไซเบอร์คืออะไร", "什么是网络安全", "网络安全", "网络安全是什么"],
        "content": """Cybersecurity is the practice of protecting computer systems, networks, and data from digital attacks, unauthorized access, and damage.

---

ความปลอดภัยทางไซเบอร์คือการปฏิบัติในการปกป้องระบบคอมพิวเตอร์ เครือข่าย และข้อมูลจากการโจมตีทางดิจิทัล การเข้าถึงโดยไม่ได้รับอนุญาต และความเสียหาย

---

网络安全是保护计算机系统、网络和数据免受数字攻击、未经授权访问和损坏的实践。"""
    },
    "data_protection": {
        "keywords": ["what is data protection", "data protection คือ", "การปกป้องข้อมูล", "การปกป้องข้อมูลคืออะไร", "什么是数据保护", "数据保护", "数据保护是什么"],
        "content": """Data protection refers to measures and practices to safeguard sensitive information from unauthorized access, corruption, or loss.

---

การปกป้องข้อมูลคือมาตรการและแนวปฏิบัติในการปกป้องข้อมูลที่ละเอียดอ่อนจากการเข้าถึงโดยไม่ได้รับอนุญาต การเสียหาย หรือการสูญหาย

---

数据保护是保护敏感信息免受未经授权访问、损坏或丢失的措施和实践。"""
    },
    "network_security": {
        "keywords": ["what is network security", "network security คือ", "ความปลอดภัยของเครือข่าย", "ความปลอดภัยของเครือข่ายคืออะไร", "什么是网络安全", "网络安全"],
        "content": """Network security is the protection of computer networks from intrusions, attacks, and unauthorized access through firewalls, encryption, and monitoring.

---

ความปลอดภัยของเครือข่ายคือการปกป้องเครือข่ายคอมพิวเตอร์จากการบุกรุก การโจมตี และการเข้าถึงโดยไม่ได้รับอนุญาตผ่านไฟร์วอลล์ การเข้ารหัส และการตรวจสอบ

---

网络安全是通过防火墙、加密和监控保护计算机网络免受入侵、攻击和未经授权访问。"""
    },
    "identity_access_management": {
        "keywords": ["what is identity & access management", "what is identity and access management", "identity & access management คือ", "identity and access management คือ", "การจัดการตัวตนและการเข้าถึง", "การจัดการตัวตนและการเข้าถึงคืออะไร", "什么是身份和访问管理", "身份和访问管理", "身份和访问管理是什么"],
        "content": """Identity & access management (IAM) refers to systems and policies that control who can access resources and verify user identities in an organization.

---

การจัดการตัวตนและการเข้าถึงคือระบบและนโยบายที่ควบคุมว่าใครสามารถเข้าถึงทรัพยากรและตรวจสอบตัวตนของผู้ใช้ในองค์กร

---

身份和访问管理是控制谁可以访问资源并验证组织中用户身份的系统和策略。"""
    },
    "bms": {
        "keywords": ["what is bms", "bms คือ", "bms คืออะไร", "ระบบบริหารจัดการอาคาร", "ระบบบริหารจัดการอาคารคืออะไร", "什么是bms", "楼宇管理系统"],
        "content": """BMS (Building Management System) is a computer-based control system that monitors and manages building facilities like HVAC, lighting, and security.

---

ระบบบริหารจัดการอาคาร (BMS) คือระบบควบคุมที่ใช้คอมพิวเตอร์ซึ่งตรวจสอบและจัดการสิ่งอำนวยความสะดวกของอาคาร เช่น ระบบปรับอากาศ แสงสว่าง และความปลอดภัย

---

楼宇管理系统（BMS）是基于计算机的控制系统，用于监控和管理建筑设施，如暖通空调、照明和安全。"""
    },
    "mechanical": {
        "keywords": ["what is mechanical", "mechanical คือ", "ระบบเครื่องกล", "ระบบเครื่องกลคืออะไร", "什么是机械系统", "机械系统", "机械系统是什么"],
        "content": """Mechanical systems involve physical machinery and equipment, including HVAC, elevators, and other moving components in buildings.

---

ระบบเครื่องกลคือระบบที่เกี่ยวข้องกับเครื่องจักรและอุปกรณ์ทางกายภาพ รวมถึงระบบปรับอากาศ ลิฟต์ และส่วนประกอบที่เคลื่อนไหวอื่นๆ ในอาคาร

---

机械系统涉及物理机械和设备，包括暖通空调、电梯和建筑物中的其他移动部件。"""
    },
    "electrical": {
        "keywords": ["what is electrical", "electrical คือ", "ระบบไฟฟ้า", "ระบบไฟฟ้าคืออะไร", "什么是电气系统", "电气系统", "电气系统是什么"],
        "content": """Electrical systems distribute and control electrical power throughout a building, including wiring, panels, and electrical equipment.

---

ระบบไฟฟ้าคือระบบที่กระจายและควบคุมพลังงานไฟฟ้าทั่วทั้งอาคาร รวมถึงสายไฟ แผงควบคุม และอุปกรณ์ไฟฟ้า

---

电气系统是在整个建筑物中分配和控制电力的系统，包括布线、配电板和电气设备。"""
    },
    "plumbing": {
        "keywords": ["what is plumbing", "plumbing คือ", "ระบบประปา", "ระบบประปาคืออะไร", "什么是管道系统", "管道系统", "管道系统是什么"],
        "content": """Plumbing systems manage water supply, drainage, and sewage in buildings through pipes, fixtures, and related equipment.

---

ระบบประปาคือระบบที่จัดการน้ำประปา ระบบระบายน้ำ และน้ำเสียในอาคารผ่านท่อ อุปกรณ์ และอุปกรณ์ที่เกี่ยวข้อง

---

管道系统是通过管道、固定装置和相关设备管理建筑物中的供水、排水和污水的系统。"""
    },
    "fire_protection": {
        "keywords": ["what is fire protection", "fire protection คือ", "ระบบป้องกันอัคคีภัย", "ระบบป้องกันอัคคีภัยคืออะไร", "什么是消防系统", "消防系统", "消防系统是什么"],
        "content": """Fire protection refers to systems and measures designed to detect, prevent, and suppress fires, including alarms, sprinklers, and fire extinguishers.

---

ระบบป้องกันอัคคีภัยคือระบบและมาตรการที่ออกแบบมาเพื่อตรวจจับ ป้องกัน และดับไฟ รวมถึงสัญญาณเตือน สปริงเกลอร์ และเครื่องดับเพลิง

---

消防系统是设计用于检测、预防和扑灭火灾的系统和措施，包括警报器、喷淋系统和灭火器。"""
    },
    "power_control": {
        "keywords": ["what is power control", "power control คือ", "ระบบควบคุมพลังงาน", "ระบบควบคุมพลังงานคืออะไร", "什么是电源控制", "电源控制", "电源控制是什么"],
        "content": """Power control refers to systems that regulate and manage electrical power distribution, voltage, and consumption in buildings or facilities.

---

ระบบควบคุมพลังงานคือระบบที่ควบคุมและจัดการการกระจายพลังงานไฟฟ้า แรงดันไฟฟ้า และการใช้พลังงานในอาคารหรือสิ่งอำนวยความสะดวก

---

电源控制是调节和管理建筑物或设施中电力分配、电压和消耗的系统。"""
    },
    "lighting_control": {
        "keywords": ["what is lighting control", "lighting control คือ", "ระบบควบคุมแสงสว่าง", "ระบบควบคุมแสงสว่างคืออะไร", "什么是照明控制", "照明控制", "照明控制是什么"],
        "content": """Lighting control refers to automated systems that manage lighting levels, schedules, and energy efficiency through sensors, timers, and smart controls.

---

ระบบควบคุมแสงสว่างคือระบบอัตโนมัติที่จัดการระดับแสง ตารางเวลา และประสิทธิภาพการใช้พลังงานผ่านเซ็นเซอร์ ตัวจับเวลา และการควบคุมอัจฉริยะ

---

照明控制是通过传感器、定时器和智能控制管理照明水平、时间表和能源效率的自动化系统。"""
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

def normalize_text(text: str) -> str:
    """Normalize text by removing hyphens and extra spaces for better matching"""
    return text.replace('-', ' ').replace('  ', ' ').strip()

def find_relevant_content(query: str) -> str:
    """Find relevant content using keyword matching with synonyms"""
    query_lower = query.lower()
    query_normalized = normalize_text(query_lower)
    lang = detect_language(query)
    matches = []
    
    # Check if query is a single word (no spaces or only one word)
    # If so, treat it as "what is <word>"
    query_words = query_normalized.strip().split()
    is_single_word = len(query_words) == 1
    
    # If single word query, expand it based on language
    if is_single_word:
        single_word = query_words[0]
        if lang == 'th':
            # For Thai, add variations: "word คือ", "word คืออะไร"
            expanded_queries = [single_word, f"{single_word} คือ", f"{single_word} คืออะไร", 
                              f"{single_word}คือ", f"{single_word}คืออะไร"]
        elif lang == 'zh':
            # For Chinese, add variations: "什么是word", "word是什么"
            expanded_queries = [single_word, f"什么是{single_word}", f"{single_word}是什么"]
        else:
            # For English, add "what is word"
            expanded_queries = [single_word, f"what is {single_word}", f"what is a {single_word}",
                              f"what are {single_word}"]
    else:
        expanded_queries = [query_lower, query_normalized]
    
    # Search through all expanded query variations
    for search_query in expanded_queries:
        for topic, data in KNOWLEDGE_BASE.items():
            for keyword in data["keywords"]:
                keyword_lower = keyword.lower()
                keyword_normalized = normalize_text(keyword_lower)
                if keyword_lower in search_query or keyword_normalized in search_query or search_query in keyword_lower:
                    content = extract_language_content(data["content"], lang)
                    if content not in matches:  # Avoid duplicates
                        matches.append(content)
                    break
        if matches:  # If we found matches, stop searching
            break
    
    if matches:
        return "\n\n".join(matches)
    
    fallback = {
        'th': """ขออภัย ฉันไม่พบข้อมูลที่ตรงกับคำถามของคุณ กรุณาลองถามใหม่หรือติดต่อเราที่:
อีเมล: cblue.thailand@gmail.com
โทร: +66 (0)81 854 4291""",
        'zh': """抱歉，我没有找到与您问题相关的信息。请重新提问或联系我们：
邮箱：cblue.thailand@gmail.com
电话：+66 (0)81 854 4291""",
        'en': """Sorry, I couldn't find information matching your question. Please try asking differently or contact us at:
Email: cblue.thailand@gmail.com
Phone: +66 (0)81 854 4291"""
    }
    
    return fallback.get(lang, fallback['en'])
