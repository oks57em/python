# Петя и Катя- брат и сестра.Он задумывает два натуральных
# числа X и Y(X ,Y <=1000),а Катя должна их отгадать.
# Для этого Петя делает две подсказки.Он называет сумму 
# этих чисел S и их произведение P.

x = abs(int(input("Ввести первое число X")))
y = abs(int(input("Ввести второе число Y")))
if x < 1 or x > 1000 or y < 1 or y > 1000:
    print("Число не из заданного диапазона.")
else:
    s = x + y
    p = x * y
    stop = 0
    for i in range(1001):
        if stop != 1:
            for j in range(1001):
                if stop != 1:
                    if i * j == p and i + j == s:
                        print(i,j)
                        stop = 1
            else:
                j = 1001
        else:
            i = 1001
