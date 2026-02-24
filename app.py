from flask import Flask, redirect, render_template, request, url_for
from models.database import init_db
from models.tarefa import Tarefa

# --- Configuração Inicial do App ---
app = Flask(__name__)

# Cria a tabela no banco de dados assim que o servidor inicia
init_db()

#Rotas de Navegação Simples e Teste
@app.route('/')
def home():
    """ Renderiza a página inicial """
    return render_template('home.html', titulo='Home')

# Rota Principal da Agenda (Listar e Criar) 
@app.route('/agenda', methods=['GET','POST'])
def agenda():
    tarefas = None

    # Se o usuário preencher o formulário e enviar (POST), salva a nova tarefa
    if request.method == 'POST':
        titulo_tarefa = request.form['titulo-tarefa']
        data_conclusao = request.form['data-conclusao']
        tarefa = Tarefa(titulo_tarefa, data_conclusao)
        tarefa.salvar_tarefa()

    # Busca todas as tarefas para exibir na tela
    tarefas = Tarefa.obter_tarefas()
    return render_template('agenda.html', titulo='Agenda', tarefas=tarefas)

# Rota para Excluir Tarefa pela ID
@app.route('/delete/<int:idTarefa>')
def delete(idTarefa):
    """ Busca a tarefa pelo ID e a remove do banco """
    tarefa = Tarefa.id(idTarefa)
    tarefa.excluir_tarefa()
    return redirect(url_for('agenda'))

# Rota para Editar Tarefa 
@app.route('/update/<int:idTarefa>', methods=['GET', 'POST']) 
def update(idTarefa):
    tarefas = None

    # Se o formulário de edição for enviado, atualiza os dados no banco
    if request.method == 'POST':
        titulo_tarefa = request.form['titulo-tarefa']
        data_conclusao = request.form['data-conclusao']
        tarefa = Tarefa(titulo_tarefa, data_conclusao, idTarefa)
        tarefa.atualizar_tarefas()

    # Recarrega a lista e identifica qual tarefa está sendo editada para preencher o form
    tarefas = Tarefa.obter_tarefas()
    tarefa_selecionada = Tarefa.id(idTarefa)
    return render_template('agenda.html', titulo=f'Editando a tarefa ID: {idTarefa}',tarefa_selecionada=tarefa_selecionada, tarefas=tarefas )

# Rotas de Alteração de Status (Concluir/Reabrir)
@app.route('/concluir/<int:idTarefa>', methods=['GET', 'POST'])
def concluir(idTarefa):
    """ Marca a tarefa como feita e volta para a agenda """
    tarefa = Tarefa.id(idTarefa)
    tarefa.concluir_tarefa()
    return redirect(url_for('agenda'))

@app.route('/reabrir/<int:idTarefa>', methods=['GET', 'POST'])
def reabrir(idTarefa):
    """ Marca a tarefa como pendente e volta para a agenda """
    tarefa = Tarefa.id(idTarefa)
    tarefa.reabrir_tarefa()
    return redirect(url_for('agenda'))

# Teste de Rota 
@app.route('/ola')
def ola_mundo():
    return "Olá, Mundo!"