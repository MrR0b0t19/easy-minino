# easy-minino
Script para entender mejor el minino

# Script para el Análisis de Archivos .pcap con Minino

## Introducción

Este Script está diseñado para ayudarte en el análisis de archivos .pcap generados por la herramienta Minino, creada por Electronic Cats. El archivo .pcap que genera Minino contiene paquetes de red capturados durante el escaneo, y este script te ayudará a interpretar esos datos, incluso si no tienes experiencia previa en análisis de red.

## ¿Qué es un archivo .pcap?

Un archivo .pcap (Packet Capture) es un formato que almacena los paquetes de datos que viajan a través de una red. Esta información es muy útil para analizar la comunicación entre dispositivos, identificar problemas de red o simplemente observar el tráfico.

## ¿Qué es Minino?

Minino es una herramienta desarrollada por Electronic Cats que escanea redes locales para identificar dispositivos IoT. Cuando ejecutas Minino, captura el tráfico de la red y genera un archivo .pcap que contiene todos los paquetes de red asociados a los dispositivos detectados.

## Requisitos

Antes de empezar, debes tener claro que para usuarlo ya debes tener el archivo descargado, si no cuentas con el revisa la documentacion de electronic cats, despues en tu terminal instala "scapy" usando pip install scapy.

## Instrucciones para analizar el archivo .pcap

1. Captura el tráfico de la red con Minino: Ejecuta Minino. Esto generará un archivo .pcap con todos los paquetes capturados.

2. Abre el archivo .pcap en Wireshark:
   - Inicia Wireshark y abre el archivo .pcap.
   - En Wireshark podrás ver una lista detallada de todos los paquetes de red.
   - esto es el caso normal y el generico

3. Utiliza el script para facilitar la interpretación: Si no deseas o desconoces como analizar cada paquete manualmente, puedes usar el script que he creado para extraer información relevante y presentarla de manera más amigable. El script puede identificar dispositivos IoT, mostrar las direcciones IP y MAC, y resaltar los tipos de paquete.

   - Instrucciones de uso del script:
     1. Ejecuta el script en tu entorno de desarrollo o en kali.
     2. Proporciona el archivo .pcap como entrada al script.
     3. El script procesará el archivo y te mostrará un resumen fácil de entender.

4. Interpretación de los resultados:
   
   - Tipo de paquete: te muestra el tipo de paquete beacon/probe response/data/etc
   - SSID: El  nombre del AP.
   - Dirección MAC: Cada dispositivo tiene una dirección MAC única que se utiliza para identificarlo en la red.
   - canal: canal de comunicacion donde se encuentra la red.
  
para mas informacion revisar documentacion de minino
   

## Ejemplo de Resultado en Wireshark

A continuación se muestra cómo se verían los resultados del archivo .pcap en Wireshark. En esta imagen, puedes ver una lista de paquetes capturados, con detalles como la dirección IP, el protocolo utilizado y los puertos involucrados.

![image](https://github.com/user-attachments/assets/80f64d1a-b5c9-4927-ab76-bcf45aea564e)


## Ejemplo de Salida del Script

El script que creé simplifica la salida de los resultados, presentando un resumen claro de los dispositivos detectados en la red. Aquí tienes un ejemplo de cómo se verá la salida:

![image](https://github.com/user-attachments/assets/22097f4f-2526-4533-afba-f419fd54f7c5)


## Conclusión

Con este README y el script proporcionado, ahora puedes analizar y comprender mejor los archivos .pcap generados por Minino. Aunque el proceso de análisis de paquetes puede ser complejo, este enfoque te ayudará a obtener información relevante de manera más sencilla. Si tienes alguna duda o pregunta, no dudes en ponerte en contacto conmigo.

---

Este enfoque debería hacer que el proceso sea más accesible para usuarios novatos, guiándolos paso a paso y proporcionándoles ejemplos visuales y claros. ¡Espero que sea útil!

----

## Redes sociales

# Instagram:
https://www.instagram.com/arnoldm_y19/profilecard/?igsh=MTUwc2Z3ZjJmaWZmbA==

# Tiktok
https://www.tiktok.com/@fan_tasma?_t=8rh15oWyhC4&_r=1

# X / Twitter
https://x.com/arnoldmy0?s=21
