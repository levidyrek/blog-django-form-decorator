import functools

from django.shortcuts import render


def view_form(form_cls, template):
    """
    Creates a decorator that handles the standard Django Form
    workflow; only calling the wrapped view when on a successfully-
    validated POST.
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(request, *args, **kwargs):
            form = form_cls()
            if request.method == 'POST':
                form = form_cls(request.POST)
                if form.is_valid():
                    return func(
                        request, *args, **kwargs,
                        params=form.cleaned_data
                    )

            return render(request, template, {
                'form': form,
            })

        return wrapper
    return decorator
