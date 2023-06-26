# Rebrandly Integration Documentation

This Documentation is split into 3 sections: 

* API Integration
* Rebrandly Application GUI
     1. What the application does
     2. How to setup the python scripts to work on your computer
* Rebrandly Text Integration
     1. What the application does
     2. How to setup the python scripts to work on your computer


## API Integration
Before making any exe files or attempting to start implementing this code, you will need to change the Rebrandly API integration in the code. In order to do this you must have a valid subscription with Rebrandly.

In the code, under the function `create_rebranded_link()`, look for the following code snipet:

```python
linkRequest = {
   "destination": f"{data_for_link['link']}",
   "domain": {"fullName": "domain_goes_here"},
   "slashtag": f"{data_for_link['slashtag']}",
   "title": f"{data_for_link['title']}"
}
```
In the `"domain"` section of the hash table, replace `"domain_goes_here"` with your company domain. DO NOT REPLACE `"fullName": `!

```python
requestHeaders = {
   "Content-type": "application/json",
   "apikey": "apikey_goes_here",
   "workspace": "workspace_id_goes_here",
}
```
In the `"apikey"` and `"workspace"` section of this hashtable, replace `"apikey_goes_here"` with your api key and `"workspace_id_goes_here"` with your workspace id. DO NOT REPLACE `"application/json"`!

If you do not know how to get your API Key and Workspace ID, refer to the Rebrandly API Link: https://developers.rebrandly.com/docs


## Rebrandly App GUI
### Application Function
The Rebrandly Application is a Python script that provides a graphical user interface (GUI) for rebranding and shortening URLs using the Rebrandly API. It allows you to customize their links with custom slashtags and titles, making them more visually appealing. 

**You must have a valid Rebrandly Account and access your api key and workspace id!**

1. Users can also enter a custom slashtag, which is a unique identifier added to the shortened URL.
2. Optionally, users can provide a title for the rebranded link. This title will not actually show up in your rebranded link, it is for the Rebrandly Website when
   you hover over the link.
3. Once the necessary information is entered, users can click the corresponding buttons to confirm the link, slashtag, and title.
4. Finally, users can click the "Rebrand Link" button to create the rebranded URL using the Rebrandly API. The rebranded link is displayed on the GUI.

**The App-GUI-Test.py is a file for developers. It is to freely test the GUI functions and understand if any changes to the code will work without requesting multiple API calls (as there is only a certain number of links you can generate in rebrandly per month).
App-GUI-Test.py is NOT USED in the final product. This documentation is for the Rebrandly-App-GUI.py**


### Setup exe file
To make this python file run on any computer, you can convert it into an exe. You would do this with the following code:

```cmd
pip install pyinstaller

cd C:Path\to\file\Rebrandly-App-GUI.py

pyinstaller --onefile --noconsole Rebrandly-App-GUI.py
```

This will create a new exe file in a DICT folder in the folder you run the python code in. You can move this exe file anywhere you would like.
I would recommend creating a shortcut for this application so that whenever you would like to create a new link it is instantanously opened with a hotkey. 
Once you have the exe file ready, thats all the steps completed and you can start using the GUI freely!


## Rebrandly Text Integration
### Application Function
The Rebrandly Text Integration makes rebranding links easier by using the Rebrandly API to push requests out easier using a text file to input the link and slashtag quickly. There will be a .txt file to paste the link into, and then you run an .exe file. This exe file will convert the previous link into a new link.

Before using the Rebrandly Text Integration, put setup.py and Rebrandly-Text-Integration.py into 1 folder.

Using the Rebrandly App:
1. Open the Rebrandly Input text file
2. Input your link that needs to be converted on the 1st line of text
3. Input your slashtag on the 2nd line of text
4. Run the Rebrandly Application and the new link should generate on the 3rd line

*DO NOT USE THE FOLLOWING FOR SLASHTAGS:
- All Capital Letters
- Any Special Characters (#, $, &, etc...)

For ease of use the following workflow is the reccomended:
1. Create a shortcut for "Rebrandly App.exe"
2. Create a shortcut for "Rebrandly Input.txt"
3. Click properties of both shortcuts and select a shortcut key

Anytime you would like to generate a new link, just click the shortcut key for Rebrandly Input and
type in the link and slashtag. Then press the shortcut key for the Rebrandly App and have your link
generated immediately.

If you would like to clean up the folder as there are a lot of files in it, you can either create a
new folder inside of the original folder to store the shortcuts, setup, and readme files or hide them
with the properties menu.

### Setup exe file
To make this python file run on any computer, you can convert it into an exe. You would do this with the following code:

```cmd
pip install pyinstaller

cd C:Path\to\folder\with\script

pyinstaller --onefile --noconsole Rebrandly-Text-Integration.py
pyinstaller --onefile --noconsole setup.py
```

This will create 2 new exe file in a DICT folder in the folder you run the python code in. You can move this exe file anywhere you would like.

When you make the new exe files, put them into a folder together and run the setup.exe and you will be all set to start using the Rebrandly Text Integration!

