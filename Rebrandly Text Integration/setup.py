def create_readme():
    with open('readme.txt', 'w') as readme_file:
        readme_file.write("""Rebrandly Integration Documentation
-----------------------------------
Before using the Rebrandly App, put Rebrandly Input and Rebrandly App into 1 folder (for ease of access
I reccomend you store the README File and Setup File in the same folder as well.)

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
        """)


def create_input():
    with open('Rebrandly Input.txt', 'w') as input_file:
        input_file.write('')


def main():
    create_readme()
    create_input()


if __name__ == "__main__":
    main()
