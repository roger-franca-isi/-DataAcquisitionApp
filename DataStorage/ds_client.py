import psycopg2
from psycopg2 import sql

# Configurações de conexão ao banco de dados
conn_params = {
    'dbname': 'Database_DataAcquisitionApp',    # Nome do banco de dados
    'user': 'my_app_user',                      # Nome do usuário
    'password': '12345678',                      # Senha do usuário
    'host': '127.0.0.1',                         # Endereço do servidor do banco de dados
    'port': '5432'                              # Porta do servidor do banco de dados
}

# Função para salvar os dados no banco de dados
def save_broker_data(broker_name, broker_ip, broker_port):
    try:
        conn = psycopg2.connect(**conn_params)
        cursor = conn.cursor()
        
        insert_query = sql.SQL("""
            INSERT INTO "TABLE_MQTT" (broker_name, broker_ip, broker_porta)
            VALUES (%s, %s, %s)
        """)
        
        cursor.execute(insert_query, (broker_name, broker_ip, broker_port))
        
        conn.commit()
        cursor.close()
        conn.close()
        return True
    
    except Exception as e:
        print(f"Erro ao conectar ao banco de dados: {e}")
        return False
    
# Função para conectar ao banco de dados e executar a consulta
def query_broker_data():
    try:
        # Conectar ao banco de dados
        conn = psycopg2.connect(**conn_params)
        cursor = conn.cursor()

        # Consulta SQL
        query = """SELECT broker_name, broker_ip, broker_porta FROM "TABLE_MQTT";"""

        # Executar a consulta
        cursor.execute(query)

        # Buscar os resultados
        results = cursor.fetchall()

        # Exibir os resultados
        for row in results:
            print(f"Broker Name: {row[0]}, Broker IP: {row[1]}, Broker Porta: {row[2]}")

        # Fechar o cursor e a conexão
        cursor.close()
        conn.close()
        
        return row[1], row[2]
    
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        
        
        
    