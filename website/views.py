from django.shortcuts import render, HttpResponseRedirect, redirect
from update.models import Weight
from highscores.views import get_monthly_alltime, get_statistics
from .models import Subscribe
from .forms import NameForm
import smtplib
import calendar, time
from django.core.mail import EmailMessage


def index(request, template="website/index.html"):

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


    stat = get_statistics()
    error_msg = None
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            if form.cleaned_data['studmail'] != '':
                if form.form_contains_letters():
                    studmail = form.cleaned_data['studmail'] + "@stud.ntnu.no"
                    created = calendar.timegm(time.gmtime())

                    # save to database
                    sub_obj = Subscribe(studmail=studmail, created=created)
                    sub_obj.save()

                    # Send the user a notify mail =)
                    sendMail(studmail)


                    return redirect("/subscribe/")

                else:
                    error_msg = "- Username can only contain letters [a-zA-Z]"
            else:
                error_msg = "nothing"
        else:
            error_msg = "- Form data is invalid"
    else:

        form = NameForm()

    # if GET request


    context = {

        'form': form,
        'error_msg': error_msg,
        'WEIGHT': Weight.objects.get(key=1).weight,
        'STATISTICS': stat,

    }

    return render(request, "website/subscribe.html", context)


### see settings for email stuff ###

def sendMail(email_receiver, content=None):
    # if "to" is not a list of e-mails but a string
    # it will be converted to a single item list

    if content:
        subject = "Coffee is ready :)"
        subtype = "text"
        message = content
        sendTemplate(subject, message, subtype, email_receiver)

    else:
        subject = "Abakaffe Subcribe :)"
        html_msg = """\
            <html>
            <meta charset="ISO-8859-1">
            <head></head>
            <body>
            <p>Hi!<br>
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
        """
        sendTemplate(subject, html_msg, "html", email_receiver)


def sendTemplate(subject, content, subtype,receiver):

    if not isinstance(receiver, list):
        receiver = receiver.strip().split()
    try:
        email = EmailMessage(subject, content, "abakaffenotifier@gmail.com", receiver)
        email.content_subtype = subtype
        email.send()
    except smtplib.SMTPException as e:
        print("Email ERROR:", e)
