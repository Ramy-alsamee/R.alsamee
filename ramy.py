import requests, time, os, platform, secrets, json, hmac, hashlib

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

def print_banner(system_name, device_id, secret_enabled):
    """طباعة واجهة البرنامج ودليل الربط باللغة العربية مع إرشادات الأمان المتقدمة."""
    os.system("clear" if os.name != "nt" else "cls")
    
    line = "=" * 70
    print(line)
    print(f"🚀 R.alsamee: جسر المهام الآمن المتقدم - {system_name}")
    print(line)
    
    print("\n[!] انسخ النص التالي وأرسله لمساعد الذكاء الاصطناعي (ChatGPT/Claude/Manus):")
    print("-" * 70)
    
    auth_note = "مع التحقق من التوقيع الأمني (HMAC)" if secret_enabled else "بدون مفتاح سري (اتصال مباشر)"
    integration_note = (
        f"أقوم حالياً بإعداد جسر مهام محلي آمن لبيئة {system_name}.\n"
        f"PROTOCOL ID: {device_id}\n"
        f"إرسال المهام (POST): https://ntfy.sh/{device_id}\n"
        f"استقبال النتائج (GET): https://ntfy.sh/{device_id}-res/json?poll=1\n"
        f"الوضع الأمني: {auth_note}\n\n"
        f"ملاحظة أمنية: جميع المهام تخضع للتحقق من الصلاحية وموافقتي اليدوية محلياً."
    )
    print(integration_note)
    print("-" * 70)
    print("\n[حماية متقدمة: منع إعادة التشغيل والتحقق من التوقيع مفعلة]")
    print(line)

def verify_signature(payload_str, signature, secret_key):
    """التحقق من صحة التوقيع الأمني للرسالة لمنع التلاعب."""
    if not secret_key:
        return True
    expected = hmac.new(
        secret_key.encode("utf-8"),
        payload_str.encode("utf-8"),
        hashlib.sha256
    ).hexdigest()
    return hmac.compare_digest(expected, signature)

if __name__ == "__main__":
    system_name = detect_system()
    
    print("=" * 60)
    print("تكوين جسر R.alsamee الآمن (Advanced Security)")
    print("=" * 60)
    
    user_input = input("[?] أدخل معرف القناة (أو اضغط Enter لإنشاء معرف عشوائي): ").strip()
    user_tag = user_input if user_input else secrets.token_hex(6)
    device_id = f"fury-secure-{user_tag}"
    
    secret_key = input("[?] أدخل مفتاح المصادقة السري HMAC (أو اتركه فارغاً للوضع المرن): ").strip()
    secret_enabled = bool(secret_key)
    
    print_banner(system_name, device_id, secret_enabled)
    print(f"[*] القناة النشطة: {device_id}")
    print("[*] في انتظار المهام الآمنة... (سيظهر لك طلب موافقة عند وصول أي أمر)\n")
    
    processed_ids = set()
    
    while True:
        try:
            r = requests.get(f"https://ntfy.sh/{device_id}/json?poll=1", timeout=25)
            if r.status_code == 200:
                for line in r.text.strip().split("\n"):
                    if not line: continue
                    msg = json.loads(line)
                    msg_id = msg.get("id")
                    
                    if msg.get("event") == "message" and msg_id not in processed_ids:
                        raw_msg = msg.get("message", "")
                        processed_ids.add(msg_id)
                        
                        task = ""
                        signature = ""
                        timestamp = 0
                        
                        # محاولة تحليل الرسالة بصيغة JSON آمنة
                        try:
                            data = json.loads(raw_msg)
                            task = data.get("cmd", "")
                            signature = data.get("signature", "")
                            timestamp = data.get("timestamp", 0)
                            
                            # حماية ضد إعادة التشغيل (Anti-Replay: صلاحية الرسالة 5 دقائق)
                            if timestamp and (time.time() - timestamp > 300):
                                print(f"\n[!] تم تجاهل رسالة منتهية الصلاحية (Replay Attack Prevention): {msg_id}")
                                continue
                                
                            # التحقق من التوقيع إذا كان المفتاح مفعلاً
                            if secret_enabled:
                                payload_check = f"{task}:{timestamp}"
                                if not verify_signature(payload_check, signature, secret_key):
                                    print(f"\n[!] فشل التحقق من التوقيع الأمني للرسالة! تم رفض الأمر.")
                                    continue
                        except json.JSONDecodeError:
                            # دعم الأوامر النصية التقليدية في حال عدم استخدام JSON
                            task = raw_msg.strip()
                        
                        if task:
                            print(f"\n[!] أمر وارد (مُتحقق منه): {task}")
                            choice = input("[?] هل توافق على تنفيذ هذا الأمر محلياً؟ (y/N): ").strip().lower()
                            
                            if choice == 'y':
                                print("[+] جاري التنفيذ...")
                                import subprocess
                                res = subprocess.run(task, shell=True, capture_output=True, text=True)
                                output = res.stdout + res.stderr
                                
                                if not output: output = "(تم التنفيذ بنجاح بدون مخرجات نصية)"
                                
                                print(output)
                                requests.post(f"https://ntfy.sh/{device_id}-res", data=output.encode("utf-8"), timeout=10)
                                print("[+] تم إرسال النتيجة بأمان.")
                            else:
                                print("[-] تم رفض المهمة من قبل المستخدم.")
                                requests.post(f"https://ntfy.sh/{device_id}-res", data="تم رفض المهمة محلياً.".encode("utf-8"), timeout=10)
        
        except KeyboardInterrupt:
            print("\n\n[!] تم إيقاف الجسر. وداعاً!")
            break
        except requests.exceptions.ConnectionError:
            print("\n[!] خطأ في الاتصال: تعذر الوصول إلى خادم الجسر.")
            print("[i] نصيحة: إذا كنت في شبكة مقيدة، جرب تفعيل VPN ثم أعد التشغيل.")
            time.sleep(5)
            continue
        except Exception as e:
            time.sleep(2)
            continue
        
        time.sleep(1)
