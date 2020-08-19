#Read Me : Below were set as ENV varibles for the OS to read and execute as requested in CLI Mode or Using Python to Execute with User_input
#C:\Program Files\Oracle\VirtualBox
#C:\Program Files (x86)\Google\Chrome\Application
#C:\Program Files\VideoLAN\VLC
#C:\Program Files\Sublime Text 3
#C:\Program Files (x86)\WinSCP

import os
import getpass
import smtplib, ssl
while True:
        user_in = input("chat with me with your requirememnt : ")
        if (("run" in user_in or "execute" in user_in)) and (("player" in user_in or "media" in user_in)):
            os.system("vlc")
        elif ("run" in user_in) and ("google" in user_in) or ("chrome" in user_in):
            os.system("chrome")
        elif ("run" in user_in) and (("notepad" in user_in or "editor" in user_in)):
            os.system("notepad")    
        elif (("run" in user_in or "execute" in user_in or "open" in user_in or "start" in user_in)) and (("virtualbox" in user_in or "vm" in user_in )):
            os.system("VirtualBox")
        elif (("run" in user_in or "execute" in user_in or "open" in user_in or "start" in user_in)) and (("sublimetext" in user_in or "sublime text" in user_in or "sublimetext editor" in user_in)):
            os.system("sublime_text")
        elif (("run" in user_in or "execute" in user_in or "open" in user_in or "start" in user_in)) and (("winscp" in user_in )):
            os.system("winscp") 
        elif ("exit" in user_in) or ("quit" in user_in):
            break
        else:
             print("Requested program is not registered within our System")

#print("Do you want to send email to the notifier : ")
email = input(" Do you want to send email to the Notifier : ")
if email == 'no':
    print("exit")
    
elif email == 'yes':
    port = 465
    sender_email = "<Change with your email-Id>>"
    receiver_email = input("Type receiver_email : ")
    #password = getpass.getpass(prompt='Type your password and press enter: ') 
    password = input("Type your password and press enter:")

#Reference: https://realpython.com/python-send-email/#getting-started
#Enable less secure app in your gmail setting - https://myaccount.google.com/lesssecureapps?pli=1
#Install the smtplib if not present by default -> #pip install smtplib
#import smtplib, ssl
    from email.mime.text import MIMEText
    from email.mime.multipart import MIMEMultipart

    message = MIMEMultipart("alternative")
    message["Subject"] = input("Enter your Subject : ")
    message["From"] = sender_email
    message["To"] = receiver_email

# Create the plain-text and HTML version of your message
    text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
    html = """\
<html>
  <body>
     
    <p>Hi<br>
       How are you?<br>
       <a href="https://www.youtube.com/channel/UCtY-JhEZ3iPLtozWGgd2efQ">IIEC_connect</a> 
       has many great tutorials.
    </p>
  </body>
</html>
"""

# Turn these into plain/html MIMEText objects
    part1 = MIMEText(text, "plain")
    part2 = MIMEText(html, "html")

# Add HTML/plain-text parts to MIMEMultipart message
# The email client will try to render the last part first
    message.attach(part1)
    message.attach(part2)

# Create secure connection with server and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
        server.login(sender_email, password)
        server.sendmail( sender_email, receiver_email, message.as_string()
        )

"""
#Usage of OS to chat and get the required output -Basic
import os
user_in = input("chat with me with your requirememnt : ")
if (("run" in user_in or "execute" in user_in)) and (("player" in user_in or "media" in user_in)):
    os.system("vlc")
elif ("run" in user_in) and ("google" in user_in) or ("chrome" in user_in):
    os.system("chrome")
elif ("run" in user_in) and (("notepad" in user_in or "editor" in user_in)):
    os.system("notepad")
else:
     print("not supported")
     
    
"""
    
"""
     
#If Condition Checking

i = 1
if i >= 10:
    print("hi")
else:
    print("not valid")
    
#While condition checking
while i<=10:
    print("hi")
    i = i + 1
     
x = 2
while x > 10:
    print("ok")
else:
    print("not ok")

    
"""
    
