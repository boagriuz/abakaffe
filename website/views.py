from django.shortcuts import render, redirect
from update.models import Weight
from highscores.views import get_monthly_alltime
from django.core.urlresolvers import reverse
from django.http import HttpResponseRedirect
from .models import Subscribe
from datetime import datetime
from .forms import NameForm
from .send_a_mail_bakken_style import mail
import smtplib

import os

def index(request, template="website/index.html"):
    subscribe(request)
    context = {'WEIGHT': Weight.objects.get(pk=1).weight}
    return render(request, template, context)


def highscore(request, template="website/highscore.html"):
    monthly, alltime = get_monthly_alltime()
    context = {'MONTHLY': monthly, 'ALLTIME': alltime}
    return render(request, template, context)


def about(request, template="website/about.html"):
    return render(request, template)


def subscribe(request):
    # if POST request
    if (request.method == 'POST'):
        form = NameForm(request.POST)

        # check if valid
        if (form.is_valid()):
            # create timestamp
            now = datetime.now()

            # set db fields # process form.cleaned_data

            studmail = form.cleaned_data['studmail'] + "@stud.ntnu.no"
            created = str(now.hour) + ":" + str(now.minute)

            # save to database
            sub_obj = Subscribe(studmail=studmail, created=created)
            sub_obj.save()

            #Send the user a notify mail =)
            try:

                mail(studmail)
                context = {'success': "<h1>Thank you for subscribing!</h1>"}

            except smtplib.SMTPException as e:

                print("Failed to send notify email: ", e)
                context = {'error': "<h1>Failed to send email, plz try again.</h1>"}
        else:
            context = {'error': 'Something bad happend :('}

        # redirect to new site

        return redirect('/subscribe/', context)
    # if GET request
    else:
        form = NameForm()

    return render(request, 'website/base.html', {'form': form})

    # forms.py => views => models.py => db.sqlite3