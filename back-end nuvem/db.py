from pymongo import MongoClient

# Conexão com Mongo Atlas
uri = "mongodb+srv://api_user:DANILLY20@cluster0.i20lea8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri)

# Definindo banco e coleção
db = client["iot_turbidez"]
turbidez_collection = db["turbidez"]

# Função para salvar leitura
def salvar_leitura(valor):
    turbidez_collection.insert_one({"valor": valor})

# Função para listar leituras
def listar_leituras():
    return list(turbidez_collection.find({}, {"_id": 0}))
