from sqlite3 import Connection, connect, Cursor
from typing import Any, Optional, Self, Type
from types import TracebackType
from dotenv import load_dotenv
import traceback
import os

# Configurações Iniciais e Variáveis de Ambiente
load_dotenv() # Procura um arquivo .env com variáveis 
DB_PATH = os.getenv('DATABASE', './data/tarefas.sqlite3')

# --- Função de Inicialização do Banco de Dados ---
def init_db(db_name: str = DB_PATH):
    """ Cria a tabela tarefas caso ela ainda não exista no arquivo especificado """
    with connect(db_name) as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS tarefas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo_tarefa TEXT NOT NULL,
            data_conclusao TEXT,
            concluida INTEGER DEFAULT 0    
        );
        """)

#Classe de Gerenciamento do Banco de Dados 
class Database:
    """
        Classe que regencia conexões e operações com o banco de dados SQLitre. 
        Utiliza o protocolo de gerenciamento de contxtos para garantir qua a conexão seja encerrada corretamente
    """
    
    # Inicialização da classe e criação da tabela
    def __init__(self, db_name: str = DB_PATH) -> None:
        self.connection: Connection = connect(db_name)
        self.cursor: Cursor = self.connection.cursor()
        self.executar("""
        CREATE TABLE IF NOT EXISTS tarefas (
         id INTEGER PRIMARY KEY AUTOINCREMENT,
         titulo_tarefa TEXT NOT NULL,
         data_conclusao TEXT,
         concluida INTEGER DEFAULT 0);
        """)

    # Métodos para execução de comandos SQL e consultas
    def executar(self, query: str, params: tuple = ()) -> Cursor:
        """ Executa comandos de alteração (INSERT, UPDATE, DELETE) e commita as mudanças """
        self.cursor.execute(query, params)
        self.connection.commit()
        return self.cursor

    def buscar_tudo(self, query: str, params: tuple = ()) -> list[Any]:
        """ Executa consultas (SELECT) e retorna todos os resultados encontrados """
        self.cursor.execute(query, params)
        return self.cursor.fetchall()

    def close(self) -> None:
        """ Encerra a conexão com o banco de dados """
        self.connection.close()

    # Métodos para o Gerenciamento de Contexto (with) 

    # Método de entrada do contexto
    def __enter__(self) -> Self:
        """ Retorna a própria instância ao entrar no bloco 'with' """
        return self

    # Método de saída do contexto
    def __exit__(
        self,
        exc_type: Optional[Type[BaseException]],
        exc_value: Optional[BaseException   ],
        tb: Optional[TracebackType],
    ) -> None:
        """ 
        Garante o fechamento da conexão ao sair do bloco 'with' e 
        realiza o log de erros caso ocorra alguma exceção 
        """
        if exc_type is not None:
            print("Exceção capiturar no contexto: ")
            print(f"Tipo: {exc_type.__name__}")
            print(f"Mensagem: {exc_value}")
            print("Traceback completo:")
            traceback.print_tb(tb)

        self.close()