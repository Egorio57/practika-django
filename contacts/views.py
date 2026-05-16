from django.contrib import messages
from django.shortcuts import redirect
from django.shortcuts import render

from .forms import ContactForm


def contact_view(request):

    form = ContactForm()

    if request.method == 'POST':

        form = ContactForm(request.POST)

        if form.is_valid():

            form.save()

            messages.success(
                request,
                'Сообщение успешно отправлено.'
            )

            return redirect('contacts:contact')

    context = {
        'form': form
    }

    return render(
        request,
        'contacts/contact.html',
        context
    )