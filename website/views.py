from django.shortcuts import render, redirect, render_to_response
from update.models import Weight
from highscores.views import get_monthly_alltime, get_statistics
from .models import Subscribe
from datetime import datetime
from .forms import NameForm
from .send_a_mail_bakken_style import mail
import smtplib


def index(request, template="website/index.html"):
    subscribe(request)
    stat = get_statistics()
    context = {
        'WEIGHT': Weight.objects.get(pk=1).weight,
        'STATISTICS': stat,
        'popup': True,
    }


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

    if (request.method == 'POST'):
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

                return redirect('index.html', context)

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

    return render_to_response(request, 'website/index.html', context)

    # forms.py => views => models.py => db.sqlite3
