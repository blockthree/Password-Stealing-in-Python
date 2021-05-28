import requests

def download(url):
    image = requests.get(url)
    file_name = url.split("/")[-1]
    with open(file_name,'wb') as b:
        b.write(image.content)

download("https://i.pinimg.com/564x/b9/59/a0/b959a00e047b6071f417c4ef50dd0951.jpg")    