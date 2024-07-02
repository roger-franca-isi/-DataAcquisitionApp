import psycopg2
from psycopg2 import sql

from DataStorage.ds_interface import DatabaseInterface

class SensorsDatabase(DatabaseInterface):
    def __init__(self):
        # Configurações de conexão ao banco de dados
        self.conn_params = {
            'dbname': 'Database_DataAcquisitionApp',    # Nome do banco de dados
            'user': 'my_app_user',                      # Nome do usuário
            'password': '12345678',                      # Senha do usuário
            'host': '127.0.0.1',                         # Endereço do servidor do banco de dados
            'port': '5432'                              # Porta do servidor do banco de dados
        }
        
    def save_data(self, sensor_tag, sensor_implement, sensor_data, sensor_unit):
        try:
            conn = psycopg2.connect(**self.conn_params)
            cursor = conn.cursor()
            
            insert_query = sql.SQL("""
                INSERT INTO "table_sensor" (sensor_tag, sensor_implement, sensor_data, sensor_unit)
                VALUES (%s, %s, %s, %s)
            """)
            
            cursor.execute(insert_query, (sensor_tag, sensor_implement, sensor_data, sensor_unit))
            print(f"SensorDatabase - Salvo no Banco de dados")

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
            query = """SELECT sensor_tag, sensor_implement, sensor_data, sensor_unit  
                FROM "table_sensor";"""
    
            # Executar a consulta
            cursor.execute(query)
    
            # Buscar os resultados
            results = cursor.fetchall()
    
            # Exibir os resultados
            #for row in results:
            #    print(f"Broker Name: {row[0]}, Broker IP: {row[1]}, Broker Porta: {row[2]}")
    
            # Fechar o cursor e a conexão
            cursor.close()
            conn.close()
            
            return results
        
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            
    def delete_data(self, sensor_tag):
        try:
            conn = psycopg2.connect(**self.conn_params)
            cursor = conn.cursor()
            
            delete_query = sql.SQL("""
                DELETE FROM "table_sensor"
                WHERE sensor_tag = %s
            """)
            
            cursor.execute(delete_query, (sensor_tag,))
            
            conn.commit()
            cursor.close()
            conn.close()
            return True
        
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return False
        