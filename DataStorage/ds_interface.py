from abc import ABC, abstractmethod

# Configurações de conexão ao banco de dados
conn_params = {
    'dbname': 'Database_DataAcquisitionApp',    # Nome do banco de dados
    'user': 'my_app_user',                      # Nome do usuário
    'password': '12345678',                      # Senha do usuário
    'host': '127.0.0.1',                         # Endereço do servidor do banco de dados
    'port': '5432'                              # Porta do servidor do banco de dados
}

class DatabaseInterface(ABC):
    
    @abstractmethod
    def save_data(self, *args):
        pass

    @abstractmethod
    def fetch_data(self, *args):
        pass

    @abstractmethod
    def delete_data(self, *args):
        pass
