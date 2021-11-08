import urllib.request
from PIL import Image
import logging
from time import sleep

print('Скрипт запущен :)\nСмотрите файл Q_logs.log в рабочей директории')

logging.basicConfig(filename='Q_logs.log',  filemode='a', level=logging.INFO,
                    format='%(asctime)s - %(levelname)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
def analising():
    img = urllib.request.urlopen(
        "http://www2.irf.se/maggraphs/preliminary_k_index_last_24.png", timeout=30).read()
    out = open("K&Q index.png", "wb")
    out.write(img)
    out.close()

    image = Image.open("K&Q index.png")
    pix = image.load()

    x = 1185
    y_1 = 145
    y_2 = 131
    y_3 = 118
    y_4 = 105
    y_5 = 91
    y_6 = 78
    y_7 = 65
    y_8 = 51
    y_9 = 38

    sample_color = str((255, 255, 255))

    if str((pix[x, y_9])) != sample_color:
        return 9
    elif str((pix[x, y_8])) != sample_color:
        return 8
    elif str((pix[x, y_7])) != sample_color:
        return 7
    elif str((pix[x, y_6])) != sample_color:
        return 6
    elif str((pix[x, y_5])) != sample_color:
        return 5
    elif str((pix[x, y_4])) != sample_color:
        return 4
    elif str((pix[x, y_3])) != sample_color:
        return 3
    elif str((pix[x, y_2])) != sample_color:
        return 2
    elif str((pix[x, y_1])) != sample_color:
        return 1
    else:
        return 0

while True:
    try:
        data = analising()
        logging.info(data)
        sleep(600)
    
    except Exception as e:
        print(e)
        logging.info('Connection error')
        sleep(5)
