from django.shortcuts import render
from app.forms import UserForm
from app.models import Algorithm


def index(request):
    context_dict = {"algorithms": Algorithm.objects.all()}
    return render(request, 'app/index.html', context=context_dict)


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request, 'app/register.html',
                  context={'user_form': user_form, 'registered': registered})
