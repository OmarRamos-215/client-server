from http import client
from iiot_device import Sensor
import json
import time

# Creación de un objeto de la clase HTTPConnection
_conn= client.HTTPConnection(host='localhost', port=5000)

# Creación de un objeto de la clase Sensor
s= Sensor()

# Para formar un JSON para enviar al servidor
headers= {'Content-type' : 'application/json'}

while True:
    data= {
        'id' : 1,
        'name' : 'Inclination sensor',
        'value' : s.get_random_inclination()
    }

    json_data= json.dumps(data)

    _conn.request('POST', '/inclination', json_data, headers=headers)
    _conn.close()
    

    #print(s.get_random_number())
    #print(s.get_temp())
    #print(s.get_temp_for_windows())
    time.sleep(5)