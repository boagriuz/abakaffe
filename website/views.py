import calendar
import time
from django.core.mail import EmailMessage
from django.shortcuts import render, redirect, HttpResponseRedirect
from highscores.views import get_monthly_alltime, get_statistics
from .forms import NameForm
from update.models import Weight
from .models import Subscribe
import smtplib

error_msg = "nothing"
username = None


def index(request, template="website/index.html"):
    stat = get_statistics()
    global error_msg, username
    error_msg = None

    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['studmail'] != '':
                if form.form_contains_letters():

                    username = form.cleaned_data['studmail']
                    studmail = form.cleaned_data['studmail'] + "@stud.ntnu.no"
                    created = calendar.timegm(time.gmtime())

                    sub_obj = Subscribe(studmail=studmail, created=created)
                    sub_obj.save()

                    # send a notify
                    sendMail(studmail, "")

                    error_msg = "success"
                    # save to database

                else:
                    error_msg = "- Username can only contain letters [a-zA-Z]"
            else:
                error_msg = "nothing"
        else:
            error_msg = "- Form data is invalid"
    else:
        form = NameForm()
        error_msg = "nothing"

    context = {
        'form': form,
        'username': username,
        'error_msg': error_msg,
        'WEIGHT': Weight.objects.get(key=1).weight,
        'STATISTICS': stat,
    }

    return render(request, "website/index.html", context)


def highscore(request, template="website/highscore.html"):
    monthly, alltime = get_monthly_alltime()
    stat = get_statistics()
    context = {'MONTHLY': monthly, 'ALLTIME': alltime, 'STATISTICS': stat}
    return render(request, template, context)


def about(request, template="website/about.html"):
    return render(request, template)


### see settings for email stuff ###
def sendMail(email_receiver, content):
    if content:
        subject = "Coffee is ready :)"
        subtype = "text"
        message = content

    else:
        subject = "Abakaffe Subcribe :)"
        subtype = "html"
        message = """\
            <html>
            <meta charset="ISO-8859-1">
            <head></head>
            <body>
            <p>Hi %s!<br>
            Thank you for subscribing to Abakaffe =)<br>
            You will be notified when fresh coffee is ready.<br>
            Your welcome to <a href="http://abakaffe.today">visit our page</a> at any time! :)

            </p>
            <p>Peace and Love, <br> </p>
            <br>
            <pre>

              ,,                                        ,...  ,...
      db     *MM                 `7MM                 .d' "".d' ""
     ;MM:     MM                   MM                 dM`   dM`
    ,V^MM.    MM,dMMb.   ,6"Yb.    MM  ,MP' ,6"Yb.   mMMmm mMMmm.gP"Ya
   ,M  `MM    MM    `Mb 8)   MM    MM ;Y   8)   MM    MM    MM ,M'   Yb
   AbmmmqMA   MM     M8  ,pm9MM    MM;Mm    ,pm9MM    MM    MM 8M******
  A'     VML  MM.   ,M9 8M   MM    MM `Mb. 8M   MM    MM    MM YM.    ,
.AMA.   .AMMA.P^YbmdP'  `Moo9^Yo..JMML. YA.`Moo9^Yo..JMML..JMML.`Mbmmd'

            </pre>
            </body>
            </html>
        """ % username

    if not isinstance(email_receiver, list):
        receiver = email_receiver.strip().split()
    else:
        receiver = email_receiver

    try:
        email = EmailMessage(subject, message, "abakaffenotifier@gmail.com", receiver)
        email.content_subtype = subtype
        email.send()

    except smtplib.SMTPException as e:
        print("Email ERROR:", e)

