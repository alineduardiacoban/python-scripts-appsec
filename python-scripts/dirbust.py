import requests
import sys
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http':'http://127.0.0.1:8080', 'https':'http://127.0.0.1:8080'}

def bruteforce_directories(url):
    print("[+] Brute forcing directories...")
    with open("rockyou.txt", 'r') as directories:
        for directory in directories:
            bf_directory = directory.strip('\n')
            r = requests.Session()
            dirbust_url = url + f"/path/to/{bf_directory}"
            req = r.get(dirbust_url, verify = False)
            if req.status_code != 404:
                print(f"[+] Directory found: {directory}. ")
                with open ('directory.txt', 'a') as g:
                    g.write(directory)
        
def main():
    if len(sys.argv) != 2:
        print("[+] Usage: %s <url>" % sys.argv[0])
        print(["[+] Example: %s www.example.com" % sys.argv[0]])
        sys.exit(-1)

    url = sys.argv[1]
    bruteforce_directories(url)

if __name__ == "__main__":
    main()