from .models import Project
from django.contrib import messages
from django.urls import reverse
from django.shortcuts import redirect
from django.db.models import Q



def owner_level_access(function):
    """
       Decorator used to test if a user has rights to access a project
       """

    def wrap(request, *args, **kwargs):

        project = Project.objects.filter(pk=kwargs['id']).first()

        if (project.owner == request.user or request.user.is_superuser):
            return function(request, *args, **kwargs)
        else:
            messages.error(request, "User not allowed to modify project")
            return redirect(reverse("project_view", kwargs=dict(id=project.id)))

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap

    pass


def group_level_access(function):
    """
    Decorator used to test if a user has rights to access a project
    """
    def wrap(request, *args, **kwargs):

        id=kwargs['id']

        # Get the project access
        project = Project.objects.filter(pk=id).first()

        # Asking for a non-existing project.
        if not project:
            messages.error(request, f"Project with id={id} does not exist.")
            return redirect(reverse("project_list"))

        # Conditions for allowing access.
        allow_access = project.privacy == Project.PUBLIC
        allow_access = allow_access or project.owner == request.user
        allow_access = allow_access or project.group in request.user.groups.all()

        if allow_access:
            return function(request, *args, **kwargs)
        else:
            messages.error(request, f"Access to project id={id} denied.")
            return redirect(reverse("project_list"))

    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap
