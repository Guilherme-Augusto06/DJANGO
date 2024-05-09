# DJANGO
# Configuração do Ambiente Virtual e Estrutura do Projeto

Este guia fornecerá instruções sobre como configurar um ambiente virtual e organizar a estrutura do projeto.

## Configuração do Ambiente Virtual

1. Abra o terminal ou prompt de comando.

2. Navegue até o diretório do projeto.

3. Para criar um novo ambiente virtual, execute o seguinte comando:

    ```bash
    python -m venv venv
    ```

    Isso criará um novo diretório chamado `venv` que conterá todos os pacotes instalados localmente.

4. Ative o ambiente virtual. No Windows, execute:

    ```bash
    .\venv\Scripts\Activate.ps1
    ```

    Você saberá que o ambiente virtual está ativado quando o prefixo `(venv)` aparecer à esquerda do prompt de comando.

## Estrutura do Projeto

1. Mantenha as pastas `static` e `templates` fora da pasta do ambiente virtual. A estrutura do projeto pode ser semelhante à seguinte:

    ```
    projeto/
    ├── venv/
    │   ├── ...
    ├── aulaTeste/
    │   ├── aulaTeste/
    │   │   └── ...
    ├── |
    │   ├── hotel/
    |   |   └──... 
    |   ├── db.sqlite
    ├── ├── manage.py
    ├── README.md
    ```

    Coloque arquivos estáticos, como CSS, JavaScript e imagens, na pasta `static`, e arquivos de modelo HTML na pasta `templates`.

## Instalação das Dependências

1. Com o ambiente virtual ativado, instale as dependências necessárias usando o `pip install`. Execute os seguintes comandos:

    ```bash
    pip install Django
    ```

