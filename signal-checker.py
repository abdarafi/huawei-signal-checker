from huawei_lte_api.Client import Client
from huawei_lte_api.Connection import Connection

with Connection('http://YOUR_USERNAME:YOUR_PASSWORD@YOUR_HUAWEI_IP/') as connection:
    client = Client(connection)

    device_signal = client.device.signal()
    rsrp = int(device_signal['rsrp'].strip('dBm'))
    result = ""
    # TODO also consider to measure the result based on other metrics, not only RSRP.
    if rsrp >= -84:
        result = "Excellent"
    elif rsrp <= -85 or rsrp <= -102:
        result = "Good"
    elif rsrp <= -103 or rsrp <= -111:
        result = "Fair"
    else:
        result = "Poor"
    
    print('[+] Cell ID: {}'.format(device_signal['cell_id']))
    print('[+] RSRQ: {}'.format(device_signal['rsrq']))
    print('[+] RSRP: {}'.format(device_signal['rsrp']))
    print('[+] RSSI: {}'.format(device_signal['rssi']))
    print('\nOverall LTE signal strength is {}'.format(result))