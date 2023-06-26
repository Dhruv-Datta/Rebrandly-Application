import pyperclip
import requests
import json

old_link = pyperclip.paste()

slashtag = input('Enter Slashtag: ')

linkRequest = {
    "destination": f"{old_link}",
    "domain": {"fullName": "domain_goes_here"},
    "slashtag": f"{slashtag}",
}

requestHeaders = {
    "Content-type": "application/json",
    "apikey": "apikey_goes_here",
    "workspace": "workspace_id_goes_here",
}

r = requests.post(
    "https://api.rebrandly.com/v1/links",
    data=json.dumps(linkRequest),
    headers=requestHeaders,
)

if r.status_code == requests.codes.ok:
    link = r.json()
    print(f'Long URL was {link["destination"]}, short URL is {link["shortUrl"]}')

pyperclip.copy(link["shortUrl"])
