import requests

def download_file(url , file_name):
    respo=requests.get(url)
    if respo.status_code ==200:
        with open(file_name , 'wb') as file:
            
