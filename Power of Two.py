#Question 3: Power of Two
def is_power_of_two(num):
    return num>0 and(num & (num-1))==0
print(is_power_of_two(8))
print(is_power_of_two(6))
