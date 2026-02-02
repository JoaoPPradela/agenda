from typing import Self

from models.database import Database

class Tarefa:
    def __init__(self: Self, titulo_tarefa: str, data_conclusao =None)-> None:
        self.titulo: str = titulo_tarefa
        self.data_conclusao: str  = data_conclusao 
    def salvar_tarefa(self: Self)-> None:
        with Database('./data/tarefas.sqlite3') as db:
            query: str = " INSERT INTO tarefas (titulo_tarefa, data_conclusao) VALUES (?, ?);"
            params: tuple = (self.titulo, self.data_conclusao)
            db.executar(query, params)    