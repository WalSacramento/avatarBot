# Bot de Avatar do Telegram

Este é um bot do Telegram que permite aos usuários enviar uma foto e receber de volta a foto com um avatar sobreposto. A imagem é ajustada para uma proporção de 1:1, aplicando um desfoque nas áreas adicionadas para manter a proporção.

## Funcionalidades

- Recebe uma foto do usuário.
- Ajusta a foto para uma proporção de 1:1, aplicando desfoque nas áreas adicionadas.
- Sobrepõe um avatar na foto ajustada.
- Envia a imagem resultante de volta para o usuário.

## Pré-requisitos

- Python 3.6 ou superior
- Conta no Telegram para criar um bot e obter um token API

## Instalação

1. Clone o repositório para o seu ambiente local:

    ```sh
    git clone https://github.com/seu-usuario/seu-repositorio.git
    cd seu-repositorio
    ```

2. Crie um ambiente virtual (opcional, mas recomendado):

    ```sh
    python -m venv venv
    source venv/bin/activate  # No Windows, use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```sh
    pip install -r requirements.txt
    ```

4. Crie um arquivo `.env` na raiz do projeto e adicione o seu token API do Telegram:

    ```plaintext
    TELEGRAM_API_TOKEN=seu-token-api
    ```

5. Coloque a imagem do avatar na pasta `assets` com o nome `banner_Val.png`.

## Uso

1. Execute o bot:

    ```sh
    python avatarBot.py
    ```

2. No Telegram, envie uma foto para o bot. O bot ajustará a foto para uma proporção de 1:1, aplicará um desfoque nas áreas adicionadas, sobreporá o avatar e enviará a imagem resultante de volta para você.

## Estrutura do Projeto

```plaintext
seu-repositorio/
├── assets/
│   └── avatar.png
├── avatarBot.py
├── requirements.txt
└── .env