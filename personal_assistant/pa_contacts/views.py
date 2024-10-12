from django.db.models.functions import ExtractMonth, ExtractDay
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from pa_core.views import overview
from .forms import ContactsForm
from .models import Contact


def main(request):
    contacts = Contact.objects.all()
    today = timezone.now().date()
    days_param = request.GET.get('days', 7)

    tabs = [
        (7, 'Week'),
        (30, 'Month'),
        (90, '3 months'),
    ]

    try:
        days = int(days_param)
        if days <= 0:
            days = 7
    except ValueError:
        days = 7

    end_date = today + timezone.timedelta(days=days)

    upcoming_birthdays_filtered = []

    upcoming_birthdays = (
        Contact.objects.annotate(
            birth_month=ExtractMonth('birthday'),
            birth_day=ExtractDay('birthday')
        )
    )

    for contact in upcoming_birthdays:
        if contact.birthday:
            birth_month = contact.birth_month
            birth_day = contact.birth_day

            if (
                birth_month < today.month or
                (birth_month == today.month and birth_day < today.day)
            ):
                birthday_this_year = contact.birthday.replace(year=today.year + 1)
            else:
                birthday_this_year = contact.birthday.replace(year=today.year)

            if today <= birthday_this_year <= end_date:
                upcoming_birthdays_filtered.append((birthday_this_year, contact))

    upcoming_birthdays_filtered.sort(key=lambda x: x[0])
    sorted_contacts = [contact for _, contact in upcoming_birthdays_filtered]

    return overview(
        request,
        'contacts',
        contacts,
        {
            'upcoming_birthdays': sorted_contacts,
            'days': days,
            'tabs': tabs,
        },
        'Contacts',
    )


def create(request):

    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='pa_contacts:main')
        else:
            return render(request, 'pa_contacts/add_contact.html', {'form': form})

    return render(request, 'pa_contacts/add_contact.html', {'form': ContactsForm()})


def delete(request, contact_id):
    Contact.objects.get(pk=contact_id).delete()
    return redirect(to='pa_contacts:main')


def edit(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    
    if request.method == 'POST':
        form = ContactsForm(request.POST, instance=contact)
        if form.is_valid():
            form.save()
            return redirect('pa_contacts:main')
    else:
        form = ContactsForm(instance=contact)
    
    return render(request, 'pa_contacts/edit.html', {'form': form})
