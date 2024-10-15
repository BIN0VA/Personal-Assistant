from django.contrib.auth.decorators import login_required
from django.db.models.functions import ExtractMonth, ExtractDay
from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone

from pa_core.views import overview
from .forms import ContactsForm
from .models import Contact


@login_required
def main(request):
    contacts = Contact.objects.filter(user=request.user)

    if (
        (request.GET.get('type', 'contacts').lower() in ('', 'contacts')) and
        (query := request.GET.get('query'))
    ):
        contacts_search = contacts.filter(
            Q(name__icontains=query) |
            Q(address__icontains=query) |
            Q(phone__icontains=query) |
            Q(email__icontains=query)
        )
    else:
        contacts_search = contacts

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
        contacts.annotate(
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
                birthday_this_year = contact.birthday \
                    .replace(year=today.year + 1)
            else:
                birthday_this_year = contact.birthday.replace(year=today.year)

            if today <= birthday_this_year <= end_date:
                upcoming_birthdays_filtered.append(
                    (birthday_this_year, contact),
                )

    upcoming_birthdays_filtered.sort(key=lambda x: x[0])
    sorted_contacts = [contact for _, contact in upcoming_birthdays_filtered]

    return overview(
        request,
        'contacts',
        contacts_search,
        {
            'upcoming_birthdays': sorted_contacts,
            'days': days,
            'tabs': tabs,
        },
        'person',
        'Contacts',
    )


@login_required
def create(request):
    if request.method == 'POST':
        form = ContactsForm(request.POST, user=request.user)

        if form.is_valid():
            contact = form.save(commit=False)
            contact.user = request.user
            contact.save()

            return redirect('pa_contacts:home')

        return render(request, 'pa_contacts/add.html', {'form': form})

    return render(request, 'pa_contacts/add.html', {'form': ContactsForm()})


@login_required
def delete(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id, user=request.user)
    contact.delete()
    return redirect('pa_contacts:home')


@login_required
def edit(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id, user=request.user)

    if request.method == 'POST':
        form = ContactsForm(request.POST, instance=contact, user=request.user)

        if form.is_valid():
            form.save()

            return redirect('pa_contacts:home')
    else:
        form = ContactsForm(instance=contact, user=request.user)

    return render(request, 'pa_contacts/edit.html', {'form': form})
