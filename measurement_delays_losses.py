# -*- coding: utf-8 -*-
import sys
import subprocess
import ctypes
import datetime
import threading
import time
import re
import locale
import os
from pathlib import Path
from queue import Queue
from colorclass import Color, Windows

platform = sys.platform
name_folder_mesurement = "measuring_loss_delay"
max_strings_file = 3700  # maximum number of lines in the data file


if "linux" in platform:
    path_to_home = str(Path.home())
    # print(path_to_home)
    if not os.path.exists("{0}/{1}".format(path_to_home, name_folder_mesurement)):
        # print("Directory '{0}/{1}' not exists".format(path_to_home,name_folder_mesurement))
        try:
            os.makedirs("{0}/{1}".format(path_to_home, name_folder_mesurement))
            # print("Directory '{0}/{1}' was created".format(path_to_home, name_folder_mesurement))
            full_path_to_home = "{0}/{1}/".format(path_to_home, name_folder_mesurement)
            # print(full_path_to_home)
        except Exception as e:
            print(e)
    else:
        full_path_to_home = "{0}/{1}/".format(path_to_home, name_folder_mesurement)
        # print(full_path_to_home)
elif "win" in platform:
    path_to_home = r"C:\\"
    print(path_to_home)
    if not os.path.exists("{0}/{1}".format(path_to_home, name_folder_mesurement)):
        # print("Directory '{0}/{1}' not exists".format(path_to_home, name_folder_mesurement))
        try:
            os.makedirs("{0}/{1}".format(path_to_home, name_folder_mesurement))
            # print("Directory '{0}/{1}' was created".format(path_to_home, name_folder_mesurement))
            full_path_to_home = "{0}/{1}/".format(path_to_home, name_folder_mesurement)
            # print(full_path_to_home)
        except Exception as e:
            print(e)
    else:
        full_path_to_home = "{0}/{1}/".format(path_to_home, name_folder_mesurement)
        print(full_path_to_home)


def check_file_exist(path_to_file):
    result_check = os.path.exists(path_to_file)
    return result_check


def ping_ip(ip_address, platform):
    """
    Функция выполняющая каманду ping и возвращающая результат выполнения
    Function that executes the 'ping' command and returns the result of execution
    """

    if "win" in platform:
        # Определяем кодировку терминала windows
        # Define the encoding of the terminal windows
        coding = "cp{0}".format(ctypes.windll.kernel32.GetOEMCP())
        reply = subprocess.run(['ping', '-n', '20', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               encoding=coding)

        if reply.returncode == 0:
            return reply.stdout
        else:
            status = "FAILD"
            loss = "100"
            return status, loss

    elif "linux" in platform:
        reply = subprocess.run(['ping', '-c', '20', '-n', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               encoding=sys.stdout.encoding)
        if reply.returncode == 0:
            return reply.stdout
        else:
            status = "FAILD"
            return status


def get_data_from_ping(result, platform):
    """
    Функция выполняющая разбор результатов команды 'ping' для получения значений потерь, средней и максимальной
    задержки
    Function that parses the results of the 'ping' command to obtain loss, average and maximum values delays
    """
    if result != "FAILD":
        if "win" in platform:
            lost = re.search(r'\d+%', result).group(0)
            # status = "OK"
            lang = locale.windows_locale[ctypes.windll.kernel32.GetUserDefaultUILanguage()]
            # Определяем язык ОС Windows
            # Define the language OS Windows
            if "ru" in lang:
                a = re.search(r'Среднее = \d+ мсек', result).group(0)
                aver_delay = re.search(r'\d+', a).group(0)
                a = re.search(r'Максимальное = \d+ мсек', result).group(0)
                max_delay = re.search(r'\d+', a).group(0)

            elif "en" in lang:
                a = re.search(r'Average = \d+ms', result).group(0)
                aver_delay = re.search(r'\d+', a).group(0)
                a = re.search(r'Maximum = \d+ms', result).group(0)
                max_delay = re.search(r'\d+', a).group(0)
                print(max_delay)
        elif "linux" in platform:
            # status = "OK"
            lost = re.search(r'\d+%', result).group(0)
            delays = re.search(r"\d+\.\d+/\d+\.\d+/\d+\.\d+/\d+\.\d+", result).group(0).split("/")
            aver_delay = str(delays[1])
            max_delay = str(delays[2])
    else:
        # status = result
        lost = "100%"
        aver_delay = "0"
        max_delay = "0"
    return lost, aver_delay, max_delay


def ping(work_queue):
    while not work_queue.empty():
        # Получаем задание из очереди
        i = work_queue.get()
        # print('DEVICE: ', i)"
        ip_address = i
        now = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        result = ping_ip(ip_address, platform)
        lost, aver_delay, max_delay = get_data_from_ping(result, platform)
        print("{0} {1} {2} {3} {4}".format(now, ip_address, lost, aver_delay, max_delay))
        check_file_exist1 = check_file_exist(full_path_to_home + ip_address + r".txt")
        if check_file_exist1:
            with open(full_path_to_home + ip_address + r".txt", 'r+') as f:
                lines = f.readlines()
                if len(lines) >= max_strings_file:
                    f.seek(0)  # go back to the beginning of the file
                    f.write("{0};{1};{2};{3};{4}\n".format(now, ip_address, lost, aver_delay, max_delay))  # write new content at the beginning
                    for i in range(len(lines) - 1):  # write old content after new
                        f.write(lines[i])
                else:
                    with open(full_path_to_home + ip_address + r".txt", 'a') as f:
                        f.write("{0};{1};{2};{3};{4}\n".format(now, ip_address, lost, aver_delay, max_delay))
        else:
            with open(full_path_to_home + ip_address + r".txt", 'w') as f:
                f.write("{0};{1};{2};{3};{4}\n".format(now, ip_address, lost, aver_delay, max_delay))

        work_queue.task_done()
        # print(u'Очередь: %s завершилась' % i)
        # print("Len queue {0}".format(len(work_queue.queue)))


if __name__ == "__main__":
    work_queue = Queue()
    while True:
        start = datetime.datetime.now()
        """
        Заполняем очередь устройствами из списка. 
        Fill the queue with devices from the list
        """
        list_ip = ["8.8.8.8", "8.8.4.4"]

        for i in list_ip:
            # print(i)
            work_queue.put(str(i))

        for i in range(57):
            # print(u'Flow', str(i), u'start')
            # print(u'Поток', str(i), u'стартовал')
            # print("Number of active flows: ", threading.activeCount())
            # print(u"Количчество активных потоков: ", threading.activeCount())
            t1 = threading.Thread(target=ping, args=(work_queue,))
            t1.setDaemon(True)
            t1.start()
            time.sleep(0.1)

        work_queue.join()  # Ставим блокировку до тех пор пока не будут выполнены все задания
        if "win" in platform:
            Windows.enable(auto_colors=True, reset_atexit=True)    # Enable colors in the windows terminal
        else:
            pass
        os.system("cls||clear")
        print(start.strftime("%Y-%m-%d %H:%M:%S"))
        end = datetime.datetime.now()
        delta = "{autored}" + str(end - start) + "{/autored}"
        print(Color(delta))
        time.sleep(2)  # interval between starts
