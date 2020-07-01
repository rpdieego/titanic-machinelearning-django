from django.shortcuts import render, redirect
from .models import PassengerDB
from .forms import PassengerForm
from django.contrib import messages

def home(request):

    #access Passenger DB
    if request.method == 'POST':
        form = PassengerForm(request.POST or None)

        if form.is_valid():
            form.save()
            all_items = PassengerDB.objects.all()
            messages.success(request, ('New passenger added'))
            return render(request, 'index_pM.html', {'all_items':all_items})

    else:

        all_items = PassengerDB.objects.all()
        return render(request, 'index_pM.html', {'all_items':all_items})

def delete(request, list_id):

    item = PassengerDB.objects.get(pk=list_id)
    item.delete()
    messages.success(request, ('Item deleted ..'))
    return redirect('pM_home')


def posts(request, pk_test):
    post = PassengerDB.objects.get(pk=pk_test)
    return render(request, 'posts.html', {'post':post})
