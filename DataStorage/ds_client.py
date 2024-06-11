import psycopg2

# Configurações de conexão ao banco de dados
conn_params = {
    'dbname': 'Database_DataAcquisitionApp',    # Nome do banco de dados
    'user': 'my_app_user',                      # Nome do usuário
    'password': '12345678',                      # Senha do usuário
    'host': '127.0.0.1',                         # Endereço do servidor do banco de dados
    'port': '5432'                              # Porta do servidor do banco de dados
}

# Função para conectar ao banco de dados e executar a consulta
def query_table_mqtt():
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

    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        
        
    