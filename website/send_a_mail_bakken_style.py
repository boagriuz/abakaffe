#!/usr/bin/python
# Adapted from http://kutuma.blogspot.com/2007/08/sending-emails-via-gmail-with-python.html

import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText

import os


gmail_user = "abakaffenotifier@gmail.com"
gmail_pwd = "nynoregpassord1337"

def mail(to, attach=None):




    #static things
    subject = "Abakaffe Subcribe :)"

    #text = "Thank you for subscribing to Abakaffe =)\n\n You will be notified when fresh good coffe is ready. \n\nBest regards, \n"
    html = """\
            <html>
            <head></head>
            <body>
            <p>Hi!<br>
            Thank you for subscribing to Abakaffe =)<br>
            You will be notified when fresh good coffe is ready.
            Here is the <a href="http://abakaffe.today">link</a> you wanted.
            </p>
            <p>Best regards, <br> </p>
            <br>
            <p>
                <img src="https://49.media.tumblr.com/23b345acdf7f9639bf94bb9bbe8f8191/tumblr_nvu767z9eS1s30ko5o1_500.gif" alt="I need Coffee" height="150" width="250"/>

            <br>
            </p>
            </body>
            </html>
         """

    #
    msg = MIMEMultipart()
    msg['From'] = gmail_user
    msg['To'] = to
    msg['Subject'] = subject

    #part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    #msg.attach(part1)
    msg.attach(part2)
    try:
        if attach:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(open(attach, 'rb').read())
            encoders.encode_base64(part)
            part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(attach))
            msg.attach(part)
        mailServer = smtplib.SMTP("smtp.gmail.com", 587)
        mailServer.ehlo()
        mailServer.starttls()
        mailServer.ehlo()
        mailServer.login(gmail_user, gmail_pwd)
        mailServer.sendmail(gmail_user, to, msg.as_string())
        mailServer.close()


    except smtplib.SMTPConnectError as conn:
        print("An email connection error: ", conn)
    except smtplib.SMTPAuthenticationError as auth:
        print("An email auth error: ", auth)
