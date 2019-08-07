import requests
mobno=input("enter a no :")
msg=input("enter a message :")
res=requests.post('https://textbelt.com/text',{
    'phone': mobno,
    'message':msg,
    'key': 'textbelt',
 })

result=res.json()
print(result)