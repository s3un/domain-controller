import requests
import os
import typer
import csv
import datetime
from bs4 import BeautifulSoup

onionapp = typer.Typer(add_completion=False, add_help_option=False)

torservice = os.system("sudo service tor start")

session = requests.session()
session.proxies = {}

session.proxies = {
    'http' : 'socks5h://localhost:9050',
    'https' : 'socks5h://localhost:9050'
}

@onionapp.command("oh")
def onionheader():
    domain = input("[+]Enter domain name$ ")
    starter = (typer.style("---------------------------------------------------------------------------------- \n[+] Fetching Header:  """, fg=typer.colors.BLUE))
    print(starter)
    now = datetime.datetime.now()
    response = session.get(domain)
    ohead = response.headers
    for key, value in ohead.items():
        print(f"[+]{key} : {value}")
    print("[+]Timestamp: ", now.strftime("%Y-%m-%d %H:%M:%S"))
    print(typer.style("----------------------------------------------------------------------------------", fg=typer.colors.BLUE))

@onionapp.command("osc")
def status_code():
    domain = input("[+]Enter domain name$ ")
    starter = (typer.style("---------------------------------------------------------------------------------- \n[+] Generating Status Code:  """, fg=typer.colors.BLUE))
    print(starter)
    now = datetime.datetime.now()
    page = session.get(domain)
    if page.status_code == 200:
        good = typer.style("[=]The request has succeeded and the domain is reachable", fg=typer.colors.GREEN)
        typer.echo(good)
        print("[+]Status Code: ", page.status_code)
        print("[+]Timestamp: ", now.strftime("%Y-%m-%d %H:%M:%S"))
    else:
        bad = typer.style("[+] This domain is currently not reachable", fg=typer.colors.RED)
        typer.echo(bad)
        typer.echo(page.status_code)
        print("[+]Timestamp: ", now.strftime("%Y-%m-%d %H:%M:%S"))
    print(typer.style("----------------------------------------------------------------------------------", fg=typer.colors.BLUE))


@onionapp.command("ou")
def upload():
    filepath = input("[+]Enter file path$ ")
    starter = (typer.style("---------------------------------------------------------------------------------- \n[+] Scanning through rows:  ",fg=typer.colors.BLUE))
    print(starter)
    if filepath.endswith(".csv"):
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
    print(typer.style("----------------------------------------------------------------------------------", fg=typer.colors.BLUE))

if __name__ == "__main__":
    onionapp()
    
