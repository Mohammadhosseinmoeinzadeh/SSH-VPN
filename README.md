# ZED-Panel-SSH
Very simple SSH panel
ابتدا دستور apt update && apt upgrade -y وارد کنید 
از نصب بودن python3 روی سرور اطمینان داشته باشید (عموما به صورت پیشفرض نصب هستند)
سپس کتابخانه های زیر را نصب کنید 
pip install flask
pip install gunicorn
حالا فایل زیپ را دانلود کنید و در سیستم خودتون از حالت فشرده خارج کنید
فایل زیپ را با نرم افزار Bitvise SSH Client  بعد از اتصال به سرور  در قسمت New SFTP window در سرور خود اپلود و از حالت فشرده خارج کنید
تر ترمینل سرور عبارت python3 app.py  را اجرا کنید 
حالا در مرورگر سیستم تون ادرس ای پی و پورت 5000 وارد کنید مثال: 123.21.324.21:5000 
وارد صفحه لاگین میشوید به صورت پیشفرض یوزر پسورد admin,admin  است (برای تغییر یوزر پسورد میتوانید فایل app.py را به صورت nano (دستور nano app.py) باز کنید در قسمتی که به صورت کامنت شده نوشته شده user password در قسمت if username == 'admin' and password == 'admin' قسمت های admin را به صورت دلخواه قرار بدید این یوزر پسورد برای لاگین تون استفاده میشه )
 نرم افزار برای اتصال ios و android برنامه napsternetv است. 
کانکشن های این پنل بر اساس پروتکل ssh  است.
