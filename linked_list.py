class Days:
    def __init__(self, day=None):
        self.day = day
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Print the linked list
    def list_print(self):
        # starting value
        current_value = self.head
        while current_value is not None:
            print(current_value.day)
            current_value = current_value.next

    def insert_begining(self, front_value):
        new_day = Days(front_value)
        # Update the new nodes next val to existing node
        new_day.next = self.head
        self.head = new_day

    def insert_end(self, end_value):
        new_day = Days(end_value)



lst_obj = LinkedList()
# obj of Days is copied to the object of linked list
lst_obj.head = Days("Mon")

obj2 = Days("Fri")
obj3 = Days("Wed")
obj4 = Days("Tue")
obj5 = Days("Thr")
obj6 = Days("Sat")

# Link first Node to second node
lst_obj.head.next = obj4

# Link second Node to third node
obj4.next = obj3
obj3.next = obj5
obj5.next = obj2
obj2.next = obj6

lst_obj.list_print()
lst_obj.insert_begining("Sun")
print("After inserting sun at the begining")
lst_obj.list_print()
lst_obj.insert_end("Next week")
print("After inserting next week at the end")
lst_obj.list_print()
