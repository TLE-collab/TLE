from django.shortcuts import render


def index(request):
    context_dict = {"some": 'haha'}
    return render(request, 'app/index.html', context=context_dict)

# Create your views here.
