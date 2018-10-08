class Pointers:
    def __init__(self, day = None):
        self.day = day
        self.next = None


obj1 = Pointers("Mon")
obj2 = Pointers("Fri")
obj3 = Pointers("Wed")
obj4 = Pointers("Tue")
obj5 = Pointers("Thr")
obj6 = Pointers("Sat")

obj1.next = obj4
obj4.next = obj3
obj3.next = obj5
obj5.next = obj2
obj2.next = obj6

# starting value
current_value = obj1

while current_value:
    print(current_value.day)
    current_value = current_value.next

