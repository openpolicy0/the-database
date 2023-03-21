import os, rich, sys
from rich import print
from time import sleep
from rich.console import Console
from rich.text import Text
from rich.panel import Panel
from rich.table import Table
from rich import box

print("""[bold red]
 _____ _          ____        _     _               
|_   _| |_ ___   |    \ ___ _| |___| |_ ___ ___ ___ 
  | | |   | -_|  |  |  | .'| . | .'| . | .'|_ -| -_|
  |_| |_|_|___|  |____/|__,|___|__,|___|__,|___|___|
[/bold red]""")
print("[yellow]type help for more info[/yellow]")
try:
    def menu():
        data = input("[data]: ")
        if data=="help":
           help()
        elif data=="-h":
             help()
        elif data=="--help":
             help()
        elif data=="mkfil":
             mkfil()
        elif data=="add":
             add()
        elif data=="read":
             read()
        elif data=="delete":
             delete()
        else:
            print("[bold red]command not found[/bold red]")
            menu()

    def help():
        print("""[bold yellow]
        help           list help menu (help -h --help)
        mkfil          make your file
        add            add some data to your file
        read           read a file and output it to the screen
        delete         delete the file you made
        [/bold yellow]""")
        menu()

    def mkfil():
        fn = input("[data] file name: ")
        f = open(fn, "w")
        print("[bold white][INFO] importing file[/bold white]")
        sleep(2)
        print("[bold white][INFO] making file[/bold white]")
        sleep(1)
        f.write("+----------------------------------------------------------------------------------------------+")
        f.write("\n|NEW FILE MADE                                                                                 |")
        f.write("\n+----------------------------------------------------------------------------------------------+")
        print("[bold white][INFO] done[/bold white]")
        menu()

    def add():
        d_file = input("[data]file name: ")
        d_title = input("[data]text title: ")
        d_text = input("[data]text: ")
        if os.path.exists("/home/kali/the-database/"+d_file):
           file_d = open(d_file, "a")
           table=Table(box=box.SQUARE)
           table.add_column("INFO", "text", justify="left")
           table.add_row("FILE", d_file)
           table.add_row("TITLE", d_title)
           table.add_row("TEXT", d_text)
           console=Console()
           console.print(table)
           print("[bold white][INFO] importing text into "+d_file+"[/bold white]")
           sleep(1)
           print("[bold white][INFO] writing text { "+d_text+" } [/bold white]")
           sleep(0.6)
           print("[bold white][INFO] done[/bold white]")
           file_d.write("\n| ["+d_title+"] --> "+d_text)
           file_d.write("\n+-------------------------------------------")
        else:
            print("[bold red]File not found[/bold red]")
        menu()

    def read():
        read_f = input("[data]file name: ")
        print("[bold white][INFO] getting file data[/bold white]")
        sleep(1)
        print("[bold white][INFO] done[/bold white]")
        if os.path.exists("/home/kali/the-database/"+read_f):
           database = open(read_f, "r")
           print("[blue]"+database.read())
        else:
            print("[bold red]File not found[/bold red]")
        menu()

    def delete():
        delete_file = input("[data]file name: ")
        if os.path.exists("/home/kali/the-database/"+delete_file):
           os.remove("/home/kali/the-database/"+delete_file)
        else:
            print("[bold red]File not found[/bold red]")
        menu()

    menu()

except KeyboardInterrupt:
    print("[blue]CTRL + C pressed...[/blue]")
    sys.exit()
