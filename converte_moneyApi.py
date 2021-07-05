from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

# Rota Raiz
@app.get("/")
def raiz():
    return{"Ola Mundo!"}


# Criar model
class Usuario(BaseModel):
    id: int
    email: str
    senha: str

# Cria a Base de dados

base_de_dados = [
    Usuario(id=1, email="aleleonel@gmail.com", senha="ale123"),
    Usuario(id=2, email="aleleonelcomercial@gmail.com", senha="ale456")
]

# Rota Get All
@app.get("/usuarios")
def get_todos_os_usuarios():
    return base_de_dados

# Rota Get id
@app.get("/usuarios/{id_usuario}")
def get_usuario_usando_id(id_usuario: int):
    for usuario in base_de_dados:
        if(usuario.id == id_usuario):
            return usuario
    
    return {"status": 404, "Mensagem": "Usuário não encontrado!"}

# Rota Insere
@app.post("/usuario")
def insere_usuario(usuario: Usuario):
    base_de_dados.append(usuario)
    return usuario