import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

headers = {}

def email_employees(s,url):
    result = 0
    requests = 0
    reset_password_url = url + "/path/to/endpoint"
    print("[+] Emailing employees...")
    with open('emails.txt', 'r') as file:
        for line in file:
            email = line.strip()
            reset_password_data = {"Email":email}
            r = s.post(reset_password_url, json=reset_password_data, headers=headers, verify=False)
            requests += 1
            if r.status_code == 200:
                print(f"[+] Email successfully sent for: {email} .")
                result += 1
            else:
                print(f"[-] Email could not be sent for: {email} .")
        if result == requests:
            print("[+] All emails were successfully sent.")
        else:
            print("[-] Not all of the emails were successfully delievered")
            
def main():
    if len(sys.argv) != 2:
        print("[+] Usage: %s <url>" % sys.argv[0])
        print("[+] Example: %s www.example.com" % sys.argv[0])
        sys.exit(-1)

    s= requests.Session()
    url = sys.argv[1]
    email_employees(s, url)

if __name__ == "__main__":
    main()