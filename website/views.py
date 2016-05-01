from django.shortcuts import render, HttpResponseRedirect
from update.models import Weight
from highscores.views import get_monthly_alltime, get_statistics
from .models import Subscribe
from .forms import NameForm
import smtplib
import calendar, time
from django.core.mail import send_mail


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


error_msg = None


def subscribe(request):
    # if POST request
    global error_msg

    stat = get_statistics()

    if request.method == 'POST':
        form = NameForm(request.POST)

        # check if valid
        if form.is_valid() and form.form_contains_letters():
            # create timestamp
            # set db fields # process form.cleaned_data


            studmail = form.cleaned_data['studmail'] + "@stud.ntnu.no"
            created = calendar.timegm(time.gmtime())

            # save to database
            sub_obj = Subscribe(studmail=studmail, created=created)
            sub_obj.save()

            # Send the user a notify mail =)

            send_a_mail(studmail)

            error_msg = None

            context = {
                    'form': form,
                    'error_msg': error_msg,
                    'WEIGHT': Weight.objects.get(key=1).weight,
                    'STATISTICS': stat,

                }

            return HttpResponseRedirect("/subscribe/", context)


        else:

            error_msg = ' - Form is invalid'

            # redirect to new site

    # if GET request
    else:

        form = NameForm()

    context = {

        'form': form,
        'error_msg': error_msg,
        'WEIGHT': Weight.objects.get(key=1).weight,
        'STATISTICS': stat,

    }

    return render(request, "website/subscribe.html", context)

    # forms.py => views => models.py => db.sqlite3


### EMAIL SECTION HERE ####
### see settings for email stuff ###


def send_a_mail(email_receiver):
    global error_msg

    subject = "Abakaffe Subcribe :)"
    html_msg = """\
            <html>
            <meta charset="ISO-8859-1">
            <head></head>
            <body>
            <p>Hi!<br>
            Thank you for subscribing to Abakaffe =)<br>
            You will be notified when fresh good coffee is ready.<br>
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


    try:

        send_mail(subject, message="", html_message=html_msg, from_email="abakaffenotifier@gmail.com", recipient_list=[email_receiver],
                  fail_silently=False)

    except smtplib.SMTPException as e:

        error_msg = "Failed to send email"
