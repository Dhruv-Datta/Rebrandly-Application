from tkinter import *
import requests
import json


def link_entry_check_input():
    if link_entry.get():
        link_button.config(state=NORMAL)
    else:
        link_button.config(state=DISABLED)


def slashtag_entry_check_input():
    if slashtag_entry.get():
        slashtag_button.config(state=NORMAL)
    else:
        slashtag_button.config(state=DISABLED)


def title_entry_check_input():
    if title_entry.get() or link_entry.get() or slashtag_entry.get():
        title_button.config(state=NORMAL)
    else:
        title_button.config(state=DISABLED)


def link_button_click():
    confirmation_text = Label(app, text="Link Sent", font=normal_font)
    confirmation_text.grid(row=0, column=0, padx=0, pady=(200, 0), sticky='n')

    global original_link
    original_link = link_entry.get()


def slashtag_button_click():
    confirmation_text = Label(app, text="Slashtag Sent", font=normal_font)
    confirmation_text.grid(row=0, column=1, padx=100, pady=(200, 0), sticky='n')

    global slashtag
    slashtag = slashtag_entry.get()


def title_button_click():
    confirmation_text = Label(app, text="Title Sent", font=normal_font)
    confirmation_text.grid(row=0, column=2, padx=0, pady=(200, 0), sticky='n')

    global title
    title = title_entry.get()


def create_rebranded_link():
    try:
        data_for_link = {
            'link': original_link,
            'slashtag': slashtag,
            'title': title
        }
    except NameError:
        data_for_link = {
            'link': original_link,
            'slashtag': slashtag,
            'title': ""
        }
        pass

    linkRequest = {
        "destination": f"{data_for_link['link']}",
        "domain": {"fullName": "cloudtopoffice.info"},
        "slashtag": f"{data_for_link['slashtag']}",
        "title": f"{data_for_link['title']}"
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

        show_rebranded_link = Text(app, height=1, borderwidth=0)
        center_text(show_rebranded_link)
        show_rebranded_link.insert("1.0", f'{link["shortUrl"]}', "center")
        show_rebranded_link.grid(row=1, column=0, padx=0, pady=55, sticky='n', columnspan=3)
        show_rebranded_link.configure(state="disabled")

        link_button.config(state=DISABLED)
        slashtag_button.config(state=DISABLED)
        title_button.config(state=DISABLED)
        rebrand_button.config(state=DISABLED)


def center_text(widget):
    widget.tag_configure("center", justify='center')


app = Tk()
app.title("Rebrandly App")
app.geometry("700x400")

app.rowconfigure([0, 1, 2], weight=1)
app.columnconfigure([0, 1, 2], weight=1)

heading_font = ('Verdana', 13, 'bold')
normal_font = ('Arial', 8)

apptitle = Label(app, text='Rebrandly', font=heading_font)
apptitle.grid(row=0, column=1, sticky='n')

link_label = Label(app, text='Insert Link Below')
link_label.grid(row=0, column=0, padx=10, pady=65, sticky='n')
link_entry = Entry(app, width=20)
link_entry.grid(row=0, column=0, padx=10, pady=95, sticky='n')

slashtag_label = Label(app, text='Insert Slashtag Below')
slashtag_label.grid(row=0, column=1, padx=10, pady=65, sticky='n')
slashtag_entry = Entry(app, width=20)
slashtag_entry.grid(row=0, column=1, padx=10, pady=95, sticky='n')

title_label = Label(app, text='Insert Title Below (Optional)')
title_label.grid(row=0, column=2, padx=10, pady=65, sticky='n')
title_entry = Entry(app, width=20)
title_entry.grid(row=0, column=2, padx=10, pady=95, sticky='n')

link_button = Button(app, text="Confirm Link", padx=30, pady=10, command=link_button_click, state=DISABLED)
link_button.grid(row=0, column=0, padx=10, pady=(130, 0), sticky='n')

slashtag_button = Button(app, text="Confirm Slashtag", padx=30, pady=10, command=slashtag_button_click, state=DISABLED)
slashtag_button.grid(row=0, column=1, padx=10, pady=(130, 0), sticky='n')

title_button = Button(app, text="Confirm Title", padx=30, pady=10, command=title_button_click, state=DISABLED)
title_button.grid(row=0, column=2, padx=10, pady=(130, 0), sticky='n')

rebrand_button = Button(app, text='Rebrand Link', padx=45, command=create_rebranded_link, pady=10, state=DISABLED)
rebrand_button.grid(row=1, column=1, padx=10, pady=10, sticky='s')

link_entry.bind("<KeyRelease>", lambda event: link_entry_check_input())
slashtag_entry.bind("<KeyRelease>", lambda event: slashtag_entry_check_input())
title_entry.bind("<KeyRelease>", lambda event: title_entry_check_input())

link_button.bind("<Button-1>", lambda event: rebrand_button.config(state=NORMAL))
slashtag_button.bind("<Button-1>", lambda event: rebrand_button.config(state=NORMAL))
title_button.bind("<Button-1>", lambda event: rebrand_button.config(state=NORMAL))
rebrand_button.bind("<Button-1>", lambda event: create_rebranded_link())

app.mainloop()
