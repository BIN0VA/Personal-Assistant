from django.shortcuts import render, redirect

from .forms import ContactsForm
from .models import Contact


def main(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/index.html', {'pa_contacts': contacts})


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
