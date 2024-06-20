import ttkbootstrap as tb

from GraficalInterface.ui_builder import ModernApp
from DataStorage import ds_mqtt
from DataStorage import ds_sensor
from Sensor import sensor
from Mqtt.mqtt_broker import MyMqtt

if __name__ == "__main__":
    
    myMqtt = MyMqtt()
    sensorDatabase = ds_sensor.SensorsDatabase();
    brokerDatabase = ds_mqtt.BrokerDatabase();

    root = tb.Window(themename="cyborg")
    root.geometry("1920x1080")
    app = ModernApp(root)
    
    #Realiza todas as conexoes de callbacks e interaçoes entre instancias das classes
    
    #Callback da interface grafica do Sensor
    app.frames["MainUI"].set_callback_start()
    app.frames["MainUI"].set_callback_stop()

    #Callback da interface grafica do Broker
    instance_function_broker_save_data = brokerDatabase.save_data
    app.frames["MqttUI"].set_callback_save_button(instance_function_broker_save_data)
    
    instance_function_connnect_mqtt = myMqtt.connectToBroker
    app.frames["MqttUI"].set_callback_connect_button(instance_function_connnect_mqtt)
    
    instance_function_disconnnect_mqtt = myMqtt.disconnectToBroker
    app.frames["MqttUI"].set_callback_disconnect_button(instance_function_disconnnect_mqtt)
    
    
    #Callback da interface grafica do Sensor
    instance_function_sensor_save_data = sensorDatabase.save_data
    app.frames["SensorUI"].set_callback_save_button(instance_function_sensor_save_data)

    instance_function_sensor_delete_data = sensorDatabase.delete_data        
    app.frames["SensorUI"].set_callback_delete_button(instance_function_sensor_delete_data)
    
    #Funcoes de Inicialização do sistema;
    init_broker_name, init_broker_ip, init_broker_port = brokerDatabase.fetch_data();
    app.frames["MqttUI"].insert_form_data(str(init_broker_name), str(init_broker_ip), str(init_broker_port))
    
    root.mainloop()