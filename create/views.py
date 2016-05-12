from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import PresForm


def new(request):
    if request.method == 'POST':
        form = PresForm(request.POST)
        if form.is_valid():
            pres = form.save(commit=False)
            pres.user = request.user
            pres.save()

            return HttpResponseRedirect('admin/create/pres/')

    else:
        form = PresForm()

    context = {
        'form': form,
        'context': 'create.new',
    }
    return render(request, 'create/new.html', context)
