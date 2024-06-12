import ttkbootstrap as tb

from GraficalInterface.ui_builder import ModernApp
from DataStorage import ds_client
from Mqtt.mqtt_broker import MyMqtt

if __name__ == "__main__":
    
    myMqtt = MyMqtt()
    
    root = tb.Window(themename="cyborg")
    root.geometry("1920x1080")  # Define a janela para ser full HD
    app = ModernApp(root)
    
    #Realiza todas as conexoes de callbacks e interaçoes entre instancias das classes
    app.frames["MqttUI"].set_callback_save_button(ds_client.save_broker_data)
    
    instance_function_connnect_mqtt = myMqtt.connectToBroker
    app.frames["MqttUI"].set_callback_connect_button(instance_function_connnect_mqtt)
    
    instance_function_disconnnect_mqtt = myMqtt.disconnectToBroker
    app.frames["MqttUI"].set_callback_disconnect_button(instance_function_disconnnect_mqtt)
    
    root.mainloop()