class OrderNode:
    def __init__(self, order_id, customer_name, order_total):
        self.order_id = order_id
        self.customer_name = customer_name
        self.order_total = order_total
        self.prev = None
        self.next = None

class OrderDoublyLinkedList:
    def __init__(self, max_orders):
        self.head = None
        self.tail = None
        self.max_orders = max_orders
        self.current_orders = 0

    def insert_order(self, order_id, customer_name, order_total):
        new_node = OrderNode(order_id, customer_name, order_total)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

        self.current_orders += 1
        # If the number of orders exceeds the maximum, remove the oldest order (head)
        if self.current_orders > self.max_orders:
            self.delete_oldest_order()

    def delete_oldest_order(self):
        if self.head is None:
            return
        old_head = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        else:
            self.tail = None
        self.current_orders -= 1
        return old_head

    def search_order(self, order_id):
        current = self.head
        while current:
            if current.order_id == order_id:
                return current
            current = current.next
        return None

    def delete_order(self, order_id):
        current = self.head
        while current:
            if current.order_id == order_id:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                self.current_orders -= 1
                return current
            current = current.next
        return None

    def display_orders(self):
        current = self.head
        while current:
            print(f"Order ID: {current.order_id}, Customer Name: {current.customer_name}, Order Total: {current.order_total}\n")
            current = current.next

# Example usage
max_orders = 3
order_dll = OrderDoublyLinkedList(max_orders)
order_dll.insert_order(1, "Alice", 150.00)
order_dll.insert_order(2, "Bob", 200.00)
order_dll.insert_order(3, "Charlie", 250.00)

print("Orders in POS system:")
order_dll.display_orders()

print("Inserting a new order:")
order_dll.insert_order(4, "David", 300.00)
print("Orders after inserting the fourth order (should remove the oldest order):")
order_dll.display_orders()

print("Search for order 2:", order_dll.search_order(2).customer_name if order_dll.search_order(2) else "Not found")
order_dll.delete_order(2)
print("Orders after deleting order 2:")
order_dll.display_orders()
