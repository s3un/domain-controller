import requests
import typer
import datetime
import csv
from bs4 import BeautifulSoup
import os
import time


app = typer.Typer(add_completion=False)

torservice = os.system("sudo service tor start")

session = requests.session()
session.proxies = {}

session.proxies = {
    'http' : 'socks5h://localhost:9050',
    'https' : 'socks5h://localhost:9050'
}

R = '\033[31m' # red
G = '\033[32m' # green
C = '\033[36m' # cyan
W = '\033[0m' # white


@app.command("sc")
def status_code():
    """
    - Clearweb domain status check
    """
    now = datetime.datetime.now()
    domain = input(G + '[+]' + C +"Enter domain name$ " + W)
    ios = typer.style("---------------------------------------------------------------------------------- \n[+] Generating Status Code:  """,fg=typer.colors.BLUE)
    typer.echo(ios)
    if 'https://' in domain:
        page = requests.get(domain)
    else:
        page = requests.get('https://' + domain)
    if page.status_code == 200:
        good = typer.style("[+]The request has succeeded and the domain is reachable", fg=typer.colors.GREEN)
        typer.echo(good)
        print("[+]Status Code: ", page.status_code)
        print("[+]Timestamp: ", now.strftime("%Y-%m-%d %H:%M:%S"))
    else:
        bad = typer.style("[=] This domain is currently not reachable", fg=typer.colors.RED)
        typer.echo(bad)
        typer.echo(page.status_code)
        print("[+]Timestamp: ", now.strftime("%Y-%m-%d %H:%M:%S"))
    io = typer.style("----------------------------------------------------------------------------------",fg=typer.colors.BLUE)
    typer.echo(io)


@app.command("w")
def who_is():
    """
    - Provides whois information on clearweb domains
    """
    import whois
    now = datetime.datetime.now()
    domain = input(G + '[+]' + C + "Enter your domain$ " + W)
    ios = typer.style("---------------------------------------------------------------------------------- \n[+] Generating Whois Info...:  """,fg=typer.colors.BLUE)
    typer.echo(ios)
    if 'https://' in domain:
        response = whois.whois(domain)
    else:
        response = whois.whois('https://' + domain)
    for key, value in response.items():
        print(f"[+]{key} : {value}")
    print("[+]", now.strftime("%Y-%m-%d %H:%M:%S"))
    io = typer.style("----------------------------------------------------------------------------------",fg=typer.colors.BLUE)
    typer.echo(io)


@app.command("h")
def header():
    """
    - Provides domain header information
    """
    domain = input(G + '[+]' + C + "Enter your domain$ " + W)
    ios = typer.style("---------------------------------------------------------------------------------- \n[+] Generating header info..:  """,fg=typer.colors.BLUE)
    typer.echo(ios)
    if 'https://' in domain:
        page = requests.get(domain)
    else:
        page = requests.get('https://' + domain)
    hea = page.headers
    for key, value in hea.items():
        print(f"[+]{key} : {value}")
    io = typer.style("----------------------------------------------------------------------------------",fg=typer.colors.BLUE)
    typer.echo(io)


@app.command("b")
def builtwith():
    """
    - Provides domain built with information
    """
    import builtwith
    clearweb = input(G + '[+]' + C + "Enter your domain$ " + W)
    ios = typer.style("---------------------------------------------------------------------------------- \n[+] Generating built with info...:  """,fg=typer.colors.BLUE)
    typer.echo(ios)
    if 'https://' in clearweb:
        page = builtwith.parse(clearweb)
    else:
        page = builtwith.parse('https://' + clearweb)
    for key, value in page.items():
        frameworks = ",".join(value)
        print(f"[=]{key} : {frameworks}")
    io = typer.style("----------------------------------------------------------------------------------",fg=typer.colors.BLUE)
    typer.echo(io)


@app.command("u")
def upload():
    """
    - Scans multiple clear web domain in a .csv file
    """
    filepath = input(G + '[+]' + C +"Enter file path$ " + W)
    if filepath.endswith(".csv"):
        ios = typer.style("---------------------------------------------------------------------------------- \n[+] Scanning through files:  """,fg=typer.colors.BLUE)
        typer.echo(ios)
        with open(filepath, mode='r') as f:
            reader = csv.reader(f, delimiter=',')
            for value in reader:
                framework = value[0]
                response = requests.get(framework)
                print(f"[+]{value[0]}  ", response.status_code)
    else:
        err = typer.style("[+]File format not supported!", fg=typer.colors.RED)
        typer.echo(err)
    io = typer.style("----------------------------------------------------------------------------------",fg=typer.colors.BLUE)
    typer.echo(io)


@app.command("oh")
def onionheader():
    """
    - Onion domain header information
    """
    domain = input(G + '[+]' + C + "Enter domain name$ " + W)
    ios = typer.style("---------------------------------------------------------------------------------- \n[+] Generating header info...:  """,fg=typer.colors.BLUE)
    typer.echo(ios)
    if not ".onion" in domain:
        print(f"[+]{domain} = Not a valid onion link")
    else:
        now = datetime.datetime.now()
        response = session.get(domain)
        ohead = response.headers
        for key, value in ohead.items():
            print(f"[+]{key} : {value}")
        print("[+]Timestamp: ", now.strftime("%Y-%m-%d %H:%M:%S"))
    io = typer.style("----------------------------------------------------------------------------------",fg=typer.colors.BLUE)
    typer.echo(io)


@app.command("osc")
def status_code():
    """
    - Onion domain status check
    """
    domain = input(G + '[+]' + C +"Enter domain name$ " + W)
    ios = typer.style("---------------------------------------------------------------------------------- \n[+] Generating Status Code:  """,fg=typer.colors.BLUE)
    typer.echo(ios)
    now = datetime.datetime.now()
    if 'https://' in domain:
        page = session.get(domain)
    else:
        page = session.get('https://' + domain)
    if page.status_code == 200:
        good = typer.style("[=]The request has succeeded and the domain is reachable", fg=typer.colors.GREEN)
        typer.echo(good)
        print("[+]Status Code: ", page.status_code)
        print("[+]Timestamp: ", now.strftime("%Y-%m-%d %H:%M:%S"))
    elif page.status_code != 200:
        print("The onion link is currently not reachable")
        print("[+]Status Code: ", page.status_code)
    else:
        bad = typer.style("[+] This domain is currently not reachable", fg=typer.colors.RED)
        typer.echo(bad)
        typer.echo(page.status_code)
        print("[+]Timestamp: ", now.strftime("%Y-%m-%d %H:%M:%S"))
    io = typer.style("----------------------------------------------------------------------------------",fg=typer.colors.BLUE)
    typer.echo(io)


@app.command("ou")
def upload():
    """
    - Scans multiple onion domains in a .csv file
    """
    filepath = input(G + '[+]' + C +"Enter file path$ " + W)
    ios = typer.style("---------------------------------------------------------------------------------- \n[+] Scanning through files:  """,fg=typer.colors.BLUE)
    typer.echo(ios)
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
    io = typer.style("----------------------------------------------------------------------------------",fg=typer.colors.BLUE)
    typer.echo(io)

if __name__ == "__main__":
    app()