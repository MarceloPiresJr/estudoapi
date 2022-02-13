from urllib import response
from flask import Flask, request
from teste import insertUsuario

app = Flask(__name__)

@app.route("/olamundo", methods=["GET"])
def olaMundo():
    return {"ola": "mundo"}

@app.route("/cadastra/usuario", methods=["POST"])
def cadastraUsuario():
    body = request.get_json()

    if ("nome" not in body):
        return {400, "O paramentro nome é obrigatorio"}

    if ("email" not in body):
        return {400, "O paramentro email é obrigatorio"}

    if ("senha" not in body):
        return {400, "O paramentro senha é obrigatorio"}

    usuario = insertUsuario(body["nome"], body["email"], body["senha"])
    return geraResponse(200, "Usuario Criado", "User", usuario)

def geraResponse(status, mensagem, nome_do_conteudo=False, conteudo=False):
    response = {}
    response["status"] = status
    response["mensagem"] = mensagem

    if(nome_do_conteudo and conteudo):
        response[nome_do_conteudo] = conteudo
    
    return response

app.run()