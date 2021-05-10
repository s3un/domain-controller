import requests
import subprocess as subp
import os
import datetime
import typer

onionapp = typer.Typer(add_completion=False, add_help_option=False)

torservice = os.system("sudo service tor start")

session = requests.session()
session.proxies = {}

session.proxies = {
    'http' : 'socks5h://localhost:9050',
    'https' : 'socks5h://localhost:9050'
}

@onionapp.command()
def onionheader():
    domain = input("[+]Enter domain name$ ")
    starter = (typer.style("---------------------------------------------------------------------------------- \n[+] Fetching Header:  """, fg=typer.colors.BLUE))
    print(starter)
    response = session.get(domain)
    ohead = response.headers
    for key, value in ohead.items():
        print(f"[+]{key} : {value}")


@onionapp.command()
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
    print (typer.style("----------------------------------------------------------------------------------", fg=typer.colors.BLUE))


@onionapp.command()
def builtwith():
    import builtwith
    domain = input("[+]Enter your domain$ ")
    starter = (typer.style("---------------------------------------------------------------------------------- \n[+] Generating Builtwith Info:  """,fg=typer.colors.BLUE))
    page = builtwith.parse(domain)
    for key, value in page.items():
        frameworks = ",".join(value)
        print(f"[=]{key} : {frameworks}")


if __name__ == "__main__":
    onionapp()
    
