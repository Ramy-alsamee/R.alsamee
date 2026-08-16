import requests, time, os, platform, secrets, json

def detect_system():
    """اكتشاف نظام التشغيل الحالي."""
    if os.path.exists("/data/data/com.termux/files/usr/bin/bash"):
        return "Termux (Android)"
    try:
        with open("/etc/os-release", "r") as f:
            content = f.read().lower()
            if "kali" in content: return "Kali Linux"
            if "ubuntu" in content: return "Ubuntu Linux"
    except: pass
    return f"Linux ({platform.system()})"

def print_banner(system_name, device_id):
    """طباعة واجهة البرنامج ودليل الربط باللغة العربية."""
    os.system("clear" if os.name != "nt" else "cls")
    
    line = "=" * 70
    print(line)
    print(f"🚀 R.alsamee: جسر المهام الذكي - {system_name}")
    print(line)
    
    print("\n[!] انسخ النص التالي وأرسله لمساعد الذكاء الاصطناعي (ChatGPT/Claude/Manus):")
    print("-" * 70)
    
    integration_note = (
        f"أقوم حالياً بإعداد جسر مهام محلي لبيئة {system_name}.\n"
        f"PROTOCOL ID: {device_id}\n"
        f"إرسال المهام (POST): https://ntfy.sh/{device_id}\n"
        f"استقبال النتائج (GET): https://ntfy.sh/{device_id}-res/json?poll=1\n\n"
        f"ملاحظة أمنية: كل مهمة تتطلب موافقتي اليدوية محلياً قبل التنفيذ."
    )
    print(integration_note)
    print("-" * 70)
    print("\n[تنبيه: لن يتم تنفيذ أي أمر دون موافقتك اليدوية على الشاشة]")
    print(line)

if __name__ == "__main__":
    system_name = detect_system()
    
    print("=" * 60)
    print("إعداد جسر R.alsamee الآمن")
    print("=" * 60)
    
    user_input = input("[?] أدخل معرفاً خاصاً (أو اضغط Enter للحصول على معرف عشوائي): ").strip()
    user_tag = user_input if user_input else secrets.token_hex(6)
    device_id = f"fury-safe-{user_tag}"
    
    print_banner(system_name, device_id)
    print(f"[*] القناة النشطة: {device_id}")
    print("[*] في انتظار المهام... (سيظهر لك طلب موافقة عند وصول أي أمر)\n")
    
    processed_ids = set()
    
    while True:
        try:
            # استخدام poll=1 للانتظار حتى وصول رسالة
            r = requests.get(f"https://ntfy.sh/{device_id}/json?poll=1", timeout=15)
            if r.status_code == 200:
                for line in r.text.strip().split("\n"):
                    if not line: continue
                    msg = json.loads(line)
                    msg_id = msg.get("id")
                    
                    if msg.get("event") == "message" and msg_id not in processed_ids:
                        task = msg.get("message")
                        processed_ids.add(msg_id)
                        
                        print(f"\n[!] مهمة مقترحة جديدة: {task}")
                        choice = input("[?] هل توافق على تنفيذ هذا الأمر محلياً؟ (y/N): ").strip().lower()
                        
                        if choice == 'y':
                            print("[+] جاري التنفيذ...")
                            import subprocess
                            res = subprocess.run(task, shell=True, capture_output=True, text=True)
                            output = res.stdout + res.stderr
                            
                            if not output: output = "(تم التنفيذ بنجاح بدون مخرجات نصية)"
                            
                            print(output)
                            # إرسال النتيجة إلى قناة الردود
                            requests.post(f"https://ntfy.sh/{device_id}-res", data=output.encode("utf-8"), timeout=10)
                            print("[+] تم إرسال النتيجة للذكاء الاصطناعي.")
                        else:
                            print("[-] تم رفض المهمة من قبل المستخدم.")
                            requests.post(f"https://ntfy.sh/{device_id}-res", data="تم رفض المهمة محلياً.".encode("utf-8"), timeout=10)
        
        except KeyboardInterrupt:
            print("\n\n[!] تم إيقاف الجسر. وداعاً!")
            break
        except Exception as e:
            # تجاهل أخطاء الشبكة المؤقتة
            time.sleep(2)
            continue
        
        time.sleep(1)
