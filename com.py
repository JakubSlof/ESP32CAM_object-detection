import serial
import time
port = 'COM5'
baund_rate = 115200
esp = serial.Serial(port,baund_rate,timeout=1)
def send_data(nunmber):
    command = f"{nunmber}\n"
    esp.write(command.encode('utf-8'))
    print('data send')



def receve_data():
    line =0
    while True:
        line= esp.readline().decode('utf-8').strip()
        print(line)
        if line == '69':
            break
        time.sleep(1)
    print('loop braked ')

send_data(2)
receve_data()
send_data(2)
receve_data()
send_data(2)
receve_data()
send_data(2)
receve_data()