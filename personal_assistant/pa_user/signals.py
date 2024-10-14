from django.conf import settings
from django.contrib.auth.models import User
from django.core.mail import EmailMultiAlternatives
from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from django.template.loader import render_to_string


def send(
    sender: User,
    template: str,
    status: str = 'pending admin approval',
    receiver: User = None
) -> None:
    email = EmailMultiAlternatives(
        f'Account details for {sender.username} at {settings.PROJECT_NAME} '
        f'({status})',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=[(receiver or sender).email],
    )

    email.content_subtype = 'html'

    message = render_to_string(
        f'pa_user/register/email/{template}.html',
        {
            'user': receiver or sender,
            'guest': sender if receiver else None,
            'project_name': settings.PROJECT_NAME,
        },
    )

    email.attach_alternative(message, 'text/html')

    email.send()


@receiver(post_save, sender=User)
def welcome(
    sender: User,
    instance: User,
    created: bool,
    **kwargs: dict
) -> None:
    if created:
        send(instance, 'guest')

        for user in User.objects.filter(is_active=True, is_superuser=True):
            send(instance, 'admin', receiver=user)


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
    if (
        not created and
        not before.get(instance.pk) and
        instance.is_active and
        not instance.last_login
    ):
        send(instance, 'activation', 'approved')
