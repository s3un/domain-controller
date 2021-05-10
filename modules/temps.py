import requests




def fileup():
    filepath = input("[+]Enter file path$ ")
    file = open(filepath, 'r')
    for value in file:
        framework = value[0]
        respose = requests.get(framework)
        print(f"{value} : {respose} ")

fileup()