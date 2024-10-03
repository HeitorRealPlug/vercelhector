from flask import Flask, render_template, redirect, request, g
import requests
lista = []


API_KEY = 'live_hWoL5kWbC9W95Fj8aYpY6DMOR2pj0h5eqHjmcpuiTvLOQTqxP2gQkUXu7WPGt16X'
BASE_URL = 'https://api.thedogapi.com/v1/images/search'

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html', Titulo = "Dog Generator")

@app.route('/cadastro')
def cadastro():
    acesso = {'x-api-key': API_KEY}
    solicitacao = requests.get(BASE_URL, headers=acesso)
    dados = solicitacao.json()
    imagemdogato = dados[0]['url']
    return render_template('cadastro.html', Titulo="Dog Generator", imagem=imagemdogato)


@app.route('/criar', methods=['POST'])
def criar():
    imagem = request.form['url']
    descricao = request.form['descricao']
    info = [descricao,imagem]
    lista.append(info)
    return redirect('/cadastro')




@app.route('/galeria')
def galeria():

    return render_template( 'galeria.html', titulo = 'Dog Generator', imagensbd =lista)








if __name__ == '__main__':
    app.run()