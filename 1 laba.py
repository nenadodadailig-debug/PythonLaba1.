def spisok():
    
    #получаем длину списка от пользователя
    while True:
        try:
            n = int(input("Введите длину списка: "))
            if n<=0:
                print("Введите целое положительное число: ")
                continue
            break
        except ValueError:
            print("Ошибка: введите целое число.")

    sp = []

    #получаем список длинной n от пользователя
    for i in range(n):
        a = input("Введите элемент списка: ")
        
        #пытаемся преобразовать в число
        try:
            a=int(a)
        #в случае ошибки оставляем строкой
        except ValueError:
            pass

        sp.append(a)

    #список элементов, которые встречаются один раз
    result = []

    #ищем элементы, которые встречаются один раз
    for x in sp:
        if sp.count(x) == 1:
            result.append(x)
    return result

resultat=spisok()
if resultat:
    print("Элементы, встречающиеся один раз:", *resultat)
else:
    print("Элемнтов, встречающихся один раз нет")
    
