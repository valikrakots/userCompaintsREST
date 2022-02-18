from django.core.mail import send_mail

from celery import shared_task


@shared_task()
def send_email_task(user_email):
    send_mail("Thank you!",
              "You have registered",
              'runfastgo77@gmail.com',
              [user_email])
    return None