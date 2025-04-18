# Hỗ trợ unicode
import sys
from operator import itemgetter
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
def input_bai7():
    m = int(input("Nhập số hàng của mảng: "))
    n = int(input("Nhập số cột của mảng: "))
    print("Nhập các phần tử của mảng:")
    A = []
    for i in range(m):
        row = list(map(float, input(f"Nhập hàng {i + 1}: ").split()))
        if len(row) != n:
            raise ValueError("Số lượng phần tử trong hàng không khớp với số cột đã nhập.")
        A.append(row)
    return A

def bai7(A):
    m = len(A)
    n = len(A[0])

    # a. Tìm giá trị lớn nhất và nhỏ nhất trên mỗi cột
    max_in_columns = [max(row[j] for row in A) for j in range(n)]
    min_in_columns = [min(row[j] for row in A) for j in range(n)]

    # b. Tìm phần tử lớn nhất và nhỏ nhất của mảng A cùng các chỉ số hàng và cột
    max_value = float('-inf')
    min_value = float('inf')
    max_indices = (-1, -1)
    min_indices = (-1, -1)

    for i in range(m):
        for j in range(n):
            if A[i][j] > max_value:
                max_value = A[i][j]
                max_indices = (i, j)
            if A[i][j] < min_value:
                min_value = A[i][j]
                min_indices = (i, j)

    # c. Đếm số phần tử bằng phần tử lớn nhất
    count_max = sum(row.count(max_value) for row in A)

    return {
        "max_in_columns": max_in_columns,
        "min_in_columns": min_in_columns,
        "max_value": max_value,
        "max_indices": max_indices,
        "min_value": min_value,
        "min_indices": min_indices,
        "count_max": count_max
    }
def input_bai8():
    print("Nhập các tuple (name, age, score), mỗi tuple cách nhau bởi dấu cách:")
    data = input("Ví dụ: Tom,19,80 John,20,90: ")
    tuples = [tuple(item.split(',')) for item in data.split()]
    return [(name, int(age), int(score)) for name, age, score in tuples]

def bai8(tuples):
    sorted_tuples = sorted(tuples, key=itemgetter(0, 1, 2))
    return sorted_tuples
def bai9_convert_to_string(number):
    return str(number)

def bai9_sum_strings(num1, num2):
    total = int(num1) + int(num2)
    return total
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
    # Bài 7
    print('Bài 7')
    A = input_bai7()
    result = bai7(A)
    print("Giá trị lớn nhất trên mỗi cột:", result["max_in_columns"])
    print("Giá trị nhỏ nhất trên mỗi cột:", result["min_in_columns"])
    print(f"Phần tử lớn nhất là {result['max_value']} tại vị trí {result['max_indices']}")
    print(f"Phần tử nhỏ nhất là {result['min_value']} tại vị trí {result['min_indices']}")
    print(f"Số phần tử bằng phần tử lớn nhất là {result['count_max']}")
    # Bài 8
    print('Bài 8')
    tuples = input_bai8()
    sorted_tuples = bai8(tuples)
    print("Danh sách sau khi sắp xếp:")
    for item in sorted_tuples:
        print(item)
    # Bài 9
    print('Bài 9')
    num1 = input("Nhập số thứ nhất: ")
    num2 = input("Nhập số thứ hai: ")
    str_num1 = bai9_convert_to_string(num1)
    str_num2 = bai9_convert_to_string(num2)
    total = bai9_sum_strings(str_num1, str_num2)
    print(f"Tổng của {num1} và {num2} là: {total}")
if __name__ == "__main__":
   main()