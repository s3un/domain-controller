import requests
import csv
import typer

def upload():
    filepath = input("[+]Enter file path$ ")
    starter = (typer.style("---------------------------------------------------------------------------------- \n[+] Scanning through files:  ",fg=typer.colors.BLUE))
    print(starter)
    if filepath.endswith('.txt'):
        file = open(filepath, 'r')
        data = file.read()
        for value in data:
            framework = value[0]
            response = requests.get(framework)
            print(f"[+]domain: {value[0]}\n[+]Status code: ", response.status_code, "\n")
    elif filepath.endswith(".csv"):
        starter = (typer.style("---------------------------------------------------------------------------------- \n[+] Scanning through files:  ",fg=typer.colors.BLUE))
        with open(filepath, mode='r') as f:
            reader = csv.reader(f, delimiter=',')
            for value in reader:
                framework = value[0]
                response = requests.get(framework)
                print(f"[+]domain: {value[0]}\n[+]Status code: ", response.status_code, "\n")
    else:
        err = typer.style("[+]File format not supported!", fg=typer.colors.RED)
        typer.echo(err)

upload()
