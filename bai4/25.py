print("sinh viên : Nguyen Phuoc Hung 205751030110042")
values = input("Nhập dãy số của bạn, cách nhau bởi dấu phẩy: ")
numbers = [x for x in values.split(",") if int(x)%2!=0]
print (",".join(numbers))
