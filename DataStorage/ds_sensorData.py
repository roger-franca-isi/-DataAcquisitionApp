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
        
    def save_data(self, sensor_tag, sensor_value):
        try:
            conn = psycopg2.connect(**self.conn_params)
            cursor = conn.cursor()
            
            # Construindo a consulta SQL com o nome da tabela diretamente na string
            insert_query = f"""
                INSERT INTO "{sensor_tag}" (sensor_value)
                VALUES (%s)
            """
            
            # Executando a consulta com o valor do sensor
            cursor.execute(insert_query, (sensor_value,))
            
            conn.commit()
            cursor.close()
            conn.close()
            return True
        
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return False

        finally:
            # Certifique-se de fechar a conexão e o cursor
            if cursor is not None:
                cursor.close()
            if conn is not None:
                conn.close() 
        
    def fetch_data(self, sensor_tag, num_values):
        try:
            conn = psycopg2.connect(**self.conn_params)
            cursor = conn.cursor()
    
            # Construindo a consulta SQL para buscar os últimos 'num_values' registros da tabela especificada
            select_query = f"""
                SELECT sensor_value, timestamp
                FROM {sensor_tag}
                ORDER BY id DESC
                LIMIT %s
            """
            
            # Executando a consulta com o número de valores a buscar
            cursor.execute(select_query, (num_values,))
            
            # Obtendo os resultados da consulta
            results = cursor.fetchall()
    
            cursor.close()
            conn.close()
    
            return results
    
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return None
            
        
    def delete_data(self, sensor_tag):
        try:
            conn = psycopg2.connect(**self.conn_params)
            cursor = conn.cursor()
            
            # Construindo a consulta SQL para deletar todos os registros da tabela especificada
            delete_query = f"""
                DELETE FROM {sensor_tag}
            """
            
            # Executando a consulta de deletar
            cursor.execute(delete_query)    
                    
            conn.commit()
            cursor.close()
            conn.close()
            return True
        
        except Exception as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
            return False
        