## Задание №3.

Напишите чек-лист для программы, получающей на вход строку с математическим выражением, результатом программы является ответ соответствующий 
правилам математика. В строке присутствуют следующие символы, описывающие математические операции сложение(+), вычитание(-), умножение(*), 
деление(/), степень(^), скобки, которые определяют порядок операций. Строка может содержать из сторонних символов пробелы, но они не должны 
влиять на выполняемые операции. Если в выражении встречаются пустые скобки (), то они игнорируются. Строка передается в кодировке UTF-32. 
Программа должна принимать строки любой длины, а также правильно проводить вычисления с бесконечно большими и числами бесконечно стремящихся 
к нулю. Программа не может принимать несколько знаков, кроме минусов, идущих под ряд. Несколько минусов интепретируются в соответствии 
с правилами математики. 
Чек лист должен содержать входные данные, ожидаемый результат и словесное описание на что направлен данный кейс. Допускается словесное 
описание входных данных ожидаемого результата, в случае, если вычислить проверяемое значение невозможно.


### Решение:
Во время выполнения задания возникли вопросы:
Есть ли интерфейс у этой программы? В задани не сказано, что у программы есть интерфейс, значит принимаем, что абстрактная программа не имеет интерфейса, то есть не имеет поле ввода и 
кнопки подтвержающие отправку на расчет. Готовое выражение сначала должно пройти проверку программы, а затем подается на расчет. Расчет будет происходить на сервере. 
Объем памяти и скорость обработки данных примим абсолютно безграничные. Поэтому проверки полей ввода, кнопок, скорости ответа, технологической границы не нужны.
Разделы математики, по правилам которой будет работать программа: арифметика, элементарная алгебра и элементарная геометрия. Это необходимо для избежания внутренних противоречий.

Так как в задании не сказано, что в выражениях можно использовать знак "." или ",", то я буду считать, что программа может принимать дробные числа 
только с использованием знака "/", но выводить числа может со знаком точки

### Число:
| Входные данные |  Ожидаемый результат |  Описание | 
| -------------- | -------------------- | --------- |
|1|1|число|
|0.1|неподдерживаемые символ, ошибка|так как точку невозможно ввести, программа выдаст ошибку|
|0,1|неподдерживаемые символ, ошибка|так как запятую невозможно ввести, программа выдаст ошибку|
|100,000,000|неподдерживаемые символ, ошибка| программа выдаст ошибку|
|100 000|100000|разделение числа пробелом. На выводе пробел не влияет на выполнение программы|
|1()0|10|пустые скобки игнорируются|
|1(2)3|6|интерпритируются как выражение 1*2*3|
|1)23|ошибка|использование одной скобки не допустимо|
|0|0|расчет не производится, на вывод посылается тоже число|
|10^5|100000|валидное значение|
|10^-2|0.01|отрицательная степень, получение дробного числа|
|10^(5)|100000|валидное значение|
|10^3/2|500|сначала выполняется 10^3, затем /2|
|10^(3/2)|31.62278|сначала выполняется 3/2, затем 10^|

### Сложение:
| Входные данные |  Ожидаемый результат |  Описание | 
| -------------- | -------------------- | --------- |
|1+1|2|сложение 2х чисел|
|1+1+1|3|сложение 3х чисел|
|1+0|1|сложение с 0|
|0+0|0|сложение 0 и 0|
|-1+4|3|сложение с отрицательным числом|
|1+|1 или режим ожидания завершения выражения|незаконченное выражение|
|+0|0|расчет не производится, на вывод посылается 0, но без знака|
|-1+|-1 или режим ожидания завершения выражения|расчет не производится, на вывод посылается -1|
|1++++++++++|1 или режим ожидания завершения выражения|большое кличество знаков +|

### Вычитание:
| Входные данные |  Ожидаемый результат |  Описание | 
| -------------- | -------------------- | --------- |
|2-1|1|вычитание|
|1-1|0|вычитание из числа само число, получение 0|
|1-2|-1|получение отрицательного числа|
|1000-1-1-1-1-1(-1)n|-|вычитание большого количества чисел|
|5+3-4-2+6|8|комбинирование сложения и вычитания в одном выражении|
|-5-6|-11|вычитание с отрицательным числом|

### Умножение:
| Входные данные |  Ожидаемый результат |  Описание | 
| -------------- | -------------------- | --------- |
|2*2|4|умножение 2х чисел|
|1*2|2|умножение на 1|
|1*0|0|умножение на 0|
|-1*2|-2|умножение на отрицательное число|
|-1*-1|1|умножение 2х отрицательных чисел без использования скобок|
|(2+3)5|25|распределительный закон|
|(2*2)*3|12|сочетальный закон|
|6-3+4*2|11|соблюдение очередности. сначала умножение, затем вычитание, а после сложение|
|1234567890*987654321|1219326311126352640|поддержка больших чисел|
|e^-2345678*1234567890|какое-то число|поддержка выражений с абсолютно малыми и большими числами|

### Деление:
| Входные данные |  Ожидаемый результат |  Описание | 
| -------------- | -------------------- | --------- |
|6/3|2|простое деление|
|24/3/2|4|последовательное деление|
|5/2|2.5|получение дробного числа|
|4/0|ошибка деления|делить на ноль нельзя :)|
|3/3|1|деление числа само на себя|
|0/7|0|делимое =0|
|7/1|7|деление на единицу|
|6*3+4/2|20|соблюдение очередности. сначала умножение, затем деление, а после сложение|
|6/𝝿|1,90986|поддержка выражений с константами|
|6/-3|-2|деление на отрицательное число|
|-6/-3|2|деление 2х отрицательных чисел|

### Степень:
| Входные данные |  Ожидаемый результат |  Описание | 
| -------------- | -------------------- | --------- |
|2^2+3^2|13|сложение с числами в степени|
|2^2/3^2|0.44444|соблюдение очередности. сначала возведение в степень, затем деление|
|2^2(/)3^2|ошибка в выражении|знак деления внутри скобок|
|2^e|6,58089|возведение в степень е|
|2^𝝿|8.82498|возведение в степень константы|
|e^-2345678|какое-то абсолютно малое число||

### Буквы:

Так как в задании написано, что программа принимает на ввод строку с математическим выражением, а согласно википедии: "математическое выражение — конечная комбинация символов, 
которая правильно построена согласно правилам, зависящим от контекста. Математические символы могут обозначать числа (константы), переменные, операции, функции, пунктуацию, 
группирование и другие аспекты логического синтаксиса", то программа должна принимать на ввод буквы тоже.

| Входные данные |  Ожидаемый результат |  Описание | 
| -------------- | -------------------- | --------- |
|cos(90)|0|поддержка буквенных выражений. по умолчанию тригонометрические функции берутся от угла|
|sin(cos(5))|0.01739|вложеные функции|
|×4)x+/y|ошибка ввода выражения|выражения, содержащие буквы, не являющиеся математическими константами или функциями, посчитаны не будут, так как для их решения необходимо равенство числу или другому выражению, а знак равенства программа не поддерживает|
|привет5+1|ошибка|кириллица. выражение не является ни константой, ни функцией|
|hello(cos(0))|ошибка|выражение не является ни константой, ни функцией|
|log10(10)|1|поддержка математических функций. логарифм|
|sqrt(2)|4|поддержка математических функций. квадратный корень|
|cos233|ошибка|математические функции можно использовать только в том случае, если возле них есть скобки, а в них число|

### Пробелы:
| Входные данные |  Ожидаемый результат |  Описание | 
| -------------- | -------------------- | --------- |
|6 *3+4/2|20|пробел в выражении возле числа. пробел игнорируется|
|6*3+4 4/2|40|пробел в выражении внутри числа. пробел игнорируется|
|lo g 10(10)|1|пробел внутри математической функции. пробел игнорируется|
|(2+3) 5|25|пробел внутри выражения с умножением без использования знака|

### Знаки:
| Входные данные |  Ожидаемый результат |  Описание | 
| -------------- | -------------------- | --------- |
|*|ошибка|знак без выражения|
|3++2|5|в задании сказано, что программа принимает несоклько знаков подряд. наверное, при вычислении программа учитывает только 1 знак|
|***|ошибка|знак без выражения|
|5--3|2|повторяющиеся знаки минус. четное количество минусов дает плюс, нечетное - минус|
