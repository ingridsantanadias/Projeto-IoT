import urequests  # Bibliotecas para fazer requisições HTTP
import time

THINGSPEAK_API_KEY = "EK2M8D6JGL4O3XW2" 
THINGSPEAK_URL = "https://api.thingspeak.com/update"

def envia_dado(campo1_valor):
    url = f"{THINGSPEAK_URL}?api_key={THINGSPEAK_API_KEY}&field1={campo1_valor}"
    try:
        response = urequests.get(url)
        if response.status_code == 200:
            print("Dado enviado com sucesso!")
        else:
            print("Erro ao enviar dado:", response.status_code)
        response.close()
    except Exception as e:
        print("Erro na requisição:", e)

while True:
    valor = 25  
    envia_dado(valor)
    time.sleep(15)  
