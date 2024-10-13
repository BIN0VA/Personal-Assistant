from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives, send_mail
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.template.loader import render_to_string


@receiver(post_save, sender=User)
def welcome(
    sender: User,
    instance: User,
    created: bool,
    **kwargs: dict
) -> None:
    if not created:
        return

    subject = (
        f'Account details for {instance.username} at {settings.PROJECT_NAME} '
        '(pending admin approval)'
    )

    message = (
        f'Thank you for registering at {settings.PROJECT_NAME}. Your '
        'application for an account is currently pending approval. Once it '
        'has been approved, you will receive another email containing '
        'information about how to log in, set your password, and other '
        'details.'
    )

    send_mail(subject, message, settings.DEFAULT_FROM_EMAIL, [instance.email])


before = {}


@receiver(pre_save, sender=User)
def activating(sender: User, instance: User, **kwargs: dict) -> None:
    if instance.pk:
        before[instance.pk] = User.objects.get(pk=instance.pk).is_active


@receiver(post_save, sender=User)
def activation(
    sender: User,
    instance: User,
    created: bool,
    **kwargs: dict
) -> None:
    if not (
        not created and
        not before.get(instance.pk) and
        instance.is_active and
        not instance.last_login
    ):
        return

    email = EmailMultiAlternatives(
        f'Account details for {instance.username} at {settings.PROJECT_NAME} '
        '(approved)',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[instance.email],
    )

    email.content_subtype = 'html'

    message = render_to_string(
        'pa_user/register/email.html',
        {
            'user': instance,
            'project_name': settings.PROJECT_NAME,
        },
    )

    email.attach_alternative(message, 'text/html')

    email.send()
