import requests
import os

url="https://www.google.com/"    #Change this url

pagina=requests.get(url)

estado=pagina.status_code

if estado==200:
    print("Everything went well, the scraping was correct")

elif estado!=200:
    print("There was an error in scraping")

decision=input("Do you want to see the content in console yes or not?:")

if decision=="yes":
    print(pagina.text)
elif decision=="not":
    al=input("And you want to write the content to a file? yes or not:")
    if al=="yes":
        archivo=open("test.txt","w")
        archivo.write(pagina.text)
        archivo.close()
    elif al=="not":
        print("thank you for using")

#This simple script is used to scrapping on all types of pages and pass it to a txt but remember that if you have emojis or rare symbols, it will give file encoding error, but on almost all websites it works as long as they do not have that type of data

#Este simple script sirve para hacer scrapping en todo tipo de pagina y pasarlo a un txt pero recuerda que si tiene emojis o simbolos raros va a dar error de codificacion del archivo, pero en casi todas las web funciona mientras no tengan ese tipo de dato
