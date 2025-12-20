# This function checks if a given string is a palindrome
# palindrome的意思是回文，比如racecar。
# 当然为了复用性我们可以不在函数里print
# 我们写函数的时候要考虑很多东西比如输入的合法性，函数的接口设计，返回值的设计等等


def checkstring(word):
    word = word.lower().replace(" ", "")
    if len(word) == 0:
        print("The string is empty.")
    else:
        for i in range(0, len(word) // 2):
            if word[i] != word[len(word) - i - 1]:
                print("The string is not a palindrome.")
                return
        print("The string is a palindrome.")

# 在python里我们也可以很方便地反转字符串，然后直接比较
def checkstring_v2(word):
    cleaned_word = word.lower().replace(" ", "")
    if len(cleaned_word) == 0:
        print("The string is empty.")
    elif cleaned_word == cleaned_word[::-1]: # 反转字符串的简便方法，这里用的是C语言的切片方法所以比for循环更快
        print("The string is a palindrome.")
    else:
        print("The string is not a palindrome.")


def checkstring_v3(word):
    cleaned_word = word.lower().replace(" ", "")
    if len(cleaned_word) == 0:
        return False
    elif cleaned_word == cleaned_word[::-1]:
        return True
    return False

def checkstring_v4(word):
    cleaned_word = word.lower().replace(" ", "")
    if len(cleaned_word) == 0:
        raise ValueError("The string is empty.")
    return cleaned_word == cleaned_word[::-1] # 直接返回布尔值


# Test the function
# while True:
#     string = input("Enter a string (or type 'exit' to quit): ")
#     if string.lower() == 'exit':
#         print("Goodbye!")
#         break
#     checkstring(string)

while True:
    string = input("Enter a string (or type 'exit' to quit): ")
    if string.lower() == 'exit':
        print("Goodbye!")
        break
    try:
        if checkstring_v4(string):
            print("The string is a palindrome.")
        else:
            print("The string is not a palindrome.")
    except ValueError as ve:
        print(ve)