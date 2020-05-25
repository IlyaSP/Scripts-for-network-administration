# my-scripts
1. add_device_to_rancid.py

2. ciscoASA-ssh-context-config.py

3. collection_configuration_from_cisco-juniper

4. measurement_delays_losses.py

5. ping_multiple_hosts_with_threading.py

6. log_analayzer.py

7. folder ansible

# 1. add_device_to_rancid.py
Скрипт служит для добавления устройств в rancid. В скрепте реализована проверка корректности ввода IP адреса.
В файл "/etc/hosts" добавляется запись вида "IP  hostname". В файл "router.db" добавляется запись вида "IP;vendor;status". Тестировалось на Centos 7

The script  develop for add devices to rancid. In the script implemented test correctness of entering IP adress.
A "IP hostname" entry is added to the file "/ etc / hosts". In the file "router.db" a record of the form "IP; vendor; status". Tested on Centos 7

# 2. ciscoASA-ssh-context-config.py
Скрипт служит для сбора конфигураций с устройств cisco ASA. скрипт может генерировать офибки по таймауту и неверный логин/пароль, поддерживает работу с мультиконтексным режимомм. Тестировалось на Ubuntu 16.04

The script is used to collect configurations from cisco ASA devices. the script can generate time out files and incorrect login / password, supports work with multi-context mode.Tested on Ubuntu 16.04

# 3. collection_configuration_from_cisco-juniper
Скрипт служит для сбора конфигураций с устройств cisco и Juniper. скрипт может генерировать офибки по таймауту и неверный логин/пароль. Тестировалось на Ubuntu 16.04

The script is used to collect configurations from cisco and Juniper devices. The script can generate timeouts and incorrect login / password. Tested on Ubuntu 16.04

# 4. measurement_delays_losses.py
Скрипт служит для сбора иформации о потерях максимальной и средней задержке и записи этих данных в файл. Для получения данных используется команда "ping" и данные её выполнения. Тестировалось на Linux parrot 5.1.0, windows 10

The script is used to collect information about the losses of the maximum and average delay and write this data to a file. To get the data, use the "ping" command and its execution data. Tested on Linux parrot 5.1.0, windows 10

# 5. ping_multiple_hosts_with_threading.py
Скрипт получает список IP адресов из выгрузки сессий программы SecureCRT, проверяет их е командой "ping" и в конце работы выводит список не доступных устройств. Тестировалось на windows 10

The script obtains a list of IP addresses from the unloading of SecureCRT sessions, checks their availability with the "ping" command, and at the end of the work displays a list of not available devices. Tested on Windows 10

# 6. log_analyzer.py
Скрипт предназначен для анализа лог файлов. Регулярное выражение для поиска вводится пользователем. Скрипт позволяет осуществлять многократный поиск в уже обработанных результатах (например: сначала поиск производится по одному регулярному выражению, далее в результатах это поиска, производится поиск по другому регулярному выражению и так далее). Так же скрипт поддерживает вывод в консоль результатов поиска с подсветкой того, что попадает под регулярное выражение, сохранение результатов поиска в файл. 
Требуется установка библиотеки "colorclass".
Тестировался на Windows 7

The script is designed to analyze log files. The regular expression to search is entered by the user. The script allows you to perform multiple searches in already processed results (for example: first the search is performed by one regular expression, then in the search results, the search is performed by another regular expression, and so on). The script also supports output to the console of search results with highlighting of what falls under the regular expression, saving search results to a file.
Requires installation of the "colorclass" library.
Tested on Windows 7

# 7. Folder ansible
Папка содержит скрипты для обработки данных в результате выполнения playbook в ansible.

The folder contains scripts for processing data from the execution of the playbook in ansible.
