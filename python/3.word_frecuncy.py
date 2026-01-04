import re
from collections import Counter

def count_word_frequency(sentence):
    cleaned_sentence = re.sub(r'[^\w\s]', '', sentence).lower() #sub是去掉标点，lower转小写，这里的顺序是先去标点再转小写，这是用了re模块的正则表达式功能
    words = cleaned_sentence.split() #split是按空格分的，words是一个列表
    return Counter(words) #Counter是collections模块里的一个类，可以直接对列表进行计数，返回一个字典，键是元素，值是出现的次数

def analyze_sentence_frequency(): #这个函数的功能单纯是输入，排序和打印结果
    user_sentence = input("请输入一个句子：")
    word_frequency = count_word_frequency(user_sentence)
    sorted_frequency = sorted(word_frequency.items(), key=lambda item: item[1], reverse=True) #这是把字典变成一个元素是元组（key, value）的列表，然后按item[1]也就是value排序，reverse=True是降序。lambda是匿名函数，当然我们也可以定义一个函数来专门取数字，不过用lambda更简洁一些

    print("词频统计结果：")
    for word, frequency in sorted_frequency: #解包元组
        print(f"{word}: {frequency}")

    """
    for item in sorted_frequency:
        print(f"{item[0]}: {item[1]}")
        或者
        word = item[0]
        frequency = item[1]
        print(f"{word}: {frequency}")
    这两种写法也是可以的，不过上面的解包更简洁一些
    """

if __name__ == "__main__":
    test = "Hello, world! Hello, everyone. This is a test sentence. This is only a test."
    print(count_word_frequency(test))
    analyze_sentence_frequency()