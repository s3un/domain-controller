import requests
import typer

# f = open("C:\\Users\\USER\\Documents\\dtry.txt", "r")
# data = f.read( )
# f.close( )
# print(data)


def upload():
    filepath = input("[+]Enter file path$ ")
    starter = (typer.style("---------------------------------------------------------------------------------- \n[+] Scanning through files:  ",fg=typer.colors.BLUE))
    print(starter)
    if filepath.endswith('.txt'):
        file = open(filepath, 'rb')
        data = file.read()
        file.close()
        for value in data:
            framework = value[0]
            response = requests.get(framework)
            print(f"[+]domain: {value[0]}\n[+]Status code: ", response.status_code, "\n")

upload()