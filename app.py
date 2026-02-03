from flask import Flask, render_template, request, redirect, url_for
from models.tarefa import Tarefa

app = Flask(__name__)

# Lista Global para guardar as tarefas
lista_de_tarefas = [] 

@app.route('/')
def home():
    return render_template('home.html', titulo='Home')

@app.route('/agenda', methods=['GET','POST'])
def agenda():
    if request.method == 'POST':
        titulo_tarefa = request.form['titulo-tarefa']
        data_conclusao = request.form['data-conclusao']
        
        # Cria a tarefa e salva
        nova_tarefa = Tarefa(titulo_tarefa, data_conclusao)
        nova_tarefa.salvar_tarefa()
        
        # Adiciona na lista global
        lista_de_tarefas.append(nova_tarefa)
        return redirect(url_for('agenda'))

    # Se for GET (apenas carregando a página), mostramos a lista
    return render_template('agenda.html', titulo='Agenda', tarefas=lista_de_tarefas)

@app.route('/ola')
def ola_mundo():
    return "Olá, Mundo!"

if __name__ == '__main__':
    app.run(debug=True)