from django.http import HttpResponse
from django.shortcuts import render, redirect

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)

        protected_urls = [
            "/app/form/"
        ]

        router = request.path

        if request.session.get('user') is None:
            if router in protected_urls:

                return redirect('/app/home')

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware