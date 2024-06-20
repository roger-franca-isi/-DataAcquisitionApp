import psycopg2
from psycopg2 import sql

from DataStorage.ds_interface import DatabaseInterface

class BrokerDatabase(DatabaseInterface):
   def __init__(self):
       # Configurações de conexão ao banco de dados
       self.conn_params = {
           'dbname': 'Database_DataAcquisitionApp',    # Nome do banco de dados
           'user': 'my_app_user',                      # Nome do usuário
           'password': '12345678',                      # Senha do usuário
           'host': '127.0.0.1',                         # Endereço do servidor do banco de dados
           'port': '5432'                              # Porta do servidor do banco de dados
       }

   def save_data(self, broker_name, broker_ip, broker_port):
        try:
            conn = psycopg2.connect(**self.conn_params)
            cursor = conn.cursor()

            insert_query = sql.SQL("""
                INSERT INTO "TABLE_MQTT" (broker_name, broker_ip, broker_porta)
                VALUES (%s, %s, %s)
            """)

            cursor.execute(insert_query, (broker_name, broker_ip, broker_port))
            print(f"BrokerDatabase - Salvo no Banco de dados")

            conn.commit()
            cursor.close()
            conn.close()
            return True

        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return False

   def fetch_data(self):
       try:
            # Conectar ao banco de dados
            conn = psycopg2.connect(**self.conn_params)
            cursor = conn.cursor()

            # Consulta SQL
            query = """SELECT broker_name, broker_ip, broker_porta
                       FROM "TABLE_MQTT"
                       ORDER BY broker_porta DESC
                       LIMIT 1;"""

            # Executar a consulta
            cursor.execute(query)
            print(f"BrokerDatabase - Busca no Banco de dados")

            # Buscar o último registro
            result = cursor.fetchone()

            # Fechar o cursor e a conexão
            cursor.close()
            conn.close()
            
            if result:
                broker_name, broker_ip, broker_porta = result
                return broker_name, broker_ip, broker_porta
            else:
                return None, None, None
        
       except Exception as e:
           print(f"Ocorreu um erro: {e}")
           return None, None, None
        
   def delete_data(self, broker_name, broker_ip, broker_port):
        try:
            conn = psycopg2.connect(**self.conn_params)
            cursor = conn.cursor()
            
            insert_query = sql.SQL("""
                INSERT INTO "TABLE_MQTT" (broker_name, broker_ip, broker_porta)
                VALUES (%s, %s, %s)
            """)
            
            cursor.execute(insert_query, (broker_name, broker_ip, broker_port))
            print(f"BrokerDatabase - Remoção no Banco de dados")

            conn.commit()
            cursor.close()
            conn.close()
            return True
        
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return False