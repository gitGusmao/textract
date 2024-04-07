# Aplicação Python para Leitura de Arquivos PDF com Textract

Esta é uma aplicação Python que utiliza o serviço Textract da AWS para realizar a leitura de arquivos PDF.

## Pré-requisitos

- Python 3.x instalado
- Conta na AWS com acesso ao serviço Textract
- Credenciais da AWS configuradas localmente

## Instalação

1. Clone este repositório:

    ```bash
    git clone https://github.com/gitGusmao/textract.git
    ```

2. Acesse o diretório do projeto:

    ```bash
    cd textract
    ```

3. Crie um ambiente virtual:

    ```bash
    python -m venv venv
    ```

4. Ative o ambiente virtual:

    - No Windows:

      ```bash
      venv\Scripts\activate
      ```

    - No Linux/Mac:

      ```bash
      source venv/bin/activate
      ```

5. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

6. Configure as credenciais da AWS:

    - Crie um arquivo `credentials` no diretório `~/.aws` com as suas credenciais:

      ```plaintext
      [default]
      aws_access_key_id = SUA_ACCESS_KEY
      aws_secret_access_key = SUA_SECRET_ACCESS_KEY
      ```

    - Crie um bucket S3 para armazenar o PDF

## Uso

1. Execute o script `main.py`:

    ```bash
    python main.py
    ```

2. Insira o caminho do arquivo PDF que deseja ler.

3. Aguarde o processamento do Textract e visualize o resultado.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

Este projeto está licenciado sob a [MIT License](LICENSE).