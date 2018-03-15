import re
import os
import datetime
import time
import threading
import queue
import sys


path = r'c:\putty\Log\test\1234.xml'
start = datetime.datetime.now()
print(start)

list_device = []


def exam_reachable_dev(path):
    """
    обработка файла настроек из secureCRT на выходе получаем массив из списка устройст и из адресов вида
    router1; xx.xx.xx.xx
    """
    f = open(path, 'r', encoding='utf-8')
    devices = list(f.readlines())
    i = 0
    k = 1
    while i < len(devices):
        if re.search(r'[A-Z]{3}-[a-z]{1}.*-[0-9a-zA-Z-]*', devices[i]) is None:   # ищет строку вида XYZ-s2345-1ur-1
            i += 1
        else:
            hostname = re.search(r'[A-Z]{3}-[a-z]{1}.*-[0-9a-zA-Z-]*', devices[i]).group(0)   # извлекаем имя хоста и записываем переменную
            for ii in range(i, len(devices)):
                if re.search(r'Hostname', devices[ii]) != None:
                    if re.search(r'\d+.\d+.\d+.\d+', devices[ii]) is not None:  # ищет строчку с ip адресом
                        ip = re.search(r'\d+.\d+.\d+.\d+', devices[ii]).group(0)  # извлекает адрес
                        i = ii
                        k += 1
                        stroka = '{0}; {1}'.format(hostname, ip)
                        list_device.append(stroka)
                        break
                    else:
                        i = ii
                        break


exam_reachable_dev(path)

print('amount devices: ', len(list_device))


def exam_ip(work_queue):
    """проверяем доступность железок с помощью ping и пишем результат в файл"""
    while True:
        # Если заданий нет - закончим цикл
        if work_queue.empty():
            sys.exit()
        # Получаем задание из очереди
        i = work_queue.get()
        print('DEVICE: ', i)
        ip = i.split(';')[1]  # из строки вида router1; xx.xx.xx.xx получаем ip adress разделяя строку по ";"
        result = os.system('ping -n 3 -w 500 ' + ip)  # execute ping ip address

        if result == 0:
            status = 'OK'
        else:
            status = 'FAIL'
        stroka = i + '; ' + status + '\r'  # формируем строку вида (router1; xx.xx.xx.xx; OK)- hostname; ip addr; status
        with open(r'c:\putty\Log\test\dev_list_test111.txt', 'a') as out:
            out.write(stroka)
        # Сообщаем о выполненном задании
        work_queue.task_done()
        print(u'Очередь: %s завершилась' % i)


work_queue = queue.Queue()  # Создаем FIFO очередь

# Заполняем очередь заданиями
for device in list_device:
    work_queue.put(device)

print('queue length = ', len(work_queue.queue))

# Создаем и запускаем потоки, которые будут обслуживать очередь
for i in range(17):
    print(u'Поток', str(i), u'стартовал')
    print("kolichestvo activnyh potokov: ", threading.activeCount())
    t1 = threading.Thread(target=exam_ip, args=(work_queue,))
    t1.setDaemon(True)
    t1.start()
    time.sleep(0.0001)


work_queue.join()  # Ставим блокировку до тех пор пока не будут выполнены все задания
end = datetime.datetime.now()
print('time= ', end - start)
