from flask import Flask, redirect, render_template, request, url_for
from models.database import init_db
from models.tarefa import Tarefa

app = Flask(__name__)

init_db()

@app.route('/')
def home():
    return render_template('home.html', titulo='Home')

@app.route('/agenda', methods=['GET','POST'])
def agenda():
    tarefas = None

    if request.method == 'POST':
        titulo_tarefa = request.form['titulo-tarefa']
        data_conclusao = request.form['data-conclusao']
        tarefa = Tarefa(titulo_tarefa, data_conclusao)
        tarefa.salvar_tarefa()

    tarefas = Tarefa.obter_tarefas()
    return render_template('agenda.html', titulo='Agenda', tarefas=tarefas)

@app.route('/delete/<int:idTarefa>')
def delete(idTarefa):
    tarefa = Tarefa.id(idTarefa)
    tarefa.excluir_tarefa()
    # return render_template('agenda.html', titulo="Agenda",
    # tarefa=tarefas)
    return redirect(url_for('agenda'))

@app.route('/update/<int:idTarefa>', methods=['GET', 'POST']) 
def update(idTarefa):
    tarefas = None

    if request.method == 'POST':
        titulo_tarefa = request.form['titulo-tarefa']
        data_conclusao = request.form['data-conclusao']
        tarefa = Tarefa(titulo_tarefa, data_conclusao, idTarefa)
        tarefa.atualizar_tarefas()

    tarefas = Tarefa.obter_tarefas()
    tarefa_selecionada = Tarefa.id(idTarefa)
    return render_template('agenda.html', titulo=f'Editando a tarefa ID: {idTarefa}',tarefa_selecionada=tarefa_selecionada, tarefas=tarefas )

@app.route('/concluir/<int:idTarefa>', methods=['GET', 'POST'])
def concluir(idTarefa):
    tarefa = Tarefa.id(idTarefa)
    tarefa.concluir_tarefa()
    return redirect(url_for('agenda'))

@app.route('/ola')
def ola_mundo():
    return "Olá, Mundo!"