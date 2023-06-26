import pyperclip
import requests
import json

old_link = pyperclip.paste()

slashtag = input('Enter Slashtag: ')

linkRequest = {
    "destination": f"{old_link}",
    "domain": {"fullName": "cloudtopoffice.info"},
    "slashtag": f"{slashtag}",
}

requestHeaders = {
    "Content-type": "application/json",
    "apikey": "cb004ceb552346a4830acec9593e3157",
    "workspace": "26c9957d52284f7f950c0791ab6520c4",
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
