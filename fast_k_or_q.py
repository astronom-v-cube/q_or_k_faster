import requests
import logging
import time
from time import sleep
logging.basicConfig(filename='logs_q_k.log',  filemode='a', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
print('Скрипт запущен')
while True:
    try:
        r = requests.get('https://www2.irf.se/maggraphs/preliminary_real_time_k_index', timeout=60)
        data = r.text
        logging.info(data)
        sleep(60)

    except:
        logging.info('Connection error')
        time.sleep(1)
