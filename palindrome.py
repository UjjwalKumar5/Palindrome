# how to print the reverse the given Word or number

a = 0
def reverse_number(num):
    reverse_num = 0
    while num > 0 :
        remin = num % 10
        reverse_num = (reverse_num * 10) + remin
        num = num//10
    print(reverse_num)
    
reverse_number(112233)

abc = "Hello World"
print(abc[::-1])

bcd = "The given number is like si rebmun nevig eht" 
print(bcd[::-1])
reverse_num = 0
def revers_number(num):
    global reverse_num
    if num > 0 :
        remin = num % 10
        reverse_num = (reverse_num * 10) + remin
        revers_number(num//10)
    return reverse_num
    
print(revers_number(1234567))

rev = 0
def palindrome(num):
    global rev
    num = 0
    while num > 0:
        remainder = num % 10
        rev = rev*10 + remainder
        num = num // 10
        return rev
    if rev == num :
        print("The given number is palindrome")
    else:
        print("The given number is not a palindrome")
        
palindrome(151)

# For finding a given string is palindrome or not
def string(abc):
    if abc == abc[::-1]:
        print("The given string is palindrome")
    else:
        ("The given string is not a palindrome write another word")
        
string("abcddcba")


       