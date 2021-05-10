from modules.main import app
from modules.onion import onionapp
import typer

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

def homep():
    home = input("Domain controller is a clear web and dark web reconnaisance tool.\n[+] clearweb\n[+] darkweb\n[+] Quit\n[+]Select your web$ ")
    if "clearweb" == home:
        while True:
            app()
            command = input("[+]Enter command$ ")
    elif "darkweb" == home:
        try:
            onionapp()
            command = input("[+]Enter command$ ")
            if "builtwith" == command:
                from modules.onion import builtwith
                builtwith()
            elif "onionheader" == command:
                from modules.onion import onionheader
                onionheader()
            elif "status-code" == command:
                from modules.onion import status_code
                status_code()
        except:
            print("still loading")
    else:
        typer.style("[+]")
homep()