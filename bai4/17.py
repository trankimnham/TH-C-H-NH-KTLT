print("sinh viên : Nguyen Phuoc Hung 205751030110042")

print("Nhập vào số N cần tính tổng các ước số: ")
 
n = int(input())
sum = 0
 
for i in range(1, n+1):
    if (n % i == 0):
        sum += i
 
 
print("Tổng tất cả các ước số ", n, " là: ", sum)
