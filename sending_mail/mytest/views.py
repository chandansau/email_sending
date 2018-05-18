from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from mytest.forms import ContactForm
from django.conf import settings
from django.core.mail import send_mail


# Create your views here.
def index(request):
    response = HttpResponse()

    response.write("<a href=\"contact\"><font color=red>Contact Us</font></a>")
    return response


def contact(request):
    form_class = ContactForm(request.POST or None)
    if form_class.is_valid():
        subject = 'Thank you for Contacting us'
        messege = 'Your messege: ' + request.POST.get('content')
        from_email = settings.EMAIL_HOST_USER
        usermail = request.POST.get('contact_email')
        to_list = [usermail, settings.EMAIL_HOST_USER]
        send_mail(subject, messege, from_email, to_list, fail_silently=False)
        return HttpResponseRedirect('thankyou')

    return render(request, 'form.html', {'form': form_class})


def thankyou(request):
    response = HttpResponse()
    response.write('<body bgcolor=silver><center><h1><font color =red>Thanks for contacting us .</font><br><font color=blue>we just sent an email to you<blue></h1></center></body>')
    return response
