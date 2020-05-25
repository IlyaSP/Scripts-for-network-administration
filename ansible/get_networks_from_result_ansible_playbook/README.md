# 1. networks_from_ansible.py
Скрипт служит для разбора данных полученных в результате работы ansible. Результат работы скрипта будет cvs файл в котором будут содержаться следующие данные:
- Имя устройства
- Название интерфейса на котором назначен ip адрес;
- Дискрипшен интерфеса;
- IP адрес интерфеса;
- Подсеть, которой принадлежит IP адрес интерфейса;
Работа скрипта проверялась на Windows 7 и python3.7. Так же требуется установка библиотеки "netaddr" для python.

The script is used to parse the data obtained as a result of ansible. The result of the script will be a cvs file which will contain the following data:
- Hostname
- The name of the interface on which the ip address is assigned;
- Discrimination of an interface;
- IP address of the interface;
- The subnet to which the IP address of the interface belongs;
The script was tested on Windows 7 and python3.7. It also requires installing the "netaddr" library for python.

# 2. folder "data"
Данная папка содержит пример файлов с данными полученых в результате работы ansible.

This folder contains an example of files with data obtained as a result of ansible operation.

# 3. playbook_int_facts.yml
Playbook для ansible с помощью которой были получены файлы находящиеся в папке "data"
Playbook запускался на ansible 2.9

Playbook for ansible with the help of which the files located in the "data" folder were received
playbook was run on asible 2.9

# 4.result_file.cvs
Файл с результатами работы скрипта.

File with the results of the script.
