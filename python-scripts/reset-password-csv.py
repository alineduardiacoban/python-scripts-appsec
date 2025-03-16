import requests
import sys
import urllib3
import csv

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


proxies = {'http':'http://127.0.0.1:8080', 'https':'http://127.0.0.1:8080'}
headers = {}

def email_employees(s,url):
    result = 0
    requests = 0
    reset_password_url = url + "/path/to/endpoint"
    print("[+] Emailing employees...")
    with open('Emails.csv', 'r', encoding='utf-8-sig') as lines:
        reader = csv.reader(lines)
        for row in reader:
            email = row[0]
            reset_password_data = {"Email":email}
            r = s.post(reset_password_url, json=reset_password_data, headers=headers, verify=False, proxies = proxies)
            requests += 1
            if r.status_code == 200:
                print(f"[+] Email successfully sent for: {email} .")
                result += 1
            else:
                print(f"[-] Email could not be sent for: {email} .")
        if result == requests:
            print("[+] All emails were successfully sent.")
        elif result==0:
            print("[-] No emails could be sent. Try Again.")
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