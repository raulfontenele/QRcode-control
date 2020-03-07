import sqlite3  

class Database:
    def __init__(self,nome):
        self.nome = nome

        if self.checkTable('historico') == False:
            print(    self.checkTable('historico')    )
            self.criarTabela()
    
    def criarTabela(self):
        conn = sqlite3.connect(self.nome + '.db')

        # definindo um cursor
        cursor = conn.cursor()

        # criando a tabela (schema)
        cursor.execute("""
        CREATE TABLE historico (
                id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                cpnj VARCHAR(30) NOT NULL,
                horario DATETIME NOT NULL
        );
        """)

    def checkTable(self,tableName):
        conn = sqlite3.connect(self.nome + '.db')

        # definindo um cursor
        cursor = conn.cursor()

        # criando a tabela (schema)
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        
        for table in cursor.fetchall():
            if table[0] == tableName:
                conn.close()
                return True
        
        conn.close()
        return False
    
    def insert(self, date):
        conn = sqlite3.connect(self.nome + '.db')

        # definindo um cursor
        cursor = conn.cursor()
        # inserindo dados na tabela
        cursor.execute("""
        INSERT INTO historico (cpnj,horario)
        VALUES ('00000000000', '2014-06-08')
        """)

        # gravando no bd
        conn.commit()

        conn.close()
    
    def show(self):
        conn = sqlite3.connect(self.nome + '.db')
        cursor = conn.cursor()

        # lendo os dados
        cursor.execute("""
        SELECT * FROM historico;
        """)

        for linha in cursor.fetchall():
            print(linha)

        conn.close()
        

database = Database('teste')
database.insert('banana')
database.show()