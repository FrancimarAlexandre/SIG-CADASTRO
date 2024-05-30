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
                idade INTEGER NOT NULL,
                rua VARCHAR(255) NOT NULL,
                bairro VARCHAR(255) NOT NULL,
                cidade VARCHAR(255) NOT NULL,
                estaddo VARCHAR(255) NOT NULL,
                numero  INTEGER NOT NULL
            )
            """)
        self.conn.commit()
    def desconnect_bd(self):
        self.cursor.close()
    # CREATE
    def insert_dados(self):
        pass



a= DataBase()
a.connect_bd()