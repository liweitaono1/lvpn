from celery import shared_task
from django.conf import settings
from django.core.mail import EmailMultiAlternatives


@shared_task
def send_token(to_email, token):
    try:
        subject = '验证码'
        text_content = '这是一封重要的邮件.'
        html_content = '<p>这是一封<strong>重要的</strong>邮件.</p>'
        from_email = settings.DEFAULT_FROM_EMAIL
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to_email])
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return 'send email success'
    except Exception as e:
        raise Exception('send email failed')


@shared_task
def test():
    return 1
