class Node:
    def __init__(self, coeff, exp):
        self.coeff = coeff 
        self.exp = exp 
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert(self, coeff, exp):
        new_node = Node(coeff, exp)
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node
    
    def display(self):
        current = self.head
        result = []
        while current is not None:
            if current.coeff != 0:
                result.append(f"{current.coeff}x^{current.exp}")
            current = current.next
        print(" + ".join(result) if result else "0")
    
    def add(self, other):
        p1 = self.head
        p2 = other.head
        result = LinkedList()
        
        while p1 is not None and p2 is not None:
            if p1.exp == p2.exp:
                coeff_sum = p1.coeff + p2.coeff
                if coeff_sum != 0:
                    result.insert(coeff_sum, p1.exp)
                p1 = p1.next
                p2 = p2.next
            elif p1.exp > p2.exp:
                result.insert(p1.coeff, p1.exp)
                p1 = p1.next
            else:
                result.insert(p2.coeff, p2.exp)
                p2 = p2.next
        
        while p1 is not None:
            result.insert(p1.coeff, p1.exp)
            p1 = p1.next
  
        while p2 is not None:
            result.insert(p2.coeff, p2.exp)
            p2 = p2.next
        
        return result

poly1 = LinkedList()
poly1.insert(4, 3)
poly1.insert(3, 2)
poly1.insert(2, 0)

poly2 = LinkedList()
poly2.insert(6, 4)
poly2.insert(5, 3)
poly2.insert(4, 2)

print("Polynomial 1:")
poly1.display()
print("Polynomial 2:")
poly2.display()

result_poly = poly1.add(poly2)
print("Sum of Polynomials:")
result_poly.display()
