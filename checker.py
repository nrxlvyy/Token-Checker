##########################
#     TOKEN CHECKER      #
#    .gg/aquaticraider   #
#       by nrxlvyy       # 
##########################

try:
    import os
    import time
    import json
    import requests
    import threading

    from colorama import Fore
    from pystyle import Colors, Colorate

except:
    os.system('pip install Fore')
    os.system('pip install pystyle')
    os.system('pip install requests')
    os.system('pip install colorama')

with open('data/config.json', 'r') as file:
    data = json.load(file)
    hide = data.get('hide tokens')
    usethreads = data.get('threading')

tokens = open("data/tokens.txt", "r", encoding="utf8").read().splitlines()

def headers(token):
    return {
        'authorization': token,
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36',
        'content-type': 'application/json',
        'accept': '*/*',
        'accept-language': 'en-US;q=0.9,en;q=0.8',
        'cache-control': 'max-age=0',
        'connection': 'keep-alive',
        'referer': 'https://discord.com/',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'sec-gpc': '1',
        'origin': 'https://discord.com'
    }

W = Fore.RESET
C = Fore.LIGHTCYAN_EX
B = Fore.LIGHTBLACK_EX
V = Fore.GREEN
L = Fore.LIGHTYELLOW_EX
I = Fore.LIGHTRED_EX

class ui:
    def ui():
        ui.clear()
        ui.banner()
        ui.menu()

    def clear():
        os.system('cls')

    def banner():
        banner = ("""  
                  
         ▄▄▄· .▄▄▄  ▄• ▄▌ ▄▄▄· ▄▄▄▄▄▪   ▄▄· 
        ▐█ ▀█ ▐▀•▀█ █▪██▌▐█ ▀█ •██  ██ ▐█ ▌▪
        ▄█▀▀█ █▌·.█▌█▌▐█▌▄█▀▀█  ▐█.▪▐█·██ ▄▄
        ▐█ ▪▐▌▐█▪▄█·▐█▄█▌▐█ ▪▐▌ ▐█▌·▐█▌▐███▌
         ▀  ▀ ·▀▀█.  ▀▀▀  ▀  ▀  ▀▀▀ ▀▀▀·▀▀▀  
                  
            [!] discord.gg/aquaticraider 
                [!] made by nrxlvyy   
        """)
        print(Colorate.Horizontal(Colors.green_to_cyan, banner, 1))

    def menu():
        print(f"""
                {C}[{W}01{C}]{W} {W}CHECK TOKENS
                {C}[{W}02{C}]{W} {W}CLEAR FILES
                {C}[{W}03{C}]{W} {W}EXIT
            
        """)

        choice = input(Colorate.Horizontal(Colors.green_to_cyan, "Choice: ", 1))

        if choice == "":
            ui.ui()

        elif choice in ("01", "1"):
            ui.clear()
            ui.banner()
        
            if usethreads == "true":
                threads = []
                for token in tokens:
                    thread = threading.Thread(target=checker.checker, args=(token,))
                    threads.append(thread)
                    thread.start()

                for thread in threads:
                    thread.join()

                print(Colorate.Horizontal(Colors.green_to_cyan, "Done checking. Returning in 10 seconds ", 1))

                time.sleep(10)
                ui.ui()

            else:
                print(Colorate.Horizontal(Colors.green_to_cyan, "[!] set threading in config.json for faster checking", 1))

                for token in tokens:
                    checker.checker(token)
                    
                print(Colorate.Horizontal(Colors.green_to_cyan, "Done checking. Returning in 10 seconds ", 1))

                time.sleep(10)
                ui.ui()

        elif choice in ("02", "2"):
            with open('data/valid.txt', 'w') as file: 
                file.write('')

            with open('data/locked.txt', 'w') as file: 
                file.write('')
                
            print(Colorate.Horizontal(Colors.green_to_cyan, "Done clearing. Returning...", 1))

            time.sleep(3)
            ui.ui()
            
        elif choice in ("03", "3"):
            exit()
        
        else:
            ui.ui()

class checker:
    valid = 0
    locked = 0
    invalid = 0

    @classmethod
    def checker(cls, token):
        os.system(f'title Aquatic Checker / Valid: {cls.valid} / Locked: {cls.locked} / Invalid: {cls.invalid}')

        header = headers(token)

        r = requests.get('https://discord.com/api/v9/users/@me', headers=header)

        if r.status_code == 200:
            cls.valid += 1

            tokenis = f"{V}VALID"

            with open('data/valid.txt', 'a') as valid_file:
                valid_file.write(token + '\n')

        elif r.status_code == 403:
            cls.locked += 1

            tokenis = f"{L}LOCKED"

            with open('locked.txt', 'a') as locked_file:
                locked_file.write(token + '\n')

        else:
            cls.invalid += 1

            tokenis = f"{I}INVALID"
            
        data = json.loads(r.text)
        username = data.get('username')
        tid = data.get('id')

        if data.get('premium_type') == 2:
            nitro = "Boost"
        elif data.get('premium_type') == 1:
            nitro = "Basic"
        else:
            nitro = "False"

        if data.get('verified') is None:
            ev = "False"
        else:
            ev = "True"
                
        if data.get('phone') is None:
            fv = "False"
        else:
            fv = "True"

        if hide == "true":
            t = token.split(".")[0]
        else:
            t = token

        tid = str(tid) if tid is not None else "None"
        username = username if username is not None else "None"

        print(f"{tokenis.ljust(12)} {B}| {C}Token: {W}{t}{'***'.rjust(21 - len(t))} {B}| {C}ID: {W}{tid.ljust(19)} {B}| {C}User: {W}{username.ljust(20)} {B}| {C}Nitro: {W}{nitro.ljust(5)} {B}| {C}EV: {W}{ev.ljust(5)} {B}| {C}FV: {W}{fv}")

os.system(f'title Aquatic Checker')
ui.ui()
