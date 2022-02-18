# Spoil Wordle With Python!
This program sends an email to a list of receivers that contains the subject of your choice and the wordle of the day in the body. Credit to Jacob Lipman for doing the HTML stuff.
### Requirements
1. Pip install stmplib, bs4, requests, ssl, and ast. 
2. Set up your gmail account for control by the script: I suggest using a burner for security reasons.
3. This program requires that you turn on less secure apps in your google settings. Instructions can be found here: https://hotter.io/docs/email-accounts/secure-app-gmail/. 
### Running
1. replace pythonbot062@gmail.com with your low security email
2. define receivers as a list of all emails you would like to send the message to
3. if you want a different subject, replace CS CLASS NEEDS YOUR HELP. 
4. run python wordgrabber.py in your bash terminal. 
5. write your email password for the low security account
6. press enter to send! 
7. Enjoy! 
### To-Do
1. Integrate with google sheets api for the purpose of getting emails.
2. Make a gui.
3. Create a BCC option instead of individual emails. 
