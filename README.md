## 🚀 Estrutura do Projeto

- **`client/`**  
  - `app.py`: Arquivo responsável pela interface do cliente.

- **`db/`**  
  - `images.db`: Banco de dados SQLite para armazenar os metadados das imagens.
  - `database.py`: Script para criação do banco de dados e inicialização.

- **`server/`**  
  - **`images/`**
    - `original/`: Pasta que armazena as imagens originais.
    - `processed/`: Pasta que armazena as imagens processadas.
  - `server.py`: Script responsável por rodar o servidor.
  - **`libs/`**
    - `processing.py`: Módulo com funções para o processamento de imagens.

## 🛠️ Como Usar

### 1. Instalar Dependências  
No terminal, na pasta raiz do projeto, execute o seguinte comando para instalar as dependências:

```bash
pip install -r requirements.txt
```

### 2. Criar o Banco de Dados (caso não exista)  
Antes de iniciar o servidor, é necessário criar o banco de dados `images.db`, se ele não existir. Para isso:

1. Abra um terminal na pasta raiz do projeto.
2. Navegue até a pasta `db`:

   ```bash
   cd db
   ```

3. Execute o comando para rodar o script `database.py`:

   ```bash
   py database.py  # ou python database.py ou python3 database.py
   ```

### 3. Iniciar o Servidor  
Após a criação do banco de dados, inicie o servidor:

1. Abra um novo terminal na pasta raiz do projeto.
2. Navegue até a pasta `server`:

   ```bash
   cd server
   ```

3. Execute o comando para rodar o servidor:

   ```bash
   py server.py  # ou python server.py ou python3 server.py
   ```

### 4. Iniciar o Cliente  
Por fim, inicie o cliente:

1. Abra um novo terminal na pasta raiz do projeto.
2. Navegue até a pasta `client`:

   ```bash
   cd client
   ```

3. Execute o comando para rodar o cliente:

   ```bash
   py app.py  # ou python app.py ou python3 app.py
   ```

---

🎉 Após esses passos, o servidor estará rodando e o cliente estará pronto para interagir com o sistema!
