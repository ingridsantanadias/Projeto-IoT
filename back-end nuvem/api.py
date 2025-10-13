from fastapi import FastAPI
from db import turbidez_collection
from datetime import datetime
import uvicorn

app = FastAPI()

# Rota inicial só para teste
@app.get("/")
def home():
    return {"mensagem": "API rodando com sucesso 🚀"}

# Rota para listar leituras de turbidez
@app.get("/turbidez")
def listar_leituras():
    leituras = list(turbidez_collection.find({}, {"_id": 0}))
    return {"leituras": leituras}

# Rota para salvar nova leitura
@app.post("/turbidez/{valor}")
def salvar_leitura(valor: float):
    dado = {
        "valor": valor,
        "data_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    turbidez_collection.insert_one(dado)
    return {"mensagem": "Leitura salva com sucesso ✅", "dado": dado}

if __name__ == "__main__":
    uvicorn.run("api:app", host="127.0.0.1", port=8000, reload=True)
