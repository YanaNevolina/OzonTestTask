# Тестовые задания для компании OZON


## [Задание 1](/task1)

Реализуйте программу:
Дан файл input.txt, содержащий в себе строки, в которых в случайном порядке заданы поля, несущие определенную информацию. 
Каждая строка содержит в себе одинаковое количество униклаьных полей. Все строки заключены в квадратные скобки. 
Название поля и его значение отделяется двоеточием. Поля разделены пробелами и могут содержать:
1) Строковые данные, которые заключены в кавычки и могут содержать пробелы
2) Числовые данные, являющиеся последовательностью цифр.
Выходные данные:
Для строк, в которых значение поля function является "MakePayment" собрать статистику сообещний message из следующего списка: 
1) "Validation error" 
2) "AntiFraud" 
3) "Unkown user" 
Статистика должна включать в себя количество подобных сообщений, а также наиболее частое значение поля user_type для каждого типа сообщений. 
Если для какого-то сообщения максимальное количество значений полей user_type встречатеся одинаковое количество раз, то необходимо вывести любое.
Данную информацию необходимо вывести в порядке убывания по количеству сообщений, сообщения с одинаковой частотой, в пределах данной частоты, 
выводятся в произвольном порядке. Также для строк, соответствующих вышеописанному условию, необходимо вывести значения полей user_id и message, 
разделяемых табуляцией, в произвольном порядке. Вывод осуществляется в файл output.txt.


## [Задание 2](/task2)

В базе данных есть две таблицы: "user" и user_status_history.
Напишите запрос к базе данных, который для причин "Validation error", "Balance error", "AntiFraud" выводит имя пользователя, его идентефикатор, дату изменения статуса и причину, для последних пользователей,  перешедших из статуса "ok" в статус "error" по каждой из перечислинных причин, своей последней по времени записью.


## [Задание 3](/task3)

Напишите чек-лист для программы, получающей на вход строку с математическим выражением, результатом программы является ответ соответствующий 
правилам математика. В строке присутствуют следующие символы, описывающие математические операции сложение(+), вычитание(-), умножение(*), 
деление(/), степень(^), скобки, которые определяют порядок операций. Строка может содержать из сторонних символов пробелы, но они не должны 
влиять на выполняемые операции. Если в выражении встречаются пустые скобки (), то они игнорируются. Строка передается в кодировке UTF-32. 
Программа должна принимать строки любой длины, а также правильно проводить вычисления с бесконечно большими и числами бесконечно стремящихся 
к нулю. Программа не может принимать несколько знаков, кроме минусов, идущих под ряд. Несколько минусов интепретируются в соответствии 
с правилами математики.
