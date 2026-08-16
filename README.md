# R.alsamee — FURY Local Task Manager

أداة تعليمية لإدارة **مقترحات المهام المحلية** من بيئات Termux وKali Linux. تكتشف الأداة البيئة التي تعمل فيها، تنشئ معرّفاً خاصاً للقناة، وتعرض المهام الواردة للمستخدم قبل تنفيذها. لا تنفّذ الأداة أي مهمة واردة تلقائياً؛ يجب أن يوافق المستخدم محلياً على كل مهمة.

> **تنبيه أمني:** قناة `ntfy.sh` العامة ليست نظام مصادقة أو سرية بحد ذاتها. استخدم معرّفاً عشوائياً لا يتضمن اسمك أو بريدك، ولا ترسل كلمات مرور أو مفاتيح أو بيانات شخصية عبر القناة. راجع كل مهمة قبل الموافقة عليها، ولا تمنح الأداة صلاحيات Root إلا عند الضرورة القصوى.

## المزايا

| الميزة | الوصف |
|---|---|
| اكتشاف البيئة | يميّز بين Termux على Android وKali Linux، مع دعم Linux العام كخيار احتياطي. |
| معرّف مستقل | يطلب معرّفاً من المستخدم أو يولّد وسمًا عشوائياً لتقليل تداخل القنوات. |
| موافقة محلية | يعرض كل مهمة واردة وينتظر قرار المستخدم قبل التنفيذ. |
| واجهة بسيطة | يطبع المقترح والنتيجة في الطرفية المحلية. |
| لا توجد بيانات مضمنة | لا يحتوي المشروع على معرف جهاز أو كلمة مرور أو مفتاح خاص مسبقاً. |

## آلية العمل

عند بدء `ramy.py`، يكتشف السكربت النظام ويطلب معرّفاً خاصاً. بعد ذلك يراقب قناة الرسائل الخاصة بالمعرّف عبر HTTPS. عندما تصل رسالة، يعرضها كمقترح مهمة ويسأل المستخدم: `Do you want to execute this task locally? (y/N)`. عند اختيار `y` فقط، تُنفّذ المهمة في البيئة المحلية وتُرسل النتيجة إلى قناة الردود. عند أي إجابة أخرى تُرفض المهمة.

هذه الآلية **ليست اتصالاً مباشراً أو تفويضاً للذكاء الاصطناعي**، ولا تعني أن الطرف البعيد موثوق. المستخدم المحلي هو صاحب القرار النهائي، ويجب عليه التحقق من كل أمر قبل الموافقة.

## المتطلبات

يتطلب المشروع Python 3 ومكتبة `requests`.

### Termux

نفّذ الأوامر التالية داخل Termux:

```bash
pkg update -y
pkg upgrade -y
pkg install python -y
python -m pip install --upgrade pip
python -m pip install requests
```

إذا كان الملف موجوداً في مجلد التنزيلات، انسخه إلى مجلد Termux ثم شغّله:

```bash
termux-setup-storage
cp ~/storage/downloads/ramy.py ~/
python ramy.py
```

وإذا نزّلت المشروع من GitHub مباشرة:

```bash
pkg install git -y
git clone https://github.com/Ramy-alsamee/R.alsamee.git
cd R.alsamee
python ramy.py
```

### Kali Linux أو Debian أو Ubuntu

نفّذ الأوامر التالية:

```bash
sudo apt update
sudo apt install -y python3 python3-pip git
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
python -m pip install requests
```

بعد ذلك نزّل المشروع وشغّله:

```bash
git clone https://github.com/Ramy-alsamee/R.alsamee.git
cd R.alsamee
python3 ramy.py
```

إذا كنت تستخدم البيئة الافتراضية، فعّلها أولاً من داخل مجلد المشروع:

```bash
source .venv/bin/activate
python ramy.py
```

## دليل الربط السريع بالذكاء الاصطناعي 🤖

لربط الأداة بـ ChatGPT أو Claude أو Manus أو أي مساعد ذكاء اصطناعي آخر، اتبع الخطوات البسيطة التالية:

1.  **بدء الجلسة:** شغّل السكربت على جهازك (`python ramy.py`).
2.  **تحديد الهوية:** أدخل معرّفاً خاصاً بك أو اضغط Enter لتوليد واحد عشوائي.
3.  **نسخ البروتوكول:** سيظهر لك إطار يحتوي على نص تقني (Integration Note). **قم بنسخ هذا النص بالكامل.**
4.  **تفعيل المساعد:** اذهب إلى محادثة الذكاء الاصطناعي، وقم بلصق النص وأرسله. سيفهم المساعد فوراً كيفية التواصل مع جهازك.
5.  **التنفيذ:** اطلب من الذكاء الاصطناعي القيام بأي مهمة (مثلاً: "اعرض ملفات النظام"). سيظهر لك طلب الموافقة على شاشة جهازك. اكتب `y` للموافقة.

بهذه الطريقة، يتحول الذكاء الاصطناعي إلى واجهة تحكم ذكية لنظامك مع الحفاظ على خصوصيتك وأمانك.

## الاستخدام

بعد تشغيل السكربت، أدخل معرّفاً عشوائياً أو اضغط Enter لتوليد معرّف عشوائي. انسخ بيانات البروتوكول التي تظهر لك فقط إذا كنت تفهم مخاطر القنوات العامة. لا تشارك معرّفك مع أشخاص غير موثوقين، لأن أي شخص يعرف المعرّف قد يحاول نشر رسالة في القناة. عند ظهور مهمة، اقرأها كاملة؛ اكتب `y` فقط إذا كنت متأكداً من الأمر وهدفه، واضغط Enter لرفضها في أي حالة أخرى.

لإيقاف السكربت، استخدم:

```text
Ctrl+C
```

## كيفية تحديث الأداة 🔄

إذا قمت بتثبيت الأداة مسبقاً عبر `git clone` وتريد الحصول على آخر التحديثات والتحسينات، ما عليك سوى الدخول إلى مجلد المشروع وتنفيذ أمر التحديث:

```bash
cd R.alsamee
git pull origin main
```
سيقوم هذا الأمر بجلب أحدث نسخة من السكربت والدليل تلقائياً.

## ما الذي لا يفعله المشروع؟

لا يقوم المشروع بتجاوز كلمات المرور، أو كسر تشفير Wi‑Fi، أو استغلال ثغرات، أو تثبيت برمجيات خبيثة، أو منح صلاحيات Root تلقائياً. كما لا ينبغي استخدامه لإدارة أجهزة أشخاص آخرين دون موافقة صريحة منهم.

## حل مشكلات الشبكة والـ VPN 🌐

في بعض الحالات، قد تمنع شبكة الإنترنت المحلية أو جدار الحماية الاتصال بخوادم الجسر (`ntfy.sh`). إذا لاحظت أن الأداة لا تستقبل الأوامر أو لا ترسل النتائج:

1.  **استخدام VPN:** قم بتفعيل تطبيق VPN على هاتفك (لـ Termux) أو جهازك (لـ Kali) ثم أعد تشغيل السكربت. هذا غالباً ما يحل مشكلة الحجب.
2.  **تحقق من الاتصال:** تأكد من قدرتك على فتح موقع `https://ntfy.sh` في المتصفح.

## استكشاف الأخطاء

إذا ظهر الخطأ `ModuleNotFoundError: No module named 'requests'`، أعد تثبيت المكتبة داخل البيئة نفسها:

```bash
python3 -m pip install requests
```

إذا لم تصل الرسائل، تحقق من اتصال الإنترنت واسم القناة، وتأكد من أن السكربت لا يزال يعمل. تذكّر أن القنوات العامة قد تتعرض للتأخير أو الحجب أو الرسائل القديمة، لذلك لا تعتمد عليها لنقل أسرار أو أوامر حساسة.

إذا رفض Termux الوصول إلى مجلد التنزيلات، نفّذ `termux-setup-storage` مرة واحدة ووافق على الإذن. إذا رفض Kali إنشاء بيئة افتراضية، تحقق من تثبيت حزمة `python3-venv`:

```bash
sudo apt install -y python3-venv
```

## الترخيص

هذا المشروع مرخّص بموجب MIT License. وهو مخصص للتعليم، وأتمتة المهام الشخصية، والاختبار المصرّح به فقط. يتحمل المستخدم مسؤولية الأوامر التي يوافق على تنفيذها والبيئة التي يشغّل فيها الأداة.

## حقوق الملكية

حقوق الطبع والنشر © 2026 **رامي السامعي (Ramy Al-Samee)**. لا تمثل أسماء FURY Developer أو أي اسم تجاري سابق مالك الحقوق لهذا المشروع. يُرجى الرجوع إلى ملف `LICENSE` لمعرفة شروط استخدام MIT.

## English summary

Copyright © 2026 **رامي السامعي (Ramy Al-Samee)**. Please refer to `LICENSE` for the MIT License terms.

`ramy.py` is an educational local task manager for Termux, Kali Linux, and compatible Linux environments. It detects the runtime environment, creates a per-user channel identifier, polls for task proposals, and requires explicit local approval before executing a proposal. It uses Python 3 and `requests`.

Install on Termux:

```bash
pkg update -y && pkg upgrade -y
pkg install python git -y
python -m pip install requests
git clone https://github.com/Ramy-alsamee/R.alsamee.git
cd R.alsamee
python ramy.py
```

Install on Kali/Debian/Ubuntu:

```bash
sudo apt update
sudo apt install -y python3 python3-pip python3-venv git
python3 -m venv .venv
source .venv/bin/activate
python -m pip install requests
git clone https://github.com/Ramy-alsamee/R.alsamee.git
cd R.alsamee
python3 ramy.py
```

Review every incoming proposal locally. Do not send secrets through a public relay, do not run the program as root unless absolutely necessary, and use the tool only on systems you own or are explicitly authorized to administer.

## References

[1]: https://github.com/Ramy-alsamee/R.alsamee "R.alsamee repository"
[2]: https://docs.python.org/3/library/venv.html "Python venv documentation"
[3]: https://docs.ntfy.sh/ "ntfy documentation"
[4]: https://termux.dev/en/ "Termux official website"
[5]: https://www.kali.org/docs/ "Kali Linux documentation"
### Sources:
- [1] [R.alsamee repository](https://github.com/Ramy-alsamee/R.alsamee)
- [2] [Python venv documentation](https://docs.python.org/3/library/venv.html)
- [3] [ntfy documentation](https://docs.ntfy.sh/)
- [4] [Termux official website](https://termux.dev/en/)
- [5] [Kali Linux documentation](https://www.kali.org/docs/)

> ملاحظة: استخدم هذا المشروع فقط في أجهزة تملكها أو لديك تصريح صريح لإدارتها.
