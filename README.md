# FURY ULTIMATE - Universal AI-to-System Bridge 🚀

**FURY ULTIMATE** هو جسر برمجي متطور وآمن يربط بين تطبيقات الذكاء الاصطناعي (مثل ChatGPT, Claude, Manus) وبين بيئة نظامك المحلية (**Termux** أو **Kali Linux**). يتيح لك هذا النظام التحكم الكامل في جهازك وتنفيذ الأوامر البرمجية والأمنية عبر واجهة دردشة بسيطة وبأمان تام وددون الحاجة لإعدادات خادم معقدة.

---

## الميزات الرئيسية 🌟
- **دعم متعدد الأنظمة (Multi-Platform):** يكتشف السكريبت تلقائياً ما إذا كنت تعمل على بيئة **Termux (Android)** أو توزيعة **Kali Linux (PC)**.
- **خصوصية كاملة وعزل كامل (Full Privacy & Isolation):** يعتمد على معرفات فريدة (Unique IDs / Tags) يختارها المستخدم بنفسه أو يتم توليدها بشكل عشوائي آمن، لضمان عدم تداخل البيانات بين المستخدمين.
- **بدون فتح منافذ (Zero-Config / No Port Forwarding):** لا يتطلب إعدادات شبكية معقدة أو استخدام أدوات نفق (Tunneling) مزعجة، بل يعتمد على قنوات تواصل سحابية خفيفة وآمنة (`ntfy.sh`).
- **واجهة تعليمية جاهزة:** يولد تلقائياً دليلاً تشغيلياً واضحاً ومباشراً بصيغة احترافية لكي يفهَم الذكاء الاصطناعي طبيعة البروتوكول وينفذ الأوامر بدقة.

---

## كيف يعمل النظام؟ ⚙️
1. **التهيئة:** عند تشغيل السكريبت، يقوم بالتعرف على نظام التشغيل ويطلب منك إدخال **معرف خاص (Unique ID)** أو توليد معرف آمن.
2. **البروتوكول:** يعرض لك السكريبت رسالة تعليمات تقنية تحتوي على عناوين API مخصصة لمعرفك.
3. **المزامنة العكسية (Reverse Polling):**
   - يقوم الذكاء الاصطناعي بإرسال الأوامر كطلب `POST` إلى القناة المخصصة.
   - يقوم السكريبت المحلي بسحب الأمر، تنفيذه محلياً عبر صدفة النظام (`subprocess`), وإرسال النتيجة كطلب `POST` إلى قناة الردود (`-res`).

---

## دليل التثبيت والاستخدام 🛠️

### 1. المتطلبات الأساسية
تأكد من تثبيت لغة **Python 3** ومكتبة **requests**:
```bash
# على Termux
pkg update && pkg install python -y
pip install requests

# على Kali Linux / Debian / Ubuntu
sudo apt update && sudo apt install python3 python3-pip -y
pip3 install requests
```

### 2. التشغيل
قم بتحميل السكريبت `FURY_ULTIMATE.py` ثم شغله:
```bash
python3 FURY_ULTIMATE.py
```

### 3. الربط مع الذكاء الاصطناعي
- أدخل معرفك الخاص عندما يطلبه السكريبت.
- انسخ النص (الدليل التقني) الذي سيظهر لك في الشاشة.
- الصق النص في محادثتك مع الذكاء الاصطناعي (مثل ChatGPT أو Claude أو Manus).
- ابدأ بإعطاء الأوامر واستلم النتائج فوراً!

---

## إخلاء مسؤولية ⚖️
هذه الأداة مخصصة حصرياً للأغراض التعليمية، وتطوير السكربتات الشخصية، واختبار الأمان المشروع في بيئاتك المحلية. المطور لا يتحمل أي مسؤولية قانونية عن أي استخدام غير قانوني أو ضار لهذه الأداة.

---

# FURY ULTIMATE - Universal AI-to-System Bridge 🚀

**FURY ULTIMATE** is an advanced, secure bridge connecting AI assistants (ChatGPT, Claude, Manus) to your local system environment (**Termux** or **Kali Linux**). It allows you to seamlessly control your local device and execute authorized shell commands through a chat interface without complex server configurations.

## Key Features 🌟
- **Multi-Platform Support:** Automatically detects Termux (Android) or Kali Linux (PC).
- **Strict Privacy & Isolation:** Utilizes custom user-defined Unique IDs or secure random tags to completely isolate data channels.
- **Zero-Config:** No port forwarding, VPNs, or complex tunneling required.
- **AI-Ready Protocol:** Automatically generates clear, structured instructions for AI models.

## Installation & Usage 🛠️

### 1. Prerequisites
Ensure Python 3 and `requests` are installed:
```bash
pip install requests
```

### 2. Running the Tool
```bash
python3 FURY_ULTIMATE.py
```

### 3. Connection Steps
- Enter your unique identifier when prompted.
- Copy the generated technical protocol text.
- Paste it into your AI assistant session.
- Begin executing commands remotely and securely!

## Disclaimer ⚖️
This tool is intended for educational purposes, personal workflow automation, and authorized security testing only. The developer assumes no liability for misuse.

## License
MIT License
