# Hỗ trợ unicode cho Python 3.7 trở lên
import sys
sys.stdout.reconfigure(encoding='utf-8')

# Chương trình

def input_text():
    text = input("Nhập vào một chuỗi: ")
    return text
def bai1(text):
    upper = 0
    lower = 0
    space = 0
    for i in text:
        if i.isupper():
            upper += 1
        elif i.islower():
            lower += 1
        elif i.isspace():
            space += 1
    return upper, lower, space
def bai2(text):
    char = 0
    num = 0
    for i in text:
        if i.isalpha():
            char += 1
        elif i.isdigit():
            num += 1
    return char, num
def input_arr():
    arr = input('Nhập vào một chuỗi: ').split(',')
    return arr
def bai3(arr):
    arr.sort()
    return arr
def input_num():
    num = input("Nhập vào một chuỗi số:  ").split(',')
    return num
def bai4(num):
    num_tuple = tuple(num)
    return num_tuple
def input_bai5():
    text = input('Nhập vào một chuỗi: ')
    return text
def bai5(text):
    unique_words = sorted(set(text.split()))
    return ' '.join(unique_words)
def bai6():
    num = []
    for i in range(1000,3001):
        if i%2==0:
            num.append(i)
    return num
        
# Chương trình chính
def main():
    # Bài 1
    print("Bài 1")
    text = input_text()
    upper, lower, space = bai1(text)
    print(f"Có {upper} ký tự in hoa, {lower} ký tự thường, Có {space} khoảng cách trong chuỗi")
    # Bài 2
    print("Bài 2")
    text = input_text()
    char,num = bai2(text)
    print(f"Số chữ cái là {char}, Số chữ số là {num}")
    # Bải 3
    print('Bài 3')
    arr = input_arr()
    arr = bai3(arr)
    print("Chuỗi sau khi sắp xếp là: ", arr)
    # Bài 4
    print('Bài 4')
    num = input_num()
    num_tuple = bai4(num)
    print(num,"\n",num_tuple)
    # Bài 5
    print('Bài 5')
    text = input_bai5()
    unique_words = bai5(text)
    print("Các từ không trùng lặp là: ", unique_words)
    # Bài 6
    print('Bài 6')
    num = bai6()
    print(num)
if __name__ == "__main__":
   main()