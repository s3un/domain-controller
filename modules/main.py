import requests
import typer
import datetime
import re
import csv

app = typer.Typer(add_completion=False, add_help_option=False)

@app.command()
def status_code():
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


@app.command()
def who_is():
    import whois
    now = datetime.datetime.now()
    starter = (typer.style("---------------------------------------------------------------------------------- \n[+] Generating Whois Info:  """,fg=typer.colors.BLUE))
    domain = input("Enter your domain$ ")
    response = whois.whois(domain)
    for key, value in domain.items():
        print(f"[+]{key} : {value}")
    print("[+]", now.strftime("%Y-%m-%d %H:%M:%S"))


@app.command()
def ip_lookup():
    regex = "(([0-9]|[1-9][0-9]|1[0-9][0-9]|"\
            "2[0-4][0-9]|25[0-5])\\.){3}"\
            "([0-9]|[1-9][0-9]|1[0-9][0-9]|"\
            "2[0-4][0-9]|25[0-5])"

    regex1 = "((([0-9a-fA-F]){1,4})\\:){7}"\
             "([0-9a-fA-F]){1,4}"
    p = re.compile(regex)
    p1 = re.compile(regex)

    p2 = re.search(input("Enter your IP Address$ "))
    print("Ip address is valid")


@app.command()
def header():
    domain = input("Enter your domain$ ")
    starter = (typer.style("---------------------------------------------------------------------------------- \n[+] Fetching Header:  """,fg=typer.colors.BLUE))
    response = requests.get(domain)
    hea = response.headers
    for key, value in hea.items():
        print(f"[=]{key} : {value}")


@app.command()
def builtwith():
    import builtwith
    domain = input("Enter your domain$ ")
    starter = (typer.style("---------------------------------------------------------------------------------- \n[+] Generating Builtwith Info:  ",fg=typer.colors.BLUE))
    page = builtwith.parse(domain)
    for key, value in page.items():
        frameworks = ",".join(value)
        print(f"[=]{key} : {frameworks}")

@app.command()
def upload():
    filepath = input("[+]Enter file path$ ")
    starter = (typer.style("---------------------------------------------------------------------------------- \n[+] Scanning through files:  ",fg=typer.colors.BLUE))
    print(starter)
    if filepath.endswith('.txt'):
        try:
            file = open(filepath, 'r')
            for value in file:
                framework = value[0]
                response = requests.get(framework)
                print(f"[+]{value[0]} : ", response.status_code)
        except:
            err = typer.style("[+]This is not a .txt file", fg=typer.colors.RED)
            typer.echo(err)
    elif filepath.endswith(".csv"):
        with open(filepath, mode='r') as f:
            reader = csv.reader(f, delimiter=',')
            for value in reader:
                framework = value[0]
                response = requests.get(framework)
                print(f"[+]{value[0]} : ", response.status_code)
    else:
        err = typer.style("[+]File format not supported!", fg=typer.colors.RED)
        typer.echo(err)


if __name__ == "__main__":
    app()