numberlargest = int(input("enter the largest number: "))
smallestnumber = int(input("enter the smallest number: "))
while smallestnumber:
    numberstore = smallestnumber
    smallestnumber = numberlargest % smallestnumber
    numberlargest = numberstore

print("the HCF is ", numberlargest)