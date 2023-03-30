from django.shortcuts import redirect
from django.contrib import messages


def user_is_staff_or_manager(function=None, redirect_url='/'):

    def decorator(view_func):
        def _wrapped_view(request, *args, **kwargs):
            if not request.user.is_staff and not request.user.is_manager:
                messages.error(request, 'You are not authorized to access this!')
                return redirect(redirect_url)
            
            return view_func(request, *args, **kwargs)
        return _wrapped_view
    
    if function:
        return decorator(function)
    
    return decorator
