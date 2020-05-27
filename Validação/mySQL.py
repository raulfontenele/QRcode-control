import mysql.connector
from mysql.connector import errorcode 

class mySQL:
    def __init__(self,hosp,usua,senh,banc,tab):
        self.hospedagem = hosp
        self.usuario = usua
        self.senha = senh
        self.bancoDados = banc
        self.tabela = tab
        self.conexao = None
    
    def conectarBanco(self):
        try:
            self.conexao = mysql.connector.connect(host='localhost', user='root', password='', database=self.bancoDados)
            print("Database connection made!")
            
        except mysql.connector.Error as error:
            if error.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database doesn't exist")
            elif error.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("User name or password is wrong")
            else:
                print(error)

    def Inserir(self, data, hora, cnpj, num_nota, valor_compra):
        cursor = self.conexao.cursor()
        
        select_stmt = 'INSERT INTO ' + self.tabela + '(Data, Hora, Cnpj, Num_nota, Valor_compra ) VALUES (%s, %s, %s, %s, %s)'

        values = (data, hora, cnpj, num_nota, valor_compra)
        resposta = cursor.execute(select_stmt, values)
        self.conexao.commit()
        cursor.close()

    def ConsultarCondicao(self,colunaConsultada,condicao):
        cursor = self.conexao.cursor()
        select_stmt = ("SELECT Num_nota FROM " + self.tabela + " WHERE " + colunaConsultada + "  = %(condition)s")
        cursor.execute(select_stmt,{"condition" : condicao})
        if(len( cursor.fetchall() ) == 0 ):
            cursor.close()
            return True
        else:
            cursor.close()
            return False

    def Consultar(self,string_colunas):
        cursor = self.conexao.cursor()
        select_stmt = "SELECT " + string_colunas + " FROM " + self.tabela
        cursor.execute(select_stmt)
        resultado = cursor.fetchall()
        cursor.close()
        return resultado