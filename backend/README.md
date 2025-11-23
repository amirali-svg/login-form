# راهنمای اجرای پروژه

## نصب وابستگی‌ها

ابتدا Django و کتابخانه‌های مورد نیاز را نصب کنید:

```bash
pip install -r requirements.txt
```

یا اگر در پوشه اصلی هستید:

```bash
pip install -r requirements.txt
```

## اجرای سرور Django

### روش 1: استفاده از فایل run.bat (ویندوز)
```bash
cd backend
run.bat
```

### روش 2: استفاده از دستور مستقیم
```bash
cd backend
python manage.py runserver
```

سپس به آدرس `http://127.0.0.1:8000/` بروید.

## نحوه کار

1. **صفحه لاگین**: در آدرس اصلی (`http://127.0.0.1:8000/`) نمایش داده می‌شود
2. **ثبت نام**: روی دکمه "Don't have an account?" کلیک کنید
3. **فرم ثبت نام**: username، password و email را وارد کنید
4. **بعد از ثبت نام یا لاگین موفق**: به صفحه اصلی (`/main/`) هدایت می‌شوید
5. **صفحه اصلی**: نام کاربری و ایمیل شما نمایش داده می‌شود

## ساختار پروژه

```
backend/
  ├── manage.py              # فایل مدیریت Django
  ├── myproject/            # تنظیمات اصلی Django
  │   ├── settings.py       # تنظیمات پروژه
  │   └── urls.py           # مسیرهای URL
  ├── auth_app/             # اپلیکیشن احراز هویت
  │   ├── views.py          # منطق لاگین و ثبت نام
  │   ├── templates/        # فایل‌های HTML
  │   │   ├── index.html    # صفحه لاگین/ثبت نام
  │   │   └── main_page.html # صفحه اصلی
  │   ├── static/           # فایل‌های استاتیک (CSS, JS)
  │   │   ├── css/
  │   │   │   ├── styles.css
  │   │   │   └── output.css
  │   │   └── js/
  │   │       └── scripts.js
  │   └── users.json        # ذخیره اطلاعات کاربران
  └── run.bat               # فایل اجرای سریع (ویندوز)
```

## نکات مهم

- اطلاعات کاربران در فایل `auth_app/users.json` ذخیره می‌شود
- فایل‌های HTML در `auth_app/templates/` قرار دارند
- فایل‌های CSS و JS در `auth_app/static/` قرار دارند
- Django به صورت خودکار فایل‌های static را از پوشه `static/` هر app پیدا می‌کند

