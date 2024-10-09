from django.shortcuts import render, redirect
from django.utils import timezone
from django.db.models import Q
from django.db.models.functions import ExtractMonth, ExtractDay


from .forms import ContactsForm
from .models import Contact


def main(request):
    contacts = Contact.objects.all()
    today = timezone.now().date()
    days = int(request.GET.get('days', 7))
    current_month = today.month
    current_day = today.day

    upcoming_birthdays = (
        Contact.objects.annotate(
            birth_month=ExtractMonth('birthday'),
            birth_day=ExtractDay('birthday')
        )
        .filter(
            Q(birth_month=current_month, birth_day__gte=current_day) |
            Q(birth_month__gt=current_month)
        )
        .order_by('birth_month', 'birth_day')
    )

    upcoming_birthdays_filtered = []
    for contact in upcoming_birthdays:
        birthday_this_year = contact.birthday.replace(year=today.year)
        days_until_birthday = (birthday_this_year - today).days

        if 0 <= days_until_birthday <= days:
            upcoming_birthdays_filtered.append(contact)

    return render(request, 'contacts/index.html', {
        'pa_contacts': contacts,
        'upcoming_birthdays': upcoming_birthdays_filtered,
        'days': days,
    })


def create(request):

    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='pa_contacts:main')
        else:
            return render(request, 'contacts/add_contact.html', {'form': form})

    return render(request, 'contacts/add_contact.html', {'form': ContactsForm()})


def delete(request, contact_id):
    Contact.objects.get(pk=contact_id).delete()
    return redirect(to='pa_contacts:main')
