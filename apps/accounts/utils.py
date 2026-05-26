# from django.core.mail import send_mail
# from django.conf import settings
# from django.core.mail import EmailMultiAlternatives
# from django.template.loader import render_to_string


# def send_verification_email(user, token, verification_link):

#     html_content = render_to_string(
#     "emails/verify_email.html",
#     {
#         "verification_link": verification_link,
#         "username": user.username
#     }
#     )

#     email = EmailMultiAlternatives(
#         subject="Verify Your Account",
#         body="Verify your account",
#         from_email=settings.DEFAULT_FROM_EMAIL,
#         to=[user.email]
#     )

#     email.attach_alternative(html_content, "text/html")

#     email.send()

#     # send_mail(
#     #     subject="Verify Your Account",
#     #     message=f"""
#     #         Hello {user.username},

#     #         Please verify your account by clicking the link below:

#     #         {verification_link}

#     #         If you did not create this account, ignore this email.
#     #     """,
#     #     from_email=settings.DEFAULT_FROM_EMAIL,
#     #     recipient_list=[user.email],
#     # )

from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


def send_verification_email(user, verification_link):

    html_content = render_to_string(
        "emails/verify_email.html",
        {
            "username": user.username,
            "verification_link": verification_link,
        }
    )

    email = EmailMultiAlternatives(
        subject="Verify Your Account",
        body="Please verify your account.",
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[user.email],
    )

    email.attach_alternative(html_content, "text/html")

    email.send()