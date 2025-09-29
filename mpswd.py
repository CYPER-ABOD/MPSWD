import os; os.system('cls' if os.name == 'nt' else 'clear')
import secrets
import string
import time
import sys
from colorama import Fore, Style, init

init(autoreset=True)

def display_logo():
    logo = f"""
{Fore.YELLOW}{Style.BRIGHT}
    ███╗   ███╗██████╗ ███████╗██╗    ██╗██████╗ 
    ████╗ ████║██╔══██╗██╔════╝██║    ██║██╔══██╗
    ██╔████╔██║██████╔╝███████╗██║ █╗ ██║██║  ██║
    ██║╚██╔╝██║██╔═══╝ ╚════██║██║███╗██║██║  ██║
    ██║ ╚═╝ ██║██║     ███████║╚███╔███╔╝██████╔╝
    ╚═╝     ╚═╝╚═╝     ╚══════╝ ╚══╝╚══╝ ╚═════╝
{Style.RESET_ALL}
{Fore.CYAN}{Style.BRIGHT}DEVELOPER: CYPER ABOD
{Style.RESET_ALL}
{Fore.CYAN}{Style.BRIGHT}VERSION: 1.0
    """
    print(logo)

def fake_loading():
    print(Fore.YELLOW + Style.BRIGHT + "INITIALIZING TOOL, PLEASE WAIT...\n")
    for i in range(30):  # 30 steps × 0.1s = 3s
        sys.stdout.write(Fore.GREEN + "█")
        sys.stdout.flush()
        time.sleep(0.1)
    print("\n" + Fore.CYAN + Style.BRIGHT + "DONE!\n")

def generate_password(length, use_lower, use_upper, use_digits, use_symbols):
    characters = ""
    if use_lower:
        characters += string.ascii_lowercase
    if use_upper:
        characters += string.ascii_uppercase
    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += string.punctuation

    if not characters:
        print("PLEASE WAIT...")
        time.sleep(2)
        print(Fore.RED + Style.BRIGHT + "ERROR: NO CHARACTER SETS SELECTED!")
        time.sleep(3)
        import os; os.system('cls' if os.name == 'nt' else 'clear')
        return None

    if length < 1 or length > 99:
        print(Fore.BLUE + Style.BRIGHT + "PLEASE WAIT...")
        time.sleep(2)
        print(Fore.RED + Style.BRIGHT + "ERROR: PASSWORD LENGTH MUST BE BETWEEN 1 AND 99!")
        time.sleep(3)
        import os; os.system('cls' if os.name == 'nt' else 'clear')
        return None

    return ''.join(secrets.choice(characters) for _ in range(length))

def main():
    while True:
        display_logo()
        fake_loading()

        try:
            length = int(input(Fore.YELLOW + Style.BRIGHT + "PASSWORD LENGTH (1-99): "))
        except ValueError:
            print(Fore.RED + Style.BRIGHT + "ERROR: PLEASE ENTER A VALID NUMBER!")
            continue                                                                                 
        print(Fore.YELLOW + Style.BRIGHT + "\nCHOOSE CHARACTER SETS (Y/N):"
)
        use_lower = input("INCLUDE LOWERCASE LETTERS (a-z)? ").lower() == "y"
        use_upper = input("INCLUDE UPPERCASE LETTERS (A-Z)? ").lower() == "y"
        use_digits = input("INCLUDE DIGITS (0-9)? ").lower() == "y"
        use_symbols = input("INCLUDE SYMBOLS (!@#$...)? ").lower() == "y"

        password = generate_password(length, use_lower, use_upper, use_digits, use_symbols)

        if password:
            print(Fore.GREEN + Style.BRIGHT + "\nGENERATED PASSWORD: " + Fore.WHITE + Style.BRIGHT + password)
            print(Fore.YELLOW + Style.BRIGHT + "\nPRESS 0 TO RETURN TO TOOL")

            choice = input("> ")
            if choice.strip() == "0":
                continue
            else:
                print(Fore.CYAN + Style.BRIGHT + "\nTHANK YOU FOR USING MPSWD!")
                break

import signal

def _handle_sigint(signum, frame):
    print("\n\nEXITING... THANK YOU FOR USING MPSWD! GOODBYE.")
    raise SystemExit(0)

if __name__ == "__main__":
    # تسجيل معالج Ctrl+C ثم تشغيل البرنامج
    signal.signal(signal.SIGINT, _handle_sigint)
    main()
