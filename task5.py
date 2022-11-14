# python 3.11.0

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

# Основная функция, на вход две json-строки, возвращает True,
# если противоречия нет, и False, если найдено противоречие.
def task(first_string, second_string):
    # Преобразуем первую ранжировку в таблицу
    first = json_to_dict(first_string)
    A = [ [0 for i in range(len(first))] for i in range(len(first)) ]
    for i in first:
        for j in first:
            if first[i] <= first[j]:
                A[i][j] = 1
            else:
                A[i][j] = 0

    # Преобразуем вторую ранжировку в таблицу
    second = json_to_dict(second_string)
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

    # Проверяем, есть ли противоречие
    for i in range(len(first)):
        for j in range(i, len(first)):
            if S[i][j] == 0:
                return False
    return True

a = ["1", ["2","3"],"4", ["5", "6", "7"], "8", "9", "10"]
b = [["1","2"], ["3","4","5"], "6", "7", "9", ["8","10"]]
print(task(a,b))
