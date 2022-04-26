from django.shortcuts import render, redirect


from audi_our_love_shop_project.contacts.forms import ContactsForm


def contacts(request):
    if request.method == 'POST':
        form = ContactsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        if request.user.is_authenticated:
            form = ContactsForm(initial={'email': request.user.email})
        else:
            form = ContactsForm()

    context = {
        'form': form,
    }
    return render(request, 'contacts/contacts.html', context)

