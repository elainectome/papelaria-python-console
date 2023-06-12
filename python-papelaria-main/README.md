# Papelaria

Este é um projeto em Python com fins didáticos para a disciplina da instituição Fatec de Ribeirão Preto chamada "Tópicos Especiais em Informática".

### Instalação 
Execute os seguintes comandos para instalar as dependências necessárias:
- 'pip install mysql-connector-python'
- 'pip install sqlalchemy'
- 'pip install pymysql'
- 'pip install requests'

### Table 

```sql
CREATE TABLE usuarios (
  id_usuario INT AUTO_INCREMENT PRIMARY KEY,
  nome VARCHAR(255),
  email VARCHAR(255),
  senha VARCHAR(255)
);

CREATE TABLE produtos (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(200),
    preco_venda DECIMAL(10, 2),
    preco_compra  DECIMAL(10, 2),
    grupo VARCHAR(200),
    quantidade_em_estoque INT
);

CREATE TABLE vendas (
    id_venda INT AUTO_INCREMENT PRIMARY KEY,
    id_usuario INT,
    id_produto INT,
    quantidade_comprada INT,
    data_compra DATE,
    valor_total DECIMAL(10, 2),
    FOREIGN KEY (id_usuario) REFERENCES usuarios(id_usuario),
    FOREIGN KEY (id_produto) REFERENCES produtos(id_produto)
);

CREATE TABLE sobreProj (
	id_sobre INT AUTO_INCREMENT PRIMARY KEY,
	sobre VARCHAR(3000)
);
```

### Endereço do banco 
-Mudar de acordo com o tipo do seu database, login, usuario, nome do database

```py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

DATABASE_URI = 'mysql+pymysql://root:root@localhost/papelarias'

engine = create_engine(DATABASE_URI)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
```

### Para rodar
- Compilador de python (rodar pelo arquivo main.py)

### Equipe
- Abner Willian Mioti Manha
- Elaine Cristina Tome
