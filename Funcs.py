import smtplib, ssl
from bs4 import BeautifulSoup
import requests
import ast
from datetime import date

def emailsend(receiver_email, sender_email, password, subject, msg):
	"""
	given the receivers email, password, subject, and message, send an email to the receiver.
	"""
	smtp_server = "smtp.gmail.com"
	messagebody = ("wordle for today is " + (msg))
	message = 'Subject: {}\n\n{}'.format(subject, messagebody)
	port = 587 
	context = ssl.create_default_context()
	with smtplib.SMTP(smtp_server, port) as server:
		server.starttls(context=context)
		server.login(sender_email, password)
		server.sendmail(sender_email, receiver_email, message)

def get_words():
    """
    Get a list of all possible wordle words: credit to chad master Jacob Lipman for this beautiful, beautiful piece of code. 
    """
    response = requests.get('https://www.nytimes.com/games/wordle/main.18740dce.js') #get data with an http request
    html_doc = response.text #get the raw html tex of the page (string)
    soup = BeautifulSoup(html_doc, 'html.parser') #create a BeautifulSoup object

    words = html_doc[html_doc.find("Ma=")+3:html_doc.find("Oa=")-1]

    possible_words = ast.literal_eval(words)

    return possible_words
    
def wordOfDay():
	"""
	Determine the word of the day using a predetermined starting point. Messing with any of the values below will make it inaccurate
	"""
    today = date.today()
    old = date(2022, 2, 17)
    dateSince = (today - old)
    daySince = (dateSince.days)
    integer = (243 + daySince)
    List = get_words()
    return List[integer]
