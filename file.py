num = int(input(" enter your number: "))

temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp //=10

if num == reverse:
    print("this is a palindrome number")
else:
    print("this is not a palindrome number")