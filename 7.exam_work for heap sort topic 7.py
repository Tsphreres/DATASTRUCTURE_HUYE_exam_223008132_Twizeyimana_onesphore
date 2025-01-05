def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i]['priority'] < arr[left]['priority']:
        largest = left

    if right < n and arr[largest]['priority'] < arr[right]['priority']:
        largest = right

    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def build_heap(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

def heap_sort(arr):
    build_heap(arr)
    n = len(arr)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

def extract_max(arr):
    n = len(arr)
    if n == 0:
        return None
    max_item = arr[0]
    arr[0] = arr[n - 1]
    arr.pop()
    heapify(arr, n - 1, 0)
    return max_item

def increase_priority(arr, index, new_priority):
    if new_priority < arr[index]['priority']:
        return "New priority is lower than current priority"
    arr[index]['priority'] = new_priority
    while index > 0 and arr[(index - 1) // 2]['priority'] < arr[index]['priority']:
        arr[index], arr[(index - 1) // 2] = arr[(index - 1) // 2], arr[index]
        index = (index - 1) // 2

def decrease_priority(arr, index, new_priority):
    if new_priority > arr[index]['priority']:
        return "New priority is higher than current priority"
    arr[index]['priority'] = new_priority
    heapify(arr, len(arr), index)

items = [
    {'name': 'Item 1', 'priority': 3},
    {'name': 'Item 2', 'priority': 1},
    {'name': 'Item 3', 'priority': 2},
]

print("Original list:")
for item in items:
    print(f"Name: {item['name']}, Priority: {item['priority']}")

build_heap(items)

print("\nHeap built from list:")
for item in items:
    print(f"Name: {item['name']}, Priority: {item['priority']}")

max_item = extract_max(items)
print(f"\nExtracted max item: Name: {max_item['name']}, Priority: {max_item['priority']}")

print("\nList after extracting max item:")
for item in items:
    print(f"Name: {item['name']}, Priority: {item['priority']}")

increase_priority(items, 1, 5)
print("\nList after increasing priority of index 1 to 5:")
for item in items:
    print(f"Name: {item['name']}, Priority: {item['priority']}")

decrease_priority(items, 1, 0)
print("\nList after decreasing priority of index 1 to 0:")
for item in items:
    print(f"Name: {item['name']}, Priority: {item['priority']}")

heap_sort(items)
print("\nSorted list:")
for item in items:
    print(f"Name: {item['name']}, Priority: {item['priority']}")
