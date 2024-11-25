#tome como ideal principal para que no repita redes validar todo por mac 
# by: Fan_tasma
from scapy.all import rdpcap, Dot11, Dot11Beacon, Dot11ProbeResp, Dot11Auth, Dot11AssoReq, Dot11Deauth
from tqdm import tqdm
from rich.console import Console
from rich.table import Table

# Función para imprimir los detalles del paquete, evitando imprimir duplicado
def print_packet_info(pkt, printed_macs):
    src_mac = pkt[Dot11].addr2  # Dirección MAC de origen
    dst_mac = pkt[Dot11].addr1  # Dirección MAC de destino
    
    # Si ya hemos impreso esta MAC de origen, no imprimimos
    if src_mac in printed_macs:
        return False  # No imprimimos nada y retornamos False
    
    # Si no hemos mostrado esta MAC de origen, lo hacemos ahora
    printed_macs.add(src_mac)  # Añadimos la MAC de origen al conjunto de impresas
    return True

def analyze_pcap(pcap_file):
    # Leemos el archivo .pcap
    packets = rdpcap(pcap_file)
    printed_macs = set()  # seteamos macs ya impresas

    # Creamos la tabla para mostrar los resultados 
    console = Console()
    table = Table(show_header=True, header_style="bold magenta", title="Redes y Paquetes Analisados")
    table.add_column("Tipo de Paquete", style="bold green")
    table.add_column("SSID", style="bold blue")
    table.add_column("MAC Origen", style="bold yellow")
    table.add_column("MAC Destino", style="bold red")
    table.add_column("Canal", style="bold cyan")

    # Barra de progreso para la carga de los paquetes
    with tqdm(total=len(packets), desc="Cargando resultados", unit="paquete") as loading_bar:
        print(f"\nAnalizando el archivo pcap: {pcap_file}\n")
        print(f"\nby: Fan_tasma\n Analiza los resultados para posteriormente realizar tus pruebas\n\n")

        for pkt in packets:
            loading_bar.update(1)  

            if pkt.haslayer(Dot11):
                # Validar y imprimir información solo si la dirección MAC de origen no ha sido procesada
                if not print_packet_info(pkt, printed_macs):
                    continue  # Si ya se imprimió, saltamos este paquete

                # Si el paquete es un Beacon (paquete de anuncio de red) mas informacion en documentacion
                if pkt.haslayer(Dot11Beacon):
                    ssid = pkt[Dot11Beacon].info.decode(errors='ignore')  # Obtener el SSID de red
                    table.add_row("Beacon", ssid, pkt[Dot11].addr2, pkt[Dot11].addr1, str(pkt[Dot11Beacon].channel))

                # Si el paquete es una respuesta a un Probe Request (Probe Response)
                elif pkt.haslayer(Dot11ProbeResp):
                    ssid = pkt[Dot11ProbeResp].info.decode(errors='ignore')  # Obtener el SSID de red
                    table.add_row("Probe Response", ssid, pkt[Dot11].addr2, pkt[Dot11].addr1, str(pkt[Dot11ProbeResp].channel))

                # Si el paquete es un Authentication Request/Response
                elif pkt.haslayer(Dot11Auth):
                    table.add_row("Authentication", "N/A", pkt[Dot11].addr2, pkt[Dot11].addr1, "N/A")

                # Si el paquete es una solicitud de asociación (Association Request)
                elif pkt.haslayer(Dot11AssoReq):
                    ssid = pkt[Dot11AssoReq].info.decode(errors='ignore')  # Obtener el SSID
                    table.add_row("Association Request", ssid, pkt[Dot11].addr2, pkt[Dot11].addr1, str(pkt[Dot11AssoReq].channel))

                # Si el paquete es una desautenticación (Deauthentication)
                elif pkt.haslayer(Dot11Deauth):
                    table.add_row("Deauthentication", "N/A", pkt[Dot11].addr2, pkt[Dot11].addr1, "N/A")

                # Si el paquete contiene datos (tipo 2 indica datos)
                elif pkt.haslayer(Dot11) and pkt[Dot11].type == 2:  # Tipo 2 indica que es un paquete de datos
                    table.add_row("Data", "N/A", pkt[Dot11].addr2, pkt[Dot11].addr1, "N/A")
        # Imprimimos la tabla con los resultados hermosos
        console.print(table)

if __name__ == "__main__":
    pcap_file = "analizer00.pcap"  # aqui dejamos el nombre identico ya que cada escaneo lo guardxa en automatico el minino asi, lo que recomiendo es mover y eliminar
    analyze_pcap(pcap_file)
