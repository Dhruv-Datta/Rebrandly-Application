import requests
import json
import os

file_path = "Rebrandly Input.txt"


def read_link_request_from_user():
    with open(file_path, 'r') as file_contents:
        global qwlink
        global qwdocnumber

        file_contents = file_contents.readlines()

        try:
            if len(file_contents) >= 2:
                qwlink = file_contents[0].strip()
                qwdocnumber = file_contents[1].strip()
            else:
                raise IndexError
        except IndexError:
            print("Error: Please Input BOTH the link and the document number on the 2nd Line")


def create_rebranded_link():
    if len(qwlink) > 1 and len(qwdocnumber) > 1:
        linkRequest = {
            "destination": "{}".format(qwlink)
            , "domain": {"fullName": "domain_goes_here"}
            , "slashtag": "{}".format(qwdocnumber)
        }

        requestHeaders = {
            "Content-type": "application/json",
            "apikey": "apikey_goes_here",
            "workspace": ""workspace_id_goes_here""
        }

        r = requests.post("https://api.rebrandly.com/v1/links",
                          data=json.dumps(linkRequest),
                          headers=requestHeaders)

        if r.status_code == requests.codes.ok:
            link = r.json()
            print(f'Long URL was {link["destination"]}, short URL is {link["shortUrl"]}')

            global rebranded_link
            rebranded_link = link["shortUrl"]

            print("Success! Rebranded Link was created")
    else:
        print("Error: No link provided")


def write_link_on_text_file():
    with open(file_path, 'a') as write_file:
        write_file.write('\n')
        write_file.write(rebranded_link)


def open_file():
    os.startfile(file_path)


def main():
    read_link_request_from_user()
    create_rebranded_link()
    write_link_on_text_file()
    open_file()


if __name__ == '__main__':
    main()
