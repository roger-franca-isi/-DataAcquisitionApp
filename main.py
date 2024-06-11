from GraficalInterface.ui_builder import create_app
from DataStorage.ds_client import query_table_mqtt

if __name__ == "__main__":
    query_table_mqtt()
    #root = create_app()
    #root.mainloop()