from django.shortcuts import render


def home(request):
    return render(request, 'catalog/home.html')


def contacts(request):
    if request.method == 'POST':
        name = request.POST.get('email')
        user_message = request.POST.get('message')
        print(f'{name}: {user_message}')
    return render(request, 'catalog/contacts.html')
