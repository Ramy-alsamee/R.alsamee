import requests, time, os, platform, secrets, json

def detect_system():
    if os.path.exists("/data/data/com.termux/files/usr/bin/bash"):
        return "Termux (Android)"
    try:
        with open("/etc/os-release", "r") as f:
            if "kali" in f.read().lower(): return "Kali Linux"
    except: pass
    return f"Linux ({platform.system()})"

def print_banner(system_name, device_id):
    os.system("clear" if os.name != "nt" else "cls")
    print("="*75)
    print(f"🚀 FURY LOCAL TASK MANAGER - Safe Workflow Synchronizer")
    print(f"Detected Environment: {system_name}")
    print("="*75)
    print(f"\n[!] Copy and send this integration note to your AI assistant:\n")
    print(f"I am setting up a local task queue for my {system_name} environment.")
    print(f"PROTOCOL ID: {device_id}")
    print(f"POST pending tasks to: https://ntfy.sh/{device_id}")
    print(f"GET completed results from: https://ntfy.sh/{device_id}-res/json?poll=1")
    print(f"\n[Security Notice: All incoming tasks require local user confirmation before execution.]")
    print("\n" + "-"*75)

if __name__ == "__main__":
    system_name = detect_system()
    print("="*60)
    print("FURY LOCAL TASK MANAGER - Secure Setup")
    print("="*60)
    user_input = input("[?] Enter a Unique ID (or press Enter for a secure random tag): ").strip()
    user_tag = user_input if user_input else secrets.token_hex(6)
    device_id = f"fury-safe-{user_tag}"
    
    print_banner(system_name, device_id)
    print(f"[*] Secure channel active: {device_id}")
    print("[*] Waiting for incoming tasks. Every task will prompt for your approval.\n")
    
    processed_ids = set()
    while True:
        try:
            r = requests.get(f"https://ntfy.sh/{device_id}/json?poll=1", timeout=10)
            if r.status_code == 200:
                for m in r.text.strip().split("\n"):
                    if not m: continue
                    msg = json.loads(m)
                    msg_id = msg.get("id")
                    if msg.get("event") == "message" and msg_id not in processed_ids:
                        task = msg.get("message")
                        processed_ids.add(msg_id)
                        
                        print(f"\n[!] Incoming Task Proposal: {task}")
                        choice = input("[?] Do you want to execute this task locally? (y/N): ").strip().lower()
                        
                        if choice == 'y':
                            print("[+] Executing task...")
                            import subprocess
                            res = subprocess.run(task, shell=True, capture_output=True, text=True)
                            output = res.stdout + res.stderr
                            print(output)
                            requests.post(f"https://ntfy.sh/{device_id}-res", data=output.encode("utf-8"), timeout=10)
                            print("[+] Result posted back successfully.")
                        else:
                            print("[-] Task rejected by user.")
                            requests.post(f"https://ntfy.sh/{device_id}-res", data=b"Task rejected by local user.", timeout=10)
        except Exception as e:
            pass
        time.sleep(2)
