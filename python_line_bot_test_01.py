#!/usr/local/bin/python3
import requests
url = 'https://notify-api.line.me/api/notify'
token = 'DB0yEn8zezvk2MxmRXPhamHd4ZfbdFeP91pHfeXMa02'
headers = {'content-type':'application/x-www-form-urlencoded','Authorization':'Bearer '+token}
msg = 'Hello LINE Notify'
r = requests.post(url, headers=headers, data = {'message':msg})
print(r.text)