class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, item):
        self.items.append(item)
    
    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        return None
    
    def front(self):
        if not self.is_empty():
            return self.items[0]
        return None
    
    def size(self):
        return len(self.items)
    
    def display(self):
        print(f"Queue: {self.items}")
    
    def clear(self):
        self.items = []
        print("Queue is cleared")

# สร้าง Queue
q = Queue()

# ทดสอบ 1: ตรวจสอบคิวว่าง
print("คิวว่างหรือไม่:", q.is_empty())  # ควรได้ True

# ทดสอบ 2: เพิ่มข้อมูล
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()  # ควรได้ [1, 2, 3]

q.clear()
q.display()