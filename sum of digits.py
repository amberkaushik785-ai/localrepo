def sum_digits(num):
    sum=0
    while(num>0):
        sum = sum + num%10
        num=num//10
    return sum
print(sum_digits(123))
