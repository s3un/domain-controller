import csv
import requests
import typer

def uploads():
    filepath = input("[+]Enter file path: ")
    if filepath.endswith('.txt'):
        file = open(filepath, 'r')
        for value in file:
            framework = value[0]
            response = requests.get(framework)
            print(f"[+]{value[0]} : ", response.status_code)
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



