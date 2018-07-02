from django.shortcuts import render

# Create your views here.
def the_mighty_function(request):
    context = {
    'msg': 'Hello World!',
    }
    return render(request, 'homePage.html', context)
