print("sinh viên : Nguyen Phuoc Hung")
print("mssv: 205751030110042")
print("###############")
#################
class Circle(object):
    def __init__(self, r):
        self.radius = r
###########################
    def area(self):
       return self.radius**2*3.14
aCircle = Circle(2)
print (aCircle.area())

