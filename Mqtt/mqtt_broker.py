import paho.mqtt.client as mqtt

class MyMqtt:
    def __init__(self):
        # Criação do cliente MQTT
        self.client = mqtt.Client()

        # Atribuição das funções de callback
        self.client.on_connect = self.callback_on_connect
        self.client.on_message = self.callback_on_message
        self.client.on_publish = self.callback_on_publish

    def connectToBroker(self, broker_address, broker_port):
        self.broker_address = str(broker_address)
        self.broker_port = int(broker_port)
        rc = self.client.connect(self.broker_address, self.broker_port, 60)
        
        # Avaliação do código de retorno da conexão
        if rc == 0:
            # Início do loop para processar callbacks e reconectar automaticamente
            print("Iniciando o loop MQTT...")
            self.client.loop_start()
        else:
            print(f"Não foi possível conectar ao broker MQTT. Código de retorno: {rc}")
    
    def disconnectToBroker(self):
       self.client.disconnect()
            
    # Função callback quando o cliente se conecta ao broker
    def callback_on_connect(self, client, userdata, flags, rc):
        
        self.client.publish("test/topic", "Hello, MQTT!")

        if rc == 0:
            print("Conectado ao broker MQTT!")
            # Subscrever ao tópico quando conectado
            client.subscribe("test/topic")
        else:
            print(f"Falha na conexão. Código de retorno: {rc}")
    
    # Função callback quando uma mensagem é recebida do broker
    def callback_on_message(self, client, userdata, msg):
        print(f"Mensagem recebida no tópico {msg.topic}: {msg.payload.decode()}")
        
    # Função callback quando a mensagem é publicada
    def callback_on_publish(self, client, userdata, mid):
        print("Mensagem publicada com sucesso")

