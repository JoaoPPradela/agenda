from sqlite3 import Cursor
from typing import Optional, Self, Any
from models.database import Database

class Tarefa:
    """
    Representa uma tarefa e lida com todas as operações no banco de dados.
    """
    
    # Criação do objeto na memória com os dados da tarefa
    def __init__(self: Self, titulo_tarefa: Optional[str], data_conclusao: Optional[str]= None, id_tarefa: Optional[int] = None, concluida: Optional[int] = 0) -> None:
        self.titulo_tarefa: Optional[str] = titulo_tarefa
        self.data_conclusao: Optional[str] = data_conclusao
        self.id_tarefa: Optional[int] = id_tarefa
        self.concluida: Optional[int] = concluida

    # Busca de dados (Selects) 
    @classmethod
    def id(cls, id: int) -> Self:
        """ Busca uma única tarefa pelo número do ID """
        with Database() as db:
            query: str = 'SELECT titulo_tarefa, data_conclusao, concluida FROM tarefas WHERE id = ?;'
            params: tuple = (id,)
            resultado = db.buscar_tudo(query, params)
            
            # Pega os dados da lista retornada e coloca em variáveis
            [[titulo, data, concluida]] = resultado

        return cls(id_tarefa=id, titulo_tarefa=titulo, data_conclusao=data, concluida=concluida)
        
    @classmethod
    def obter_tarefas(cls) -> list[Self]:
        """ Lista todas as tarefas que estão salvas no banco """
        with Database() as db:
            query: str = 'SELECT titulo_tarefa, data_conclusao, id, concluida FROM tarefas;'
            resultados: list[Any] = db.buscar_tudo(query)
            # Transforma cada linha do banco em um objeto Tarefa do Python
            tarefas: list[Any] = [cls(titulo, data, id, concluida) for titulo, data, id, concluida in resultados]
            return tarefas

    # Ações de salvar e deletar dados (Insert, Update, Delete)
    def salvar_tarefa(self: Self)-> None:
        """ Salva uma nova tarefa no banco de dados """
        with Database() as db:
            query: str = " INSERT INTO tarefas (titulo_tarefa, data_conclusao, concluida) VALUES (?, ?, ?);"
            params: tuple = (self.titulo_tarefa, self.data_conclusao, self.concluida)
            db.executar(query, params)

    def excluir_tarefa(self) -> Cursor:
        """ Apaga a tarefa do banco usando o ID """
        with Database() as db:
            query: str = 'DELETE FROM tarefas WHERE id = ?;'
            params: tuple = (self.id_tarefa,)
            resultado: Cursor = db.executar(query, params)
            return resultado
    
    # Atualizações de status (Editar/Concluir) e reabertura de tarefas.
    def atualizar_tarefas(self) -> Cursor:
        """ Altera o título ou data de uma tarefa já existente """
        with Database() as db:
            query: str = 'UPDATE tarefas SET titulo_tarefa = ?, data_conclusao = ?, concluida = 0 WHERE id = ?;'
            params: tuple = (self.titulo_tarefa, self.data_conclusao, self.id_tarefa)
            resultado: Cursor = db.executar(query, params)
            return resultado
            
    def concluir_tarefa(self) -> Cursor:
        """ Muda o status da tarefa para 'Finalizada' (1) """
        with Database() as db:
            query: str = 'UPDATE tarefas SET titulo_tarefa = ?, data_conclusao = ?, concluida = 1 WHERE id = ?;'
            params: tuple = (self.titulo_tarefa, self.data_conclusao, self.id_tarefa)
            resultado: Cursor = db.executar(query, params)
            return resultado
    
    def reabrir_tarefa(self) -> Cursor:
        """ Volta o status da tarefa para 'Pendente' (0) """
        with Database() as db:
            query: str = 'UPDATE tarefas SET titulo_tarefa = ?, data_conclusao = ?, concluida = 0 WHERE id = ?;'
            params: tuple = (self.titulo_tarefa, self.data_conclusao, self.id_tarefa)
            resultado: Cursor = db.executar(query, params)
            return resultado