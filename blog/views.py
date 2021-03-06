from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Contact
from .forms import ContactForm
from django.db.models import Q

def home(request):
	get_contact = Contact.objects.all()
	search_user = request.GET.get('search_user', '')

	if search_user:
		get_contact = Contact.objects.filter(Q(name = search_user) | Q(surname = search_user) | Q(tel_number = search_user))
	else:
		get_contact = Contact.objects.all()
	
	return render(request, 'blog/userlist.html', {'users': get_contact, 'search_user': search_user})

def create_contact(request):
	form = ContactForm(request.POST or None)
	if form.is_valid():
		instance = form.save()
		return HttpResponseRedirect('/')
	context = {
		'form': form
	}
	return render(request, 'blog/create_user.html', context)

def contact_details(request, id):
	contact = Contact.objects.get(id = id)
	context = {
		"contact": contact
	}
	return render(request, 'blog/contact_details.html', context)

def update_contact(request, contact_id):
	contact = get_object_or_404(Contact, id = contact_id)
	form = ContactForm(instance = contact)
	if request.method == 'POST':
		form = ContactForm(request.POST, instance = contact)
		if form.is_valid():
			form.save()
			return HttpResponseRedirect('/contact/' + contact_id)
	context = {
		'form' : form
	}
	return render(request, 'blog/update_contact.html', context)

def delete_contact(request, contact_id):
	contact = get_object_or_404(Contact, id = contact_id)
	if request.method == 'POST':
		contact.delete()
		return HttpResponseRedirect('/')
	context = {'contact': contact}
	return render(request, 'blog/delete_contact.html', context)