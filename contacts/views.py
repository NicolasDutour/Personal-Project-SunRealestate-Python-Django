from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from .models import Contact


def contact(request):
    if request.method == 'POST':
        listing_id = request.POST['listing_id']
        listing = request.POST['listing']
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        message = request.POST['message']
        user_id = request.POST['user_id']
        realtor_email = request.POST['realtor_email']

        if request.user.is_authenticated:
            user_id = request.user.id
            has_contacted = Contact.objects.all().filter(
                listing_id=listing_id, user_id=user_id)
            if has_contacted:
                messages.error(
                    request, "Vous avez déjà envoyé une demande d'information")
                return redirect('/listings/' + listing_id)

        contact = Contact(listing=listing,
                          listing_id=listing_id,
                          name=name, email=email,
                          phone=phone,
                          message=message,
                          user_id=user_id)

        contact.save()

        send_mail(
            "Demande d'information",
            "Demande d'info pour " + listing,
            'dutourn99@gmail.com',
            [realtor_email, 'dutourn99@gmail.com'],
            fail_silently=False
        )

        messages.success(
            request, 'Votre requête a été envoyé, une personne prendra contact rapidement avec vous.')
        return redirect('/listings/' + listing_id)
