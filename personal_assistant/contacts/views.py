from django.shortcuts import render, redirect, get_object_or_404
from .forms import ContactsForm
from .models import Contact

def main(request):
    contacts = Contact.objects.all()
    return render(request, 'contacts/index.html', {"contacts": contacts})

def add_contact(request):

    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            new_contact = form.save()

            return redirect(to='contacts:main')
        else:
            return render(request, 'contacts/add_contact.html', {'form': form})

    return render(request, 'contacts/add_contact.html', {'form': ContactsForm()})

def detail(request, contact_id):
    contact = get_object_or_404(Contact, pk=contact_id)
    return render(request, 'contacts/detail.html', {"contact": contact})

def delete_contact(request, contact_id):
    Contact.objects.get(pk=contact_id).delete()
    return redirect(to='contacts:main')