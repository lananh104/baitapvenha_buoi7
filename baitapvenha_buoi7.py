"""
Bài 01: Viết hàm
        def max_min(*numbers)
    trả lại cả giá trị max, min của nhiều số được truyền vào
Bài 02: Viết hàm
        def reverse_string(str)
    trả lại chuỗi đảo ngược của chuỗi str
Bài 03: Viết hàm
        def is_perfect(n)
    để kiểm tra xem số tự nhiên n có phải là số hoàn hảo hay ko, trả lại True nếu có, False nếu không.
    Ghi chú: Xem định nghĩa về số hoàn hảo: http://hanoimoi.com.vn/Tin-tuc/Thieu-nhi/592454/so-hoan-hao-la-gi
Bài 04: Viết hàm
        def is_prime(n)
    để kiểm tra xem số tự nhiên n có phải số nguyên tố hay không, nếu có thì trả lại True, nếu không thì trả lại False
Bài 05: Viết hàm
        def count_upper_lower(str)
    trả lại số lượng chữ cái viết hoa, số lượng chữ cái viết thường trong chuỗi str
Bài 06: Viết hàm
        def is_pangram(str, alphabet)
    đề kiểm tra xem chuỗi str có phải là Pangram không, trả lại True nếu có, False nếu không
    Ghi chú: Pangram là chuỗi chứa mỗi chữ cái trong bảng alphabet ít nhất 1 lần
Bài 07: Viết hàm
        def create_matrix(n, m)
    xử lý việc tạo ra ma trận n hàng, m cột với giá trị phần tử tại (i, j) = i*j
Bài 08: Viết hàm
        def body_mass_index(m, h)
    để tính toán chỉ số BMI của một người với cân nặng m (kg), chiều cao h (m)
      Viết hàm
        def bmi_information(m, h)
    để đưa ra thông tin về chỉ số BMI cũng như phân loại mức độ gầy - béo của người cân nặng m, chiều cao h
Bài 09: Viết hàm
        def change_upper_lower(str)
    chuyển toàn bộ các ký tự in hoa sang in thường và in thường thành in hoa trong str
Bài 10: Viết hàm đệ quy đếm và trả về số lượng chữ số lẻ của số nguyên dương n cho trước.
        Ví dụ: Hàm trả về 4 nếu n là 19922610 (do n có 4 số lẻ là 1, 9, 9, 1)
Bài 11: Cho dãy số Tribonacci với công thức truy hồi sau:
            F(n) = F(n-1) + F(n-2) + F(n-3),    F(1) = 1, F(2) = 1, F(3) = 2
    Xây dựng 2 hàm để tìm ra số thứ n trong dãy số theo:
        + Hàm Đệ quy
        + Hàm Không đệ quy
Bài 12: Viết hàm
        def find_x(a_list, x)
    trả lại tất cả các vị trí mà x xuất hiện trong a_list, nếu không có thì trả lại -1
"""
# Bài 01: Viết hàm
#         def max_min(*numbers)
#     trả lại cả giá trị max, min của nhiều số được truyền vào
def max_min(*number):
    print("Số lớn nhất trong các số được truyền vào là: ",max(number))
    print("Số nhỏ nhất trong các số được truyền vào là: ", min(number))
    return max(number),min(number)
print(max_min(1,2))




# Bài 02: Viết hàm
#         def reverse_string(str)
#     trả lại chuỗi đảo ngược của chuỗi str
def reversal(str):
    return str[::-1]
print(reversal("abcdefg"))





# Bài 03: Viết hàm
#         def is_perfect(n)
#     để kiểm tra xem số tự nhiên n có phải là số hoàn hảo hay ko, trả lại True nếu có, False nếu không.
#     Ghi chú: Xem định nghĩa về số hoàn hảo: http://hanoimoi.com.vn/Tin-tuc/Thieu-nhi/592454/so-hoan-hao-la-gi
def is_perfect(n):
    t=0
    for i in range(1,n,1):
        if n%i==0:
            t+=i
    if t==n:
       return True
    return False
print(is_perfect(2))





# Bài 04: Viết hàm
#         def is_prime(n)
#     để kiểm tra xem số tự nhiên n có phải số nguyên tố hay không, nếu có thì trả lại True, nếu không thì trả lại False
def is_prime(n):
    count=[]
    if n<2:
        print("False")
    else:
        for i in range(1, n + 1, 1):
            if n%i==0:
                count.append(i)
    if len(count)>2:
        print("Đây không phải là số nguyên tố!")
        return False
    else:
        print("Đây là số nguyên tố!")
        return True
n=int(input("Mời nhập số n: "))
print(is_prime(n))





# Bài 05: Viết hàm
#         def count_upper_lower(str)
#     trả lại số lượng chữ cái viết hoa, số lượng chữ cái viết thường trong chuỗi str
def count_upper_lower(str):
    count={"Số chữ viết hoa":0,"Số chữ viết thường":0}
    for i in str:
        if i.isupper()==True:
            count["Số chữ viết hoa"]+=1
        if i.islower()==True:
            count["Số chữ viết thường"]+=1
    return count
str=input("Mời nhập chuỗi: ")
print(count_upper_lower(str))




# Bài 06: Viết hàm
#         def is_pangram(str, alphabet)
#     đề kiểm tra xem chuỗi str có phải là Pangram không, trả lại True nếu có, False nếu không
#     Ghi chú: Pangram là chuỗi chứa mỗi chữ cái trong bảng alphabet ít nhất 1 lần

def is_pangram(str):
    a=[]
    for i in b:
        if 97<=ord(i)<=122:
            a.append(i)
    print(a)
    if len(a)==26:
        return True
    return False
str=input("Mời nhập chuỗi: ")
b=set(str.lower())
print(is_pangram(str))



#bài 7:Viết hàm
    #     def create_matrix(n, m)
    # xử lý việc tạo ra ma trận n hàng, m cột với giá trị phần tử tại (i, j) = i*j
def create_matrix(n,m):
    a = [[i * j for j in range(1, m+1)] for i in range(1, n+1)]
    return a
n=int(input("Mời nhập số hàng: "))
m=int(input("Mời nhập số cột: "))
print(create_matrix(n,m))




# Bài 08: Viết hàm
#         def body_mass_index(m, h)
#     để tính toán chỉ số BMI của một người với cân nặng m (kg), chiều cao h (m)
#       Viết hàm
#         def bmi_information(m, h)
#     để đưa ra thông tin về chỉ số BMI cũng như phân loại mức độ gầy - béo của người cân nặng m, chiều cao h
import math
def body_mass_index(h,m):
    BMI=round(m/h**2,1)
    if BMI < 18.5:
        print("Bạn đang thiếu cân!")
    if 18.5<BMI<24.9:
        print("Bạn có cơ thể tốt!")
    if 25<BMI<29.9:
        print("Bạn đang thừa cân!")
    if 30<BMI<34.9:
        print("Bạn đang Bị béo phì cấp độ I!")
    if 35 < BMI < 39.9:
        print("Bạn đang Bị béo phì cấp độ II!")
    if BMI>=40:
        print("Bạn đang Bị béo phì cấp độ III!")
    return BMI
print("Đơn vị của chiều cao là: mét \nĐơn vị của cân nặng là: kilogram")
h,m= float(input("Chiều cao của bạn là: ")),float(input("Cân nặng của bạn là: "))
print(body_mass_index(h,m))





# Bài 09: Viết hàm
#         def change_upper_lower(str)
#     chuyển toàn bộ các ký tự in hoa sang in thường và in thường thành in hoa trong str
def change_upper_lower(str):
    for i in a:
        if 97<=ord(i)<=122:
            str+=f"{i.upper()}"
        if 65<=ord(i)<=90:
            str+=f"{i.lower()}"
    return str
a=input("Mời nhập chuỗi: ")
str=""
print(change_upper_lower(str))




# Bài 10: Viết hàm đệ quy đếm và trả về số lượng chữ số lẻ của số nguyên dương n cho trước.
#         Ví dụ: Hàm trả về 4 nếu n là 19922610 (do n có 4 số lẻ là 1, 9, 9, 1)
import math
def count_odd(n):
    count=0
    if n<=0:
        return 0
    else:
        a= n%10
        if a%2==1:
            count+=1
        return count + count_odd(math.trunc(n/10))
n=int(input("Mời nhập số nguyên dương n: "))
print(count_odd(n))





# Bài 11: Cho dãy số Tribonacci với công thức truy hồi sau:
#             F(n) = F(n-1) + F(n-2) + F(n-3),    F(1) = 1, F(2) = 1, F(3) = 2
#     Xây dựng 2 hàm để tìm ra số thứ n trong dãy số theo:
#         + Hàm Đệ quy
#         + Hàm Không đệ quy
##Hàm đệ quy:
def tribonacci(n):
    if 0<=n<=1:
        return n
    else:
        return  tribonacci(n-1)+tribonacci(n-2)
n=int(input("Mời nhập n"))
print(tribonacci(n))
##Hàm không đệ quy
def tribonacci(n):
    f0=0
    f1=1
    fn=1
    if 0<=n<=1:
        return n
    else:
        for i in range(2,n):
            f0=f1
            f1=fn
            fn=f0+f1
        return fn
n=int(input("Mời nhập n"))
print(tribonacci(n))




# Bài 12: Viết hàm
#         def find_x(a_list, x)
#     trả lại tất cả các vị trí mà x xuất hiện trong a_list, nếu không có thì trả lại -1
def find_x(a,x):
    index_x=[]
    if x not in a:
        return -1
    else:
        for i in range(len(a)):
            if a[i]==x:
                index_x.append(i)
        return index_x
a=list(input("Mời nhập list a:"))
x=input("Mời nhập giá trị x: ")
print(a)
print("ị trí xuất hiện của x là: ",find_x(a,x))


