# python 3.11.0

import json

# Фукнция для преобразования строки в более удобный вид
def json_to_dict(string):
    i = 0
    res = {}
    for element in string:
        if type(element) is str:
            res[int(element) - 1] = i
        else:
            for same in element:
                res[int(same) - 1] = i
        i += 1
    return res        

# Основная функция, на вход две json-строки, возвращает json-строку с парами противоречий
def task(first_string, second_string):
    # Преобразуем первую ранжировку в таблицу
    first = json_to_dict(json.loads(first_string))
    A = [ [0 for i in range(len(first))] for i in range(len(first)) ]
    for i in first:
        for j in first:
            if first[i] <= first[j]:
                A[i][j] = 1
            else:
                A[i][j] = 0

    # Преобразуем вторую ранжировку в таблицу
    second = json_to_dict(json.loads(second_string))
    B = [ [0 for i in range(len(second))] for i in range(len(second)) ]
    for i in second:
        for j in second:
            if second[i] <= second[j]:
                B[i][j] = 1
            else:
                B[i][j] = 0
        
    # Перемножаем таблицы
    S = [ [0 for i in range(len(first))] for i in range(len(first)) ]
    for i in range(10):
        for j in range(10):
            S[j][i] = A[j][i] * B[j][i]

    out = []
    # Проверяем, есть ли противоречие, и возрващаем False, если есть
    for i in range(len(first)):
        for j in range(i, len(first)):
            if S[i][j] == 0:
                out.append([json.dumps(i + 1),json.dumps(j + 1)])
    # Возвращаем результат
    return out
