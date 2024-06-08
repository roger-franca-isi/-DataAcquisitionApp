# -*- coding: utf-8 -*-
"""
Created on Sat Jun  8 17:06:38 2024

@author: roger
"""
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

class DatabaseClient:
    def __init__(self):

        # Configurações do InfluxDB
        token = "your_influxdb_token"  # Substitua pelo seu token
        org = "your_organization"  # Substitua pelo nome da sua organização
        bucket = "MqttBroker"

        # Criar uma instância do cliente
        client = InfluxDBClient(url="http://localhost:8086", token=token)
        write_api = client.write_api(write_options=SYNCHRONOUS)

        
    def connect:
        
        
    def disconnect:
        
        
    