import requests
resp = requests.post('https://textbelt.com/otp/generate', {
  'phone': '7799556080',
  'userid': 'myuser@site.com',
  'key': 'example_otp_key',
})
print(resp.json())