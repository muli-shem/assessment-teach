#Question 5: Reverse Integer

def reverse_integer(num):
    sign = -1 if num <0 else 1
    num = abs(num)
    reversed_num = 0
    while num >0:
        reversed_num = (reversed_num*10)+(num % 10)
        num //= 10
    return sign * reversed_num
print(reverse_integer(12345))
print(reverse_integer(55003434))
print(reverse_integer(4544203))