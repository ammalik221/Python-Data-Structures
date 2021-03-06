"""
Implementation of Linked List using Python 3.0.
"""

class Element(object):
    def __init__(self, value):
        """ An element has two componenets, a value and a reference to the next node. """
        self.value = value
        self.next = None

        
class Linked_List():
    def __init__(self, head=None):
        """ If no value is provided, head's default value is None. """
        self.head = head
        
    def append(self, new_element):
        """ Adding an element at the end of the list """
        # There will be two cases, one, when there isn't a head element and the other when there is a head element
        current = self.head
        if self.head:
            # iterating through the list
            while current.next:
                current = current.next
            # when current.next doesn't exist, that is, it's value is None, add the new element.
            current.next = new_element
        else:
            self.head = new_element
        print("New element inserted")
        
    def get_element_position(self, position):
        """ getting an element at a particular position considering head position = 1"""
        if position < 1:
            print("Enter a valid position(>=1)")
        elif position == 1:
            return self.head
        else:
            count = 1
            current = self.head
            # iterating through the list
            while current and count <= position:
                # when position found return the current element
                if count == position:
                    return current
                current = current.next
                count += 1
            return "Position not found"
        
    def insert_element(self, new_element, position):
        """ insert a new element at a particular position """
        current = self.head
        if position < 1:
            print("Enter a valid position(>=1)")
        elif position == 1:
            new_element.next = self.head
            self.head = new_element
        else:
            count = 1
            # iterating through the loop
            while current and count <= position:
                # when current position is less than required position by 1
                if count == position - 1:
                    new_element.next = current.next
                    current.next = new_element
                    return
                count += 1
                current = current.next
            return "Position Not Found"
        
    def delete_value(self, value):
        """ delete an element of the given value """
        current = self.head
        previous_element = None
        # iterating till current's value is not equal to required value
        while current.value != value and current:
            previous_element = current
            current = current.next
        # update the previous element to point to the element after the current element.
        if previous:
            previous.next = current.next
            current.next = None
        else:
            self.head = current.next

        
if __name__ == "__main__":
    # test cases
    # creating 3 Linked List elements
    a = Element(10)
    b = Element(22)
    c = Element(24)
    d = Element(28)
    e = Element(30)
    
    # creating a Linked List with head a
    linked_list = LinkedList(a)
    
    # appending two elements at the end of the linked list
    linked_list.append(b)
    linked_list.append(c)
    
    # output is - 
    # 10 
    # 22 
    # 24
    linked_list.print_list()
    
    # output is 10 and 22 respectively
    print(linked_list.get_element_position(1).value)
    print(linked_list.get_element_position(2).value)

    linked_list.insert_element(d, 2)
    linked_list.insert_element(e, 5)
    
    # output is -
    # 10
    # 28
    # 22
    # 24
    # 30
    linked_list.print_list()
    
    linked_list.delete_value(10)
    # output is - 
    # 28
    # 22
    # 24
    # 30
    linked_list.print_list()
