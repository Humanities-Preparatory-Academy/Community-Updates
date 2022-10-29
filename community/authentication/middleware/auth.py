from django.http import HttpResponse
from django.shortcuts import render, redirect
import re

def auth_middleware(get_response):
    # One-time configuration and initialization.

    def middleware(request):
        # Code to be executed for each request before
        # the view (and later middleware) are called.

        response = get_response(request)

        protected_urls = [
            "/internsips/form/",
            "/internships/edit/"
        ]

        # Remove all identifier digtis and other metadata to get the core url

        router = re.sub("\d", "", request.path)

        if request.session.get('user') is None:
            if router in protected_urls:

                return redirect('/internships')

        # Code to be executed for each request/response after
        # the view is called.

        return response

    return middleware