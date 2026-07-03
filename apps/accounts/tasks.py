
from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


@shared_task(
    autoretry_for=(Exception,),
    retry_backoff=True,
    max_retries=5,
)
def send_verification_email_task(
    email,
    username,
    verification_link,
):
    html_content = render_to_string(
        "emails/verify_email.html",
        {
            "username": username,
            "verification_link": verification_link,
        },
    )

    message = EmailMultiAlternatives(
        subject="Verify Your Account",
        body="Please verify your account.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[email],
    )

    message.attach_alternative(
        html_content,
        "text/html",
    )

    message.send()