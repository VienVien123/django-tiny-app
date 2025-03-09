from django.shortcuts import render, redirect, get_object_or_404
from TODO_LIST_APP.models import Task
from TODO_LIST_APP.forms import TaskForm, RegisterForm, LoginForm
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login,get_user_model,update_session_auth_hash
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm
from django.http import HttpResponseNotAllowed
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.contrib.auth import logout


def user_logout(request):
    logout(request)  # Đăng xuất user
    request.session.flush()  # Xóa toàn bộ session
    request.user = None  # Đặt user thành None để đảm bảo không còn user nào đăng nhập
    return redirect("login")  # Chuyển hướng về trang đăng nhập



@login_required(login_url="login")  # Chuyển hướng đến login nếu chưa đăng nhập
def home(request):
    if not request.user.is_authenticated:  # Kiểm tra user có đăng nhập không
        return redirect("login")
    
    tasks = Task.objects.filter(is_archived=False, is_deleted=False)
    context = {'tasks': tasks, 'form': TaskForm}
    return render(request, 'home.html', context=context)



def archived(request):
    tasks_archived = Task.objects.filter(is_archived=True, is_deleted=False)
    context = {'tasks_archived': tasks_archived}
    return render(request, 'archived.html', context=context)


def deleted(request):
    tasks_deleted = Task.objects.filter(is_archived=False, is_deleted=True)
    context = {'tasks_deleted': tasks_deleted}
    return render(request, 'deleted.html', context=context)


# def add(request):
#     if request.method == 'POST':
#         form = TaskForm(request.POST)
#         if form.is_valid():
#             obj = form.save(commit=False)
#             obj.save()
#     return redirect('home')
@login_required  # Đảm bảo người dùng đã đăng nhập
def add(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            if request.user.is_authenticated:  # Kiểm tra user có đăng nhập không
                obj = form.save(commit=False)
                obj.user = request.user  # Gán user hiện tại vào task
                obj.save()
            else:
                return HttpResponseForbidden("Bạn phải đăng nhập để thêm Task.")
    return redirect('home')

def update(request, pk):
    obj = Task.objects.get(pk=pk)
    if request.method == 'POST':
            form = TaskForm(request.POST, instance=obj)
            if form.is_valid():
                form.save()
    else:
        action = request.GET.get('action')
        if action == 'is_completed':
            obj.is_completed = not obj.is_completed
        elif action == 'is_archived':
            obj.is_archived = not obj.is_archived
            obj.is_deleted = False 
        elif action == 'is_deleted':
            obj.is_deleted = not obj.is_deleted
            obj.is_archived = False   
        else:
            return redirect('home')
        obj.save()
    return redirect(request.META.get('HTTP_REFERER'))


def empty_recycle_bin(request):
    obj = Task.objects.filter(is_deleted=True)
    obj.delete()
    return redirect('deleted')

def user_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST["username"]
            password = request.POST["password"]
            user = authenticate(request, username=username, password=password)

            print(user)

            if user:
                if user.is_active:
                    login(request, user)
                    messages.success(request, "Login successful! Welcome back 🎉")
                    return redirect('home')  # Chuyển hướng về trang chủ
                else:
                    messages.error(request, "Your account has been blocked.")
                    return redirect('login')
            else:
                messages.error(request, "Invalid username or password!")  # Hiển thị lỗi
                return render(request, "login.html", {"form": form})  # Render lại trang login với lỗi
    else:
        form = LoginForm()

    return render(request, "login.html", {"form": form})


def user_register(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    
    return render(request, 'register.html', {'form': form})


# Phần của admin
def is_admin(user):
    return user.is_superuser

# Quản lý user - admin chỉ có thể xem danh sách người dùng và thực hiện các thao tác
@user_passes_test(is_admin)
def manage_users(request):
    users = User.objects.all()
    return render(request, "manage_users.html", {'users': users})

# Khóa hoặc mở khóa user
@user_passes_test(is_admin)
def toggle_block_user(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    # Không cho phép admin khóa chính tài khoản của mình
    if user == request.user:
        messages.error(request, "You cannot block your own account.")
        return redirect('manage_users')
    
    # Khóa hoặc mở khóa tài khoản user
    user.is_active = not user.is_active  # Khóa user bằng cách thay đổi trạng thái is_active
    user.save()
    status = "blocked" if not user.is_active else "unblocked"
    messages.success(request, f"User {user.username} has been {status}.")
    return redirect('manage_users')

# Reset mật khẩu cho user
@user_passes_test(is_admin)
def reset_password(request, user_id):
    user = get_object_or_404(User, id=user_id)
    
    # Nếu user đang bị khóa, thông báo và không cho phép reset mật khẩu
    if not user.is_active:
        messages.error(request, "User account is blocked. Cannot reset password.")
        return redirect('manage_users')
    
    if request.method == "POST":
        form = PasswordChangeForm(user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)  # Cập nhật session sau khi đổi mật khẩu
            messages.success(request, f"Password for {user.username} has been reset.")
            return redirect('manage_users')
    else:
        form = PasswordChangeForm(user)

    return render(request, 'reset_password.html', {'form': form, 'user': user})