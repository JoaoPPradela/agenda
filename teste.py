from models.database import Database 

# Teste do gerenciamento de contexto
with Database('./data/tarefas.sqlite3') as db:
    db.executar('''
    CREATE TABLE IF NOT EXISTS tarefas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        titulo_tarefa TEXT NOT NULL,
        data_conclusao TEXT);
    ''')
    db.executar(" INSERT INTO tarefas (titulo_tarefa, data_conclusao) VALUES (?, ?);", ("Usar o gerenciador de contexto", "2026-02-03"))