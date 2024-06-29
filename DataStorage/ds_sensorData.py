import psycopg2
from psycopg2 import sql

from DataStorage.ds_interface import DatabaseInterface

class SensorDataStream(DatabaseInterface):
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
    
            cursor.close()
            conn.close()
                    
        except Exception as e:
            print(f"Ocorreu um erro: {e}")
            
    def delete_data(self, sensor_tag):
        try:
            conn = psycopg2.connect(**self.conn_params)
            cursor = conn.cursor()
                        
            conn.commit()
            cursor.close()
            conn.close()
            return True
        
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return False
        