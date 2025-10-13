import network
import time

SSID = "SEU_SSID" #nome da rede
PASSWORD = "SUA_SENHA" #senha da rede

def conecta_wifi():
    wlan = network.WLAN(network.STA_IF) #cria interface wifi (cliente)
    wlan.active(True) #ativa o wifi
    if not wlan.isconnected(): #verifica se ja esta conectado
        print("Conectando ao Wi-Fi...") 
        wlan.connect(SSID, PASSWORD) 
        while not wlan.isconnected():
            time.sleep(1)
            print(".")
    print("Conectado ao Wi-Fi!")
    print("Configuração de rede:", wlan.ifconfig())
    return wlan

wifi = conecta_wifi()
