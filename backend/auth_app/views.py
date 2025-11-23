from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import CustomUser

@csrf_exempt
def login_page(request):
    """نمایش صفحه لاگین و پردازش فرم"""
    error = None
    is_register = False
    
    if request.method == 'POST':
        if 'register' in request.POST:
            username = request.POST.get('username', '').strip()
            password = request.POST.get('password', '').strip()
            email = request.POST.get('email', '').strip()
            
            if not username or not password or not email:
                error = 'همه فیلدها الزامی است'
                is_register = True
            else:
                if CustomUser.objects.filter(username=username).exists():
                    error = 'این نام کاربری قبلاً استفاده شده است'
                    is_register = True
                else:
                    CustomUser.objects.create(
                        username=username,
                        password=password,
                        email=email
                    )
                    return redirect(f'/main/?username={username}')
        else:
            username = request.POST.get('username', '').strip()
            password = request.POST.get('password', '').strip()
            
            if not username or not password:
                error = 'نام کاربری و رمز عبور الزامی است'
            else:
                try:
                    user = CustomUser.objects.get(username=username)
                    if user.password == password:
                        return redirect(f'/main/?username={username}')
                    else:
                        error = 'نام کاربری یا رمز عبور اشتباه است'
                except CustomUser.DoesNotExist:
                    error = 'نام کاربری یا رمز عبور اشتباه است'
    
    if request.method == 'GET' and 'register' in request.GET:
        is_register = True
    
    return render(request, 'index.html', {
        'error': error,
        'is_register': is_register
    })

@csrf_exempt
def main_page(request):
    """نمایش صفحه اصلی با اطلاعات کاربر"""
    username = request.GET.get('username', '')
    
    if not username:
        return redirect('/')
    
    try:
        user = CustomUser.objects.get(username=username)
        return render(request, 'main_page.html', {
            'username': user.username,
            'email': user.email
        })
    except CustomUser.DoesNotExist:
        return redirect('/')

