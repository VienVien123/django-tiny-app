from django.shortcuts import redirect
from django.contrib.auth import logout
from django.contrib import messages

class BlockedUserMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if request.user.is_authenticated and request.user.is_blocked:
            messages.error(request, "Tài khoản của bạn đã bị khóa.")
            logout(request)
            return redirect("login")  # Chuyển hướng về trang đăng nhập
        return self.get_response(request)
