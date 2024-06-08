from influxdb_client import InfluxDBClient, Point
from influxdb_client.client.write_api import SYNCHRONOUS

    def save_to_influxdb(self, broker_name, broker_ip, broker_port):
        # Configurações do InfluxDB
        token = "your_influxdb_token"
        org = "your_organization"
        bucket = "your_bucket"

        client = InfluxDBClient(url="http://localhost:8086", token=token)
        write_api = client.write_api(write_options=SYNCHRONOUS)

        # Criar ponto de dados
        point = Point("mqtt_broker_info").tag("broker", broker_name).field("ip", broker_ip).field("port", int(broker_port))

        # Escrever no banco de dados
        write_api.write(bucket=bucket, org=org, record=point)
        client.close()

