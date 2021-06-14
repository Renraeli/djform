from django.shortcuts import render
from django.http import HttpResponse
from .forms import TextForm


def index(request):
    if request.method == 'POST':
        form = TextForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['text'])
            return HttpResponse('Done!')
    else:
        form = TextForm()
    return render(request, 'myapp/index.html', {'form': form})
