import requests
import typer
import datetime
import csv
from bs4 import BeautifulSoup
import os


app = typer.Typer(add_completion=False)

torservice = os.system("sudo service tor start")

session = requests.session()
session.proxies = {}

session.proxies = {
    'http' : 'socks5h://localhost:9050',
    'https' : 'socks5h://localhost:9050'
}

@app.command("sc")
def status_code():
    """
    - Clearweb domain status check
    """
    now = datetime.datetime.now()
    domain = input("Enter domain name$ ")
    starter = (typer.style("---------------------------------------------------------------------------------- \n[+] Generating Status Code:  """,fg=typer.colors.BLUE))
    page = requests.get(domain)
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
    print(typer.style("----------------------------------------------------------------------------------",fg=typer.colors.BLUE))

@app.command("w")
def who_is():
    """
    - Provides whois information on clearweb domains
    """
    import whois
    now = datetime.datetime.now()
    domain = input("Enter your domain$ ")
    starter = (typer.style("---------------------------------------------------------------------------------- \n[+] Generating Whois Info:  """,fg=typer.colors.BLUE))
    response = whois.whois(domain)
    for key, value in response.items():
        print(f"[+]{key} : {value}")
    print("[+]", now.strftime("%Y-%m-%d %H:%M:%S"))
    print(typer.style("----------------------------------------------------------------------------------",fg=typer.colors.BLUE))

@app.command("h")
def header():
    """
    - Provides domain header information
    """
    domain = input("Enter your domain$ ")
    starter = (typer.style("---------------------------------------------------------------------------------- \n[+] Fetching Header:  """,fg=typer.colors.BLUE))
    response = requests.get(domain)
    hea = response.headers
    for key, value in hea.items():
        print(f"[+]{key} : {value}")
    print(typer.style("----------------------------------------------------------------------------------", fg=typer.colors.BLUE))


@app.command("b")
def builtwith(clearweb: str = typer.Option("", help = "Clearweb")):
    """
    - Provides domain built with information
    """
    import builtwith
    clearweb = input("Enter your domain$ ")
    starter = (typer.style("---------------------------------------------------------------------------------- \n[+] Generating Builtwith Info:  ",fg=typer.colors.BLUE))
    page = builtwith.parse(clearweb)
    for key, value in page.items():
        frameworks = ",".join(value)
        print(f"[=]{key} : {frameworks}")
    print(typer.style("----------------------------------------------------------------------------------", fg=typer.colors.BLUE))


@app.command("u")
def upload():
    """
    - Scans multiple clear web domain in a .csv file
    """
    filepath = input("[+]Enter file path$ ")
    if filepath.endswith(".csv"):
        starter = (typer.style("---------------------------------------------------------------------------------- \n[+] Scanning through files:  ",fg=typer.colors.BLUE))
        with open(filepath, mode='r') as f:
            reader = csv.reader(f, delimiter=',')
            for value in reader:
                framework = value[0]
                response = requests.get(framework)
                print(f"[+]{value[0]}  ", response.status_code)
    else:
        err = typer.style("[+]File format not supported!", fg=typer.colors.RED)
        typer.echo(err)
    print(typer.style("----------------------------------------------------------------------------------",fg=typer.colors.BLUE))

@app.command("oh")
def onionheader():
    """
    - Onion domain header information
    """
    domain = input("[+]Enter domain name$ ")
    starter = (typer.style("---------------------------------------------------------------------------------- \n[+] Fetching Header:  """, fg=typer.colors.BLUE))
    print(starter)
    if not ".onion" in domain:
        print(f"[+]{domain} = Not a valid onion link")
    else:
        now = datetime.datetime.now()
        response = session.get(domain)
        ohead = response.headers
        for key, value in ohead.items():
            print(f"[+]{key} : {value}")
        print("[+]Timestamp: ", now.strftime("%Y-%m-%d %H:%M:%S"))
        print(typer.style("----------------------------------------------------------------------------------", fg=typer.colors.BLUE))

@app.command("osc")
def status_code():
    """
    - Onion domain status check
    """
    domain = input("[+]Enter domain name$ ")
    starter = (typer.style("---------------------------------------------------------------------------------- \n[+] Generating Status Code:  """, fg=typer.colors.BLUE))
    print(starter)
    now = datetime.datetime.now()
    page = session.get(domain)
    grab = BeautifulSoup(page.text, "html.parser")
    title = grab.title
    gtitle = title.string
    if page.status_code == 200:
        good = typer.style("[=]The request has succeeded and the domain is reachable", fg=typer.colors.GREEN)
        typer.echo(good)
        print("[+]Status Code: ", page.status_code)
        print(f"[+]Title: {gtitle}")
        print("[+]Timestamp: ", now.strftime("%Y-%m-%d %H:%M:%S"))
    else:
        bad = typer.style("[+] This domain is currently not reachable", fg=typer.colors.RED)
        typer.echo(bad)
        typer.echo(page.status_code)
        print("[+]Timestamp: ", now.strftime("%Y-%m-%d %H:%M:%S"))
    print(typer.style("----------------------------------------------------------------------------------", fg=typer.colors.BLUE))


@app.command("ou")
def upload():
    """
    - Scans multiple onion domains in a .csv file
    """
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
    app()