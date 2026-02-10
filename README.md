# Agenda em Python usando flask 

Este projeto foi desenvolvido para criar uma aplicação de agenda simples usando o framework Flask em Python. Ele permite que os usuários criem, visualizem, editem e excluam tarefas, armazenando as informações em um banco de dados SQLite.
 
 Para implementar este projeto, foram criados os seguintes arquivos:

 1. Faça um fork deste respositório, clicando no botão "Fork"
 
 
 2. Clone este repositório para o seu ambiente local.

  ~~~bash
  git clone <url-seu-repositorio>
  ~~~

  3. Abra o projeto ultilizando seu IDE preferido


  4.Crie, preferencialmente, um ambiente virtual ultilizando uma versão do Python >3.12.10:

  python -m venv .venv

  5. Ative o ambiente virtual:
    ~~~bash 
    source .venv/Scripts/activate

    ~~~


    No powershell

    .\.venv\Scripts\Activate.ps1

    ~~~


    6. Instale as dependências do projeto usando o arquivo requirements.txt:

    ~~~python 
    pip install -r requirements.txt
    ~~~

    7. Copie o arquivo .env.example para .env:

    8. Edite o arquivo .env para configurar o caminho do banco de dados


    9. Rode a aplicação ultilizando o comando:

    ~~~bash
    flask run
    ~~~

    10. Acesse a aplicação no navegador através do endereço:
    `http://localhost:5000`

