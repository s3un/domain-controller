import requests
import csv
import typer
import os
from bs4 import BeautifulSoup

torservice = os.system("sudo service tor start")

session = requests.session()
session.proxies = {}

session.proxies = {
    'http' : 'socks5h://localhost:9050',
    'https' : 'socks5h://localhost:9050'
}

def Onionheader():
    starter = (typer.style("---------------------------------------------------------------------------------- \n[+] Fetching Header:  """, fg=typer.colors.BLUE))
    print (starter)
    #response = session.get(Domain)
    #ohead = response.headers
    #for key, value in ohead.items():
  #      print(f"[+]{key} : {value}")


def upload():
    filepath = input("[+]Enter file path$ ")
    starter = (typer.style("---------------------------------------------------------------------------------- \n[+] Scanning through files:  ",fg=typer.colors.BLUE))
    print(starter)
    if filepath.endswith('.txt'):
        file = open(filepath, 'r')
        data = file.read()
        for value in data:
            framework = value[0]
            response = session.get(framework)
            grab = BeautifulSoup(response.text, "html.parser")
            title = grab.title
            gtitle = title.string

            print(f"[+]Domain: {value[0]}\n[+]Title: {gtitle} \n[+]Status code: ", response.status_code, "\n")
    elif filepath.endswith(".csv"):
        starter = (typer.style("---------------------------------------------------------------------------------- \n[+] Scanning through files:  ",fg=typer.colors.BLUE))
        with open(filepath, mode='r') as f:
            reader = csv.reader(f, delimiter=',')
            for value in reader:
                framework = value[0]
                response = session.get(framework)
                grab = BeautifulSoup(response.text, "html.parser")
                title = grab.title
                gtitle = title.string

                print(f"[+]Domain: {value[0]}\n[+]Title: {gtitle} \n[+]Status code: ", response.status_code, "\n")
    else:
        err = typer.style("[+]File format not supported!", fg=typer.colors.RED)
        typer.echo(err)


upload()
