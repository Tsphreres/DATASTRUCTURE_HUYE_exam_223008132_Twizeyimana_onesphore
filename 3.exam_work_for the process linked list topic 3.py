class DLLNode:
    def __init__(self, item_id, item_name, quantity, price):
        self.item_id = item_id
        self.item_name = item_name
        self.quantity = quantity
        self.price = price
        self.prev = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert_item(self, item_id, item_name, quantity, price):
        new_node = DLLNode(item_id, item_name, quantity, price)
        if self.head is None:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def search_item(self, item_id):
        current = self.head
        while current:
            if current.item_id == item_id:
                return current
            current = current.next
        return None

    def delete_item(self, item_id):
        current = self.head
        while current:
            if current.item_id == item_id:
                if current.prev:
                    current.prev.next = current.next
                if current.next:
                    current.next.prev = current.prev
                if current == self.head:
                    self.head = current.next
                if current == self.tail:
                    self.tail = current.prev
                return current
            current = current.next
        return None

    def display_items(self):
        current = self.head
        while current:
            print(f"Item ID: {current.item_id}, Name: {current.item_name}, Quantity: {current.quantity}, Price: {current.price}\n")
            current = current.next

# Example usage
dll = DoublyLinkedList()
dll.insert_item(1, "Apple", 10, 0.50)
dll.insert_item(2, "Banana", 20, 0.30)
dll.insert_item(3, "Orange", 15, 0.80)

print("Doubly Linked List items in POS system:")
dll.display_items()
print("Search for item 2:", dll.search_item(2).item_name if dll.search_item(2) else "Not found")
dll.delete_item(1)
print("Doubly Linked List items after deleting item 1:")
dll.display_items()