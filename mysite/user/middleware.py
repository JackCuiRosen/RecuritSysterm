
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from django.urls import resolve


class UserDirectMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        resolver_match = resolve(request.path)
        view_name = resolver_match.view_name
        # return redirect('/')

        if view_name == "admin:login" and request.method == "POST":
            # return redirect('/')
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(username=username,password=password)
            print(username)
            # print(user)
            if user is not None and user.has_perm('auth.can_interview') and user.is_superuser != True:
                login(request,user)
                return redirect('/interview')


        responese = self.get_response(request)


        return responese
