# -*- coding: utf-8 -*-
import re
import datetime
import os
from colorclass import Color, Windows
import sys


def find(path, reg_exp):
    """
    Функция первоначальной обработки файла, по заданному регулярному выражению.
    The function of the initial file processing, according to the given regular expression
    :param path:
    :param reg_exp:
    :return:
    """
    start = datetime.datetime.now()
    tmp_result = []
    with open(path, 'r') as f:
        [tmp_result.append(line) for line in f if re.search(reg_exp, line) is not None]
        '''
        for line in f:
            if re.search(reg_exp, line) is not None:
                tmp_result.append(line)
        '''
    end = datetime.datetime.now()
    delta = str(end - start)
    print(delta)
    print(Color("{{{0}}}{1}: {2}{{/{0}}}".format("autoyellow", "number of matches found", len(tmp_result))))
    return tmp_result


def rotary_search(result, regexp):
    """
    Функция дальнейшего поиска в обработанном файле.
    The function of further search in the processed file
    :param result:
    :param regexp:
    :return:
    """
    start = datetime.datetime.now()
    tmp_result = []
    # добавить в массив tmp_result строку из массива result, если есть совпадение с регуляркой
    [tmp_result.append(i) for i in result if re.search(reg_exp, i) is not None]
    '''
    for i in result:
        if re.search(regexp, i) is not None:
            tmp_result.append(i)
    '''
    end = datetime.datetime.now()
    delta = str(end - start)
    print(delta)
    print("{0}: {1}".format("number of matches found", len(tmp_result)))
    return tmp_result


def show_result(result, reg_exp):
    """
    Функция вывода результатов обработки.
    Function of output of processing results
    :param result:
    :param reg_exp:
    :return:
    """
    if len(result) == 0:
        print("{0}".format("No regular expression matches found"))
    else:
        for i in result:
            dict_match = {}
            line_new = ""
            a = re.finditer(reg_exp, i)
            for ii in a:
                dict_match[ii.group()] = [ii.start(), ii.end()]

            j = 0
            start_z = 0
            for key, val in dict_match.items():
                # формирование строки с подсветкой совпадений по регулярному выражению
                # forming a string with highlighting regular expression matches
                line_new += i[start_z:val[0]] + Color("{{{0}}}{1}{{/{0}}}".format("autogreen", key))
                start_z = val[1]
                j += 1
                if j == len(dict_match):
                    line_new += i[start_z:]
                else:
                    continue
            print(line_new)


def save(result, path_save):
    """
    Функция сохранения результатов в файл.
    The function of saving results to a file.
    :param result:
    :param path_save:
    :return:
    """
    try:
        with open(path_save, "w") as f:
            [f.write(i) for i in result]
        save_result = "success"
    except IOError as a:
        save_result = a
    return save_result


if __name__ == "__main__":

    platform = sys.platform
    if "win" in platform:
        Windows.enable(auto_colors=True, reset_atexit=True)  # Enable colors in the windows terminal
    else:
        pass
    loop = True
    while loop is True:
        path = str(input((r"Enter path to log file: ")))
        if os.path.exists(path) is True:
            reg_exp = str(input(("Enter regexp: ")))
            result = find(path, reg_exp)
            loop1 = True
            while loop1 is True:
                print("{0}".format("1. Show result"))
                print("{0}".format("2. Сontinue search in found"))
                print("{0}".format("3. Save result"))
                print("{0}".format("4. Exit"))
                response1 = int(input((r"Enter your choose: ")))
                if response1 == 1:
                    show_result(result, reg_exp)
                elif response1 == 2:
                    reg_exp = str(input(("Enter regexp: ")))
                    result = rotary_search(result, reg_exp)
                elif response1 == 3:
                    path_save = str(input((r"Enter the path to save the result: ")))
                    save_result = save(result, path_save)
                    if save_result == "success":
                        print(Color("{{{0}}}{1}{{/{0}}}".format("autogreen", save_result)))
                    else:
                        print(Color("{{{0}}}{1}{{/{0}}}".format("autored", save_result)))

                elif response1 == 4:
                    loop1 = False

        else:
            print("{0}".format("File not exist"))
        print("{0}".format("1. Enter path to log file"))
        print("{0}".format("2. Exit"))
        response = int(input((r"Enter your choose: ")))
        if response == 1:
            pass
        elif response == 2:
            loop = False
        else:
            print("{0}".format("Error"))
            loop = False
