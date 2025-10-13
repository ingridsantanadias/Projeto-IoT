from fastapi import FastAPI
from datetime import datetime
import requests

app = FastAPI()

THINGSPEAK_API_KEY = "EK2M8D6JGL4O3XW2"  

@app.get("/")
def home():
    return {"mensagem": "API rodando com sucesso 🚀"}

@app.post("/turbidez/{valor}")
def enviar_para_thingspeak(valor: float):
    dado = {
        "api_key": THINGSPEAK_API_KEY,
        "field1": valor
    }

    resposta = requests.post("https://api.thingspeak.com/update", params=dado)

    if resposta.status_code == 200:
        return {
            "mensagem": "Valor enviado ao ThingSpeak com sucesso s2",
            "valor": valor,
            "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    else:
        return {"erro": "Falha ao enviar pro ThingSpeak X", "detalhe": resposta.text}

