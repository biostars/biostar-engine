from django.contrib.auth import logout
from django.contrib import messages
from biostar.accounts.models import Profile


def recipes_middleware(get_response):

    def middleware(request):

        user = request.user

        # Banned and suspended users are not allowed
        if user.is_authenticated and user.profile.state in (Profile.BANNED, Profile.SUSPENDED):
            messages.error(request, f"Account is {user.profile.get_state_display()}")
            logout(request)

        response = get_response(request)
        # Can process response here after its been handled by the view

        # Turn CORS on.
        response["Access-Control-Allow-Origin"] = "*"

        return response

    return middleware


