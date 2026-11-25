import ipaddress


try:
    direccion = ipaddress.IPv4Interface(input("Introduce una dirección IPv4 con máscara CIDR: "))
    red = direccion.network
    hosts_disponibles = red.num_addresses - 2 if red.prefixlen <= 30 else red.num_addresses

    print(f"Dirección de red: {red.network_address}")
    print(f"Dirección de broadcast: {red.broadcast_address}")
    print(f"Hosts disponibles: {hosts_disponibles}")
    if red.prefixlen <= 30:
        print(f"Primera IP usable: {red.network_address + 1}")
        print(f"Última IP usable: {red.broadcast_address - 1}")
except ValueError:
    print("Entrada no válida. Introduce una dirección IPv4 con máscara CIDR, por ejemplo 192.168.1.10/24.")