from django.shortcuts import render, redirect, HttpResponseRedirect
from update.models import Weight
from highscores.views import get_monthly_alltime, get_statistics
from .models import Subscribe
from datetime import datetime
from .forms import NameForm
import smtplib
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
import os


def index(request, template="website/index.html"):
    subscribe(request)
    stat = get_statistics()
    context = {'WEIGHT': Weight.objects.get(key=1).weight, 'STATISTICS': stat}
    return render(request, template, context)


def highscore(request, template="website/highscore.html"):
    monthly, alltime = get_monthly_alltime()
    stat = get_statistics()
    context = {'MONTHLY': monthly, 'ALLTIME': alltime, 'STATISTICS': stat}
    return render(request, template, context)


def about(request, template="website/about.html"):
    return render(request, template)


def subscribe(request):
    # if POST request
    error_msg = None

    if request.method == 'POST':
        form = NameForm(request.POST)

        # check if valid
        if form.is_valid():
            # create timestamp
            now = datetime.now()

            # set db fields # process form.cleaned_data

            studmail = form.cleaned_data['studmail'] + "@stud.ntnu.no"
            created = str(now.hour) + ":" + str(now.minute)

            # save to database
            sub_obj = Subscribe(studmail=studmail, created=created)
            sub_obj.save()

            # Send the user a notify mail =)
            try:
                mail(studmail)
                context = {
                    'form': form,
                    'error_msg': error_msg,

                }

                return HttpResponseRedirect("/subscribe/", context)

            except smtplib.SMTPException as e:

                error_msg = "Failed to send notify email: ", e

        else:

            error_msg = 'Form is invalid'

            # redirect to new site

    # if GET request
    else:

        form = NameForm()

    context = {

        'form': form,
        'error_msg': error_msg,

    }

    return render(request, "website/index.html", context)

    # forms.py => views => models.py => db.sqlite3


### EMAIL SECTION HERE ####


gmail_user = "abakaffenotifier@gmail.com"
gmail_pwd = "nynoregpassord1337"


def mail(to, attach=None):
    # static things
    subject = "Abakaffe Subcribe :)"

    # text = "Thank you for subscribing to Abakaffe =)\n\n You will be notified when fresh good coffe is ready. \n\nBest regards, \n"
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
                ABAKAFFE

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

    # part1 = MIMEText(text, 'plain')
    part2 = MIMEText(html, 'html')

    # msg.attach(part1)
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
