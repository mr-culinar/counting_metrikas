from collections import Counter

# функция для преобразования кортежа в список с числами, возвращает список чисел
def represent_tuple_as_int_list(rps_values):
        return [int (value) for value in rps_values]
    
# функция для среза по пользовательскому вводу, возвращает список подтвергшийся операции среза
def slice_list(real_rps_values, slices):
        left, right = slices
        if left == right:
            print("Левая и правая граница среза не могут быть одинаковыми")
            return None
        if left > right:
            print("Левая граница не может быть больше правой")
            return None
        if right-left == 1:
             print("Срезать по единственному числу нельзя, иначе нахера второе подаешь! пиши [число, число]")
             return None
        if left < 0 or right < 0:
            print("Границы среза не могут быть отрицательным")
            return None

        return real_rps_values[left:right]
                      
    
# функция для подсчета среднего значения на полученном спсике метрики со срезом и без среза
def count_avg_metrika(data_for_counting_sum):
        avg_sliced_metrika = sum(data_for_counting_sum) / len(data_for_counting_sum) # считаем среднее значение списка метрик со срезом
        return avg_sliced_metrika
    
# считаем частоты полученных значений, заполняем словарь через Counter
def count_frequency(data_for_count_frequency):
        return dict(Counter(data_for_count_frequency))

# считаем медианное значение для списка метрик (для обычного и для среза)
def count_median(temp_list_for_count_median):
        sorted_list_for_count_median = sorted(temp_list_for_count_median)
        quotient, remainder = divmod(len(sorted_list_for_count_median), 2)
        median = sorted_list_for_count_median[quotient] if remainder else sum(sorted_list_for_count_median[quotient - 1:quotient + 1]) / 2
        return median


# принимаем решение, какая же была нагрузка
def check_load(metrika_for_determine_load, median):
        if metrika_for_determine_load >= median * 1.25:
            return "Ебучие скачки"
        elif metrika_for_determine_load <= median * 0.75:
            return "Охуительные снижения"
        else:
            return "Дохуя стабильная"
    

# цикл для коммуникации с пользователем
def main():
    try:       
        # метрики от системы мониторинга (кортеж)
        rps_values = (5081, '17184', 10968, 9666, '9102', 12321, '10617', 11633, 5035, 9554, '10424', 9378, '8577', '11602', 14116, '8066', '11977', '8572', 9685, 11062, '10561', '17820', 16637, 5890, 17180, '17511', '13203', 13303, '7330', 7186, '10213', '8063', '12283', 15564, 17664, '8996', '12179', '13657', 15817, '16187', '6381', 8409, '5177', 17357, '10814', 6679, 12241, '6556', 12913, 16454, '17589', 5292, '13639', '7335', '11531', '14346', 7493, 15850, '12791', 11288)

        # преобразовываем наш список из кортежа функцией
        real_rps_values = represent_tuple_as_int_list(rps_values)
        print("Предустановленный список со значениями метрики:\n", real_rps_values) # вывод для проверки, что сформирован список с числами

        while True:
            print("Введите число в формате 123 для добавления одного числа \nВведите числа в формате 123;123;123;123 для добавления нескольких чисел \nВведите срез в формате [число, число] для операции среза по подготовленному списку \nНажмите Enter для подсчета и выхода")
            user_metrika = input() # пользовательский ввод в консоль
            # если пользователь вводит число
            try:                
                if user_metrika.isdigit(): # проверка на число
                    real_rps_values.append(int(user_metrika)) # приведение к int
                    print(f"Ввели число {user_metrika} - записали \nТеперь список выглядит так: {real_rps_values}")
                # если значения передаются пакетным способом через ";" - 123;123;123;123;123;123...
                elif ";" in user_metrika: 
                    try:
                        numbers = list(map(int, user_metrika.split(";"))) # формируем список чисел переданных в требуемом формате
                        if any(num < 0 for num in numbers): # проверяем что число не может быть отрицательным
                             print("Числа передаваемые пакетным способом не могут быть отрицательными")
                        else:
                            real_rps_values.extend(numbers) # разделяем ввод на числа через ; и добавляем к real_rps_values
                            print(f"Пакетный ввод такой {user_metrika} - записали \nТеперь список выглядит так: {real_rps_values}")
                    except ValueError as e:
                        print(f"Ошибка в пакетном вводе {e}, используйте формат чисел разделенных ';'")   
                # если на вход в программу поступит следующая структура: # [число, число] Например, [17, 52], то необходимо произвести срез по указанным индексам (левая и правая граница, соответственно) 
                elif (user_metrika.startswith('[') and user_metrika.endswith(']')): # если пользователь просит сделать срез
                
                    try:
                        
                        slices = list(map(int, user_metrika.strip("[]").split(","))) # убираем [] из строки, разделяем числа через ",", добавляем в список условий для среза, предварительно приведя к int
                        
                        #задаем в переменные значения в список полученные через вызов функции подготовки списка со срезом 
                        data_for_counting_sum = slice_list(real_rps_values, slices)
                                            
                        #задаем частоты полученных значений
                        sliced_frequency_for_print = count_frequency(data_for_counting_sum)
                        print(f"Список значений метрик после среза выглядит вот так {data_for_counting_sum }\n Список частот после среза выглядит вот так {sliced_frequency_for_print}")
                        
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
                        print("Пользак, ты балбес - валидация не пройдена, используй числа или срез в формате [число, число]\nСписок состоит из {real_rps_values}") 
            except Exception as e:
                print(f"Пользак балбес - ошибка при вычислениях {e}, делить на ноль нельзя")
    except Exception as e:
        print(f"Программа поломалося полностью {e}")

if __name__ == "__main__":
    main()