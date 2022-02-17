from typing import Optional
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

@app.get("/")
def raiz():
    return {"ola": "Mundo"}

class Usuario(BaseModel):
    id: int
    email: str
    senha: str

base_de_dados = [
    Usuario(id=1, email="marcelo@marcelo.com.br", senha="senha123"),
    Usuario(id=2, email="junior@marcelo.com.br", senha="pwd123")
]

@app.get("/usuarios")
def get_todos_usuarios():
    return base_de_dados

@app.get("/usuarios/{id_usuario}", status_code=200)
def get_usuario_usando_id(id_usuario):
    for usuario in base_de_dados:
        if(usuario.id == id_usuario):
            return usuario

    return {"Status": 404, "Mensagem": "Não encontrou Usuario"}

@app.post("/usuarios", status_code=201)
def insere_usuario(usuario: Usuario):
    for usuarios in base_de_dados:
        if (usuarios.id != usuario.id and usuarios.email != usuario.email):
            base_de_dados.append(usuario)
            return usuario
        else:
            return 'usuario ja cadastrado no banco de dados'
