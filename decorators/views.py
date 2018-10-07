from django.http import HttpResponse
from django.shortcuts import render
from django.views.decorators.http import require_http_methods

from .decorators import view_form
from .forms import PersonForm


@require_http_methods(['GET', 'POST'])
def enter_name_no_decorator(request):
    form = PersonForm()
    if request.method == 'POST':
        form = PersonForm(request.POST)
        if form.is_valid():
            params = form.cleaned_data

            first_name = params['first_name'].title()
            last_name = params['last_name'].title()
            return HttpResponse(
                'Welcome, {} {}!'.format(first_name, last_name)
            )

    return render(request, 'enter_name_no_decorator.html', {
        'form': form,
    })


@require_http_methods(['GET', 'POST'])
@view_form(PersonForm, 'enter_name_with_decorator.html')
def enter_name_with_decorator(request, params):
    first_name = params['first_name'].title()
    last_name = params['last_name'].title()
    return HttpResponse(
        'Welcome, {} {}!'.format(first_name, last_name)
    )
