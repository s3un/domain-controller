import requests
import typer
import datetime
# import whois
import re

print("""
    ██████╗  ██████╗ ███╗   ███╗ █████╗ ██╗███╗   ██╗     ██████╗ ██████╗ ███╗   ██╗████████╗██████╗  ██████╗ ██╗     ██╗     ███████╗██████╗ 
    ██╔══██╗██╔═══██╗████╗ ████║██╔══██╗██║████╗  ██║    ██╔════╝██╔═══██╗████╗  ██║╚══██╔══╝██╔══██╗██╔═══██╗██║     ██║     ██╔════╝██╔══██╗
    ██║  ██║██║   ██║██╔████╔██║███████║██║██╔██╗ ██║    ██║     ██║   ██║██╔██╗ ██║   ██║   ██████╔╝██║   ██║██║     ██║     █████╗  ██████╔╝
    ██║  ██║██║   ██║██║╚██╔╝██║██╔══██║██║██║╚██╗██║    ██║     ██║   ██║██║╚██╗██║   ██║   ██╔══██╗██║   ██║██║     ██║     ██╔══╝  ██╔══██╗
    ██████╔╝╚██████╔╝██║ ╚═╝ ██║██║  ██║██║██║ ╚████║    ╚██████╗╚██████╔╝██║ ╚████║   ██║   ██║  ██║╚██████╔╝███████╗███████╗███████╗██║  ██║
    ╚═════╝  ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝╚═╝  ╚═══╝     ╚═════╝ ╚═════╝ ╚═╝  ╚═══╝   ╚═╝   ╚═╝  ╚═╝ ╚═════╝ ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝

    ===============================
    -- Created By IntelEye. V 1.0
    ===============================
    """)

def urla():
    global url
    url = input("Enter your domain$ ")
    if 'https://' or 'http://' not in str(url):
        pass
        response = requests.get(url)


app = typer.Typer(add_completion=False)

@app.command()
def status_code():
    now = datetime.datetime.now()
    stat = input("Enter domain name$ ")
    page = requests.get(stat)
    if page.status_code == 200:
        good = typer.style("[=]The request has succeeded and the domain is reachable", fg=typer.colors.GREEN)
        typer.echo(good)
        print("[=]", page.status_code)
        print("[=]", now.strftime("%Y-%m-%d %H:%M:%S"))
    else:
        bad = typer.style("[=] This domain is currently not reachable", fg=typer.colors.RED)
        typer.echo(bad)
        typer.echo(page.status_code)
        print("[=]", now.strftime("%Y-%m-%d %H:%M:%S"))


@app.command()
def who_is():
    import whois
    now = datetime.datetime.now()
    page = input("Enter your domain$ ")
    response = whois.whois(page)
    for key, value in page.items():
        print(f"[=]{key} : {value}")
    print("[=]", now.strftime("%Y-%m-%d %H:%M:%S"))


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
    page = input("Enter your domain$ ")
    response = requests.get(page)
    hea = response.headers
    for key, value in hea.items():
        print(f"[=]{key} : {value}")

@app.command()
def builtwith():
    import builtwith
    response = input("Enter your domain$ ")
    page = builtwith.parse(response)
    for key, value in page.items():
        frameworks = ",".join(value)
        print(f"[=]{key} : {frameworks}")


# def choose_file():
#     global file
#     file = input("Enter the file path$ ")
#     if '.txt'in str(file):


if __name__ == "__main__":
    app()
