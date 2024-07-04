import ttkbootstrap as tb

from GraficalInterface.ui_builder import ModernApp
from DataStorage import ds_mqtt
from DataStorage import ds_sensor
from DataStorage import ds_sensorData
from Sensor import sensor
from Sensor import run_sensors
from Mqtt.mqtt_broker import MyMqtt

if __name__ == "__main__":
    
    myMqtt = MyMqtt()
    sensorDatabase = ds_sensor.SensorsDatabase();
    brokerDatabase = ds_mqtt.BrokerDatabase();
    myRunSensors = run_sensors.SensorRun()
    mySensorDataStream = ds_sensorData.SensorDataStream();
    
    root = tb.Window(themename="cyborg")
    root.geometry("1920x1080")
    app = ModernApp(root)
       
    # Callback da interface grafica do Main
    instance_function_main_run = myRunSensors.run
    app.frames["MainUI"].set_callback_start(instance_function_main_run)
    
    instance_function_main_stop =  myRunSensors.stop
    app.frames["MainUI"].set_callback_stop(instance_function_main_stop)

    # Callback da interface grafica do Broker
    instance_function_broker_save_data = brokerDatabase.save_data
    app.frames["MqttUI"].set_callback_save_button(instance_function_broker_save_data)
    
    instance_function_connnect_mqtt = myMqtt.connectToBroker
    app.frames["MqttUI"].set_callback_connect_button(instance_function_connnect_mqtt)
    
    instance_function_disconnnect_mqtt = myMqtt.disconnectToBroker
    app.frames["MqttUI"].set_callback_disconnect_button(instance_function_disconnnect_mqtt)
    
    # Callback da interface grafica do Sensor
    instance_function_sensor_save_data = sensorDatabase.save_data
    app.frames["SensorUI"].set_callback_save_button(instance_function_sensor_save_data)

    instance_function_sensor_delete_data = sensorDatabase.delete_data        
    app.frames["SensorUI"].set_callback_delete_button(instance_function_sensor_delete_data)
    
    # Callback interface grafica de visualizacao
    instance_function_get_datastream = mySensorDataStream.fetch_data
    app.frames["ShowGraphUI"].set_callback_fetch_data(instance_function_get_datastream)

    # Funcoes de Inicialização do sistema
    
    #Recupera o ultimo registro no banco de dados e inseri na interface grafica de Broker MQTT
    init_broker_name, init_broker_ip, init_broker_port = brokerDatabase.fetch_data();
    app.frames["MqttUI"].insert_form_data(str(init_broker_name), str(init_broker_ip), str(init_broker_port))
    
    # Callback da Classe RunSensors
    instance_function_subscriber_boker = myMqtt.subscribe
    myRunSensors.set_mqtt_subscribe_callback(instance_function_subscriber_boker)

    instance_function_unsubscriber_boker = myMqtt.unsubscribe
    myRunSensors.set_mqtt_unsubscribe_callback(instance_function_unsubscriber_boker)
    
    instance_function_storage_data_stream = mySensorDataStream.save_data
    myRunSensors.set_data_storage_callback(instance_function_storage_data_stream)

    # Load All Sensors in database
    all_sensor_in_database = sensorDatabase.fetch_data()

    for sensorUnit in all_sensor_in_database:
        #Inseri todos os sensores na lista da UI de Sensores e ShowGraph
        app.frames["SensorUI"].insert_sensor_list(sensorUnit[0])
        app.frames["ShowGraphUI"].insert_sensor(sensorUnit[0])
        print(f"sensor_tag: {sensorUnit[0]}, sensor_implement: {sensorUnit[1]}, sensor_data: {sensorUnit[2]}, sensor_unit: {sensorUnit[3]}")
        
        #Adiciona todos os sensors no run_sensors
        localSensor = sensor.Sensor(sensorUnit[0], sensorUnit[1], sensorUnit[2], sensorUnit[3])
        myRunSensors.add_sensor(localSensor)
        
    root.mainloop()