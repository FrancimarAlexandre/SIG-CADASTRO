import sqlite3

class DataBase:
    # criando e conectando banco de dados
    def connect_bd(self):
        self.conn = sqlite3.connect("DATABASE.db")
        self.cursor = self.conn.cursor()
        
        # Criando a tabela
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Cadastro (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome VARCHAR(255) NOT NULL,
                email VARCHAR(255) NOT NULL,
                idade VARCHAR NOT NULL,
                rua VARCHAR(255) NOT NULL,
                bairro VARCHAR(255) NOT NULL,
                cidade VARCHAR(255) NOT NULL,
                estado VARCHAR(255) NOT NULL,
                numero VARCHAR NOT NULL
            )
            """)
        self.conn.commit()
    def desconnect_bd(self):
        self.cursor.close()
    # CREATE
    def insert_dados(self,nome,email,idade,rua,bairro,cidade,estado,numero):
        self.connect_bd()
        self.cursor.execute("""
            INSERT INTO Cadastro (nome, email, idade, rua, bairro, cidade, estado, numero)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """, (nome, email, idade, rua, bairro, cidade, estado, numero))
        
        self.conn.commit()
        self.desconnect_bd()


a= DataBase()
a.connect_bd()