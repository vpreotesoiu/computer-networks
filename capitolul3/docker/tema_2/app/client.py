import sys
from scapy.all import IP, UDP, Raw, send

if len(sys.argv) != 2:
    print("Utilizare: python client.py <adresa_server>")
    sys.exit(1)

SERVER_IP = sys.argv[1]
SERVER_PORT = 9999
MESSAGE = "Salut de la Vlad Preotesoiu!"

try:
    # Crează pachetul IP
    packet = IP(src="123.100.123.100", dst=SERVER_IP) / UDP(sport=12345, dport=SERVER_PORT) / Raw(load=MESSAGE)

    # Trimite pachetul
    print(f"Trimit pachet UDP către {SERVER_IP}:{SERVER_PORT}...")
    send(packet, verbose=True)
    print("Pachet trimis.")

except Exception as e:
    print(f"Eroare la trimiterea pachetului: {e}")
