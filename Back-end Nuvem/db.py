from pymongo import MongoClient
import os


MONGO_URI = os.getenv("MONGO_URI", "sua_string_de_conexao")


client = MongoClient(MONGO_URI)
db = client["iot_turbidez"]
coleta = db["leituras"]

def salvar_leitura(valor_turbidez: float):
    coleta.insert_one({
        "turbidez": valor_turbidez,
        "unidade": "NTU",
        "timestamp": datetime.now()
    })
