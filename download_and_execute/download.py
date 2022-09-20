#!/usr/bin/env python2
import requests


def download(url):
    get_response = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name, "wb") as output_file:
        output_file.write(get_response.content)


download("https://www.thestatesman.com/wp-content/uploads/2020/01/vintage.jpg")
