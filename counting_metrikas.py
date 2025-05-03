# TO DO: try except

# функция для преобразования кортежа в список с числами, возвращает список чисел
def represent_tuple_as_int_list(rps_values):
    try:
        return [int (value) for value in rps_values]
    except (TypeError, ValueError) as e:
        print(f"Ошибка преобразования кортежа в список с числами {e}")
        return []

# функция для среза по пользовательскому вводу, возвращает список подтвергшийся операции среза
def slice_list(real_rps_values, slices):
    try:
        left, right = slices
        return real_rps_values[left:right]
    except (TypeError, ValueError) as e:
        print(f"Ошибка подсчета среза {e}")
        return real_rps_values

# функция для подсчета среднего значения на полученном спсике метрики со срезом и без среза
def count_avg_metrika(data_for_counting_sum):
    try: 
        avg_sliced_metrika = sum(data_for_counting_sum) / len(data_for_counting_sum) # считаем среднее значение списка метрик со срезом
        return avg_sliced_metrika
    except (TypeError, ZeroDivisionError) as e:
        print (f"Ошибка при подсчете суммы {e}")
        return 0

# считаем частоты полученных значений
def count_frequency(data_for_count_frequency):
    try:
        frequency = {}
        for value in data_for_count_frequency: # для каждого элемента списка real_rps_values
            if value in frequency: # проверка для каждого значения словаря
                frequency[value] += 1 # если есть в словаре - добавляем ключ и плюсуем единицу (считаем кол-во вхождений)
            else:
                frequency[value] = 1 # если отсутствует в словаре - добавляем ключ и ставим единицу как кол-во вхождений
        return frequency
    except TypeError as e:
        print(f"Ошибка при подсчете частот {e}")
        return frequency

# считаем медианное значение для списка метрик (для обычного и для среза)
def count_median(temp_list_for_count_median):
    try:
        quotient, remainder = divmod(len(temp_list_for_count_median), 2)
        median = temp_list_for_count_median[quotient] if remainder else sum(temp_list_for_count_median[quotient - 1:quotient + 1]) / 2
        return median
    except (TypeError, ZeroDivisionError) as e:
        print(f"Ошибка при подсчете медианы {e}")
        return 0

# принимаем решение, какая же была нагрузка
def check_load(metrika_for_determine_load, median):
    try:
        if metrika_for_determine_load >= median * 1.25:
            return "Ебучие скачки"
        elif metrika_for_determine_load <= median * 0.75:
            return "Охуительные снижения"
        else:
            return "Дохуя стабильная"
    except TypeError as e:
        print(f"Ошибка определения умной нагрузки {e}")
        return "Ошибка определения умной нагрузки"


# цикл для коммуникации с пользователем
def main():
    try:       
        # метрики от системы мониторинга (кортеж)
        rps_values = (5081, '17184', 10968, 9666, '9102', 12321, '10617', 11633, 5035, 9554, '10424', 9378, '8577', '11602', 14116, '8066', '11977', '8572', 9685, 11062, '10561', '17820', 16637, 5890, 17180, '17511', '13203', 13303, '7330', 7186, '10213', '8063', '12283', 15564, 17664, '8996', '12179', '13657', 15817, '16187', '6381', 8409, '5177', 17357, '10814', 6679, 12241, '6556', 12913, 16454, '17589', 5292, '13639', '7335', '11531', '14346', 7493, 15850, '12791', 11288)

        # преобразовываем наш список из кортежа функцией
        real_rps_values = represent_tuple_as_int_list(rps_values)
        print("Предустановленный список со значениями метрики:\n", real_rps_values) # вывод для проверки, что сформирован список с числами

        while True:
            print("")
            print("Введите число в формате 123 для добавления одного числа \nВведите числа в формате 123;123;123;123 для добавления нескольких чисел \nВведите срез в формате [12, 52] для операции среза по подготовленному списку \nНажмите Enter для подсчета и выхода")
            user_metrika = input() # пользовательский ввод в консоль
            # если пользователь вводит число
            try:                
                if user_metrika.isdigit(): # проверка на число
                    real_rps_values.append(int(user_metrika)) # приведение к int
                    print(f"Ввели число {user_metrika} - записали")
                    print(f"Теперь список выглядит так: {real_rps_values}")
                # если значения передаются пакетным способом через ";" - 123;123;123;123;123;123...
                elif ";" in user_metrika: 
                    try:
                        real_rps_values.extend(map(int, user_metrika.split(";"))) # разделяем ввод на числа через ; и добавляем к real_rps_values
                        print(f"Пакетный ввод такой {user_metrika} - записали")
                        print(f"Теперь список выглядит так: {real_rps_values}")
                    except ValueError as e:
                        print(f"Ошибка в пакетном вводе {e}, используйте формат чисел роазделенных ';'")   
                # если на вход в программу поступит следующая структура: # [число, число] Например, [17, 52], то необходимо произвести срез по указанным индексам (левая и правая граница, соответственно) 
                elif "," in user_metrika: # если пользователь просит сделать срез
                    try:
                        slices = list(map(int, user_metrika.strip("[]").split(","))) # убираем [] из строки, разделяем числа через ",", добавляем в список условий для среза, предварительно приведя к int
                        
                        #задаем в переменные значения в список полученные через вызов функции подготовки списка со срезом 
                        data_for_counting_sum = slice_list(real_rps_values, slices)
                    
                        #задаем частоты полученных значений
                        sliced_frequency_for_print = count_frequency(data_for_counting_sum)
                        print(f"Список значений метрик после среза выглядит вот так {data_for_counting_sum }")
                        print(f"Список частот после среза выглядит вот так {sliced_frequency_for_print}")     
                        
                        #задаем в список значения среза для средней метрики из функции
                        avg_sliced_metrika = count_avg_metrika(data_for_counting_sum)
                        print("Среднее значение метрики среза:", avg_sliced_metrika)
                        
                        # считаем медианное значение для списка метрик среза 
                        median = count_median(data_for_counting_sum)
                        print ("Медианное значение метрики среза: ", median)
                        
                        # определяем, какая же была нагрузка
                        result = check_load(avg_sliced_metrika, median)
                        print ("Умная система определения нагрузки определила характер нагрузки как:\n", result)
                        break    
                    except ValueError as e:
                        print(f"Ошибка при обработке среза {e}. Используйте формат [число, число]")
                elif user_metrika == "": # если пользовательского ввода не последовало - прерываем
                            
                    # считаем среднее значение без среза
                    avg_metrika = count_avg_metrika(real_rps_values)
                    print("Среднее значение метрики без среза:", avg_metrika)
                
                    # считаем медианное значение для обычного списка метрик (без среза)
                    median = count_median(real_rps_values)
                    print ("Медианное значение метрики без среза: ", median)

                    #Считаем частоты полученных значений (без среза)
                    frequency_for_print = count_frequency(real_rps_values)
                    # Вывод частот полученных частот
                    print ("Частоты полученных значений:", frequency_for_print)

                    # определяем, какая же была нагрузка
                    result = check_load(avg_metrika, median)
                    print ("Умная система определения нагрузки определила характер нагрузки как:\n", result)
                    break      
                else: # если пользовательский ввод не валиден - сообщаем об этом
                        print("Валидация не пройдена, используйте числа") 
                        print (f"Список состои из {real_rps_values}")
            except Exception as e:
                print(f"Ошибка при вычислениях {e}")
    except Exception as e:
        print(f"Программа поломалося полностью {e}")

if __name__ == "__main__":
    main()
