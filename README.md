# ZED-Panel-SSH
Very simple SSH VPN panel



ابتدا دستور apt update && apt upgrade -y وارد کنید 


از این دستور برای نصب python3 وارد کنید :      apt install python3-pip -y



سپس کتابخانه های زیر را نصب کنید 

pip install flask


pip install gunicorn



حالا فایل زیپ (ZEDPanel.zip) را دانلود کنید.

فایل زیپ را با نرم افزار Bitvise SSH Client  بعد از اتصال به سرور  در قسمت New SFTP window در سرور خود اپلود کنید

در ترمینال دستور unzip ZEDPanel.zip را وراد کنید تا فایل از حالت فشرده خارج شود
 
در ترمینل سرور عبارت python3 app.py  را اجرا کنید 

حالا در مرورگر سیستم تون ادرس ای پی و پورت 5000 وارد کنید مثال: 123.21.324.21:5000 

وارد صفحه لاگین میشوید به صورت پیشفرض یوزر پسورد admin,admin 
است 

(برای تغییر یوزر پسورد میتوانید فایل app.py را به صورت nano (دستور nano app.py) باز کنید در قسمتی که به صورت کامنت شده نوشته شده user password در قسمت if username == 'admin' and password == 'admin' قسمت های admin را به صورت دلخواه قرار بدید این یوزر پسورد برای لاگین تون استفاده میشه )


توجه: بعد از بستن ترمینال پنل از دسترس خارج میشود( کانکشن ها قطع نمیشوند صرفا فقط به پنل دسترسی ندارید) برای دسترسی دوباره به پنل در ترمینل دستور python3 app.py  را اجرا کنید 

در صورتی که سرعت کانکشن ها کم است پورت ssh سرور را تغییر بدید.

مراحل تغییر پورت SSH: 

1. ابتدا در ترمینال این دستور را وارد کنید : sudo nano /etc/ssh/sshd_config
   2. در صفحه باز شده دنبال عبارت Port22 # بگردید (#) را پاک کنید و به جای 22 پورت مورد نظر را وارد کنید و فایل را ذخیره کنید.
   3. سرور را با دستور reboot ریستارت کنید
   4. از این پس باید باید با همان پورتی که وارد کردید، وارد سرور شوید .
در صورت خطا(بعد از اضافه کردن کاربر، کاربر را درلیست نمایش نداد) توی ترمینال این دستور  cut -d: -f1 /etc/passwd را وارد کنید اگر یوزر شما اضافه شده باشد نام یوزر نمایش خواهد داده شد. در غیر این صورت یوزر اضافه نشده.

 نرم افزار برای اتصال ios و android برنامه napsternetv است. 
 برای windows از برنامه netmode  استفاده کنید.
 
کانکشن های این پنل بر اساس پروتکل ssh  است.
