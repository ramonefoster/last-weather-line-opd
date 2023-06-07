import os, time
import datetime

def save_last_line(source_file, destination_file):
    source_modified_time = os.path.getmtime(source_file)
    destination_exists = os.path.exists(destination_file)
    
    if not destination_exists or source_modified_time > os.path.getmtime(destination_file):
        with open(source_file, 'r') as file:
            lines = file.readlines()
            #last_line = lines[-1].strip()
            last_line = lines[-1]

        with open(destination_file, 'w') as file:
            file.write(last_line)
        
        current_time = datetime.datetime.now()
        formatted_time = current_time.strftime("%H:%M")

        print(f"{formatted_time} Última linha salva em: '{destination_file}'.")
    else:
        print("Nenhuma modificação no arquivo da estação.")

while True:
    source_file = r'C:\WeatherLink\OPDNew\download.txt'
    destination_file = r'C:\Users\teste\Desktop\coopd\public\files\weather_tcspd.txt'
    save_last_line(source_file, destination_file)
    time.sleep(10)