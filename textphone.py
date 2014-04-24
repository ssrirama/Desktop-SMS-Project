__author__ = 'Tyler'
__author__ = 'ssrirama'
from tkinter import *
from twilio.rest import TwilioRestClient

master = Tk()
toBeCalled = {}
m1 = PanedWindow(master)
m1.pack(fill=BOTH, expand=1)

left = Label(m1, text="Text or call?")
m1.add(left)

m2 = PanedWindow(m1, orient=VERTICAL)
m1.add(m2)

top = Entry(m2, text="Enter Name")
m2.add(top)
top.focus_set()

bottom = Entry(m2, text="Enter Phone Number")
m2.add(bottom)

#****************************************************************************************
# DO NOT DELETE THIS : https://www.twilio.com/labs/twimlets/echo
# The aforementioned URL is used to create a FREE web URL for the Twilio app to refer to.
#****************************************************************************************

def button1click():
    toBeCalled[top.get()] = bottom.get()
    account_sid = ""
    auth_token = ""
    client = TwilioRestClient(account_sid, auth_token)
    if top.get() == "text" or top.get() == "Text":
        toSend = bottom.get()
        if bottom.get() == "" :
            toSend = "Invalid"
        else:
            toSend = bottom.get()

        message = client.messages.create(body=toSend,
                                         to="6784673448",
                                         from_="+16789054735")
    else:
        if top.get() == "call" or top.get() == "Call":
            call = client.calls.create(url="http://twimlets.com/echo?Twiml=%3CResponse%3E%0A%3CPlay%3Ehttp%3A%2F%2Fdemo.twilio.com%2Fdocs%2Fclassic.mp3%3C%2FPlay%3E%0A%3C%2FResponse%3E&",
                                       to="6784673448",
                                       from_="+16789054735")

button1 = Button(master, text="Done", command=button1click)
button1.pack()
m1.add(button1)

mainloop()
