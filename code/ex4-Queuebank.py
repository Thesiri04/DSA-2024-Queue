class Queue:
    def __init__(self):
        self.items = []
    
    def is_empty(self):
        return len(self.items) == 0
    
    def enqueue(self, customer):
        self.items.append(customer)
    
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
        for customer in self.items:
            print(f"ลูกค้า: {customer['name']}, ธุรกรรม: {customer['transaction']}")
            
class Bank:
    def __init__(self):
        self.queue = Queue()
        self.average_service_time = 5  # นาทีต่อคน
    
    def add_customer(self, name, transaction):
        self.queue.enqueue({"name": name, "transaction": transaction})
        print(f"เพิ่มลูกค้า {name} เข้าคิวสำหรับธุรกรรม {transaction}")
        
    def serve_customer(self):
        if not self.queue.is_empty():
            customer = self.queue.dequeue()
            print(f"กำลังให้บริการลูกค้า: {customer['name']} สำหรับธุรกรรม {customer['transaction']}")
        else:
            print("ไม่มีลูกค้าในคิว")
            
    def show_queue(self):
        print("คิวปัจจุบัน:")
        self.queue.display()
        print(f"จำนวนคิวที่รอ: {self.queue.size()}")
    
    def estimated_waiting_time(self):
        waiting_time = self.queue.size() * self.average_service_time
        print(f"เวลารอโดยประมาณ: {waiting_time} นาที")

# สร้างระบบธนาคาร
bank = Bank()

# เพิ่มลูกค้าเข้าคิว
bank.add_customer("เนย", "ฝากเงิน")
bank.add_customer("โจ้", "ถอนเงิน")
bank.add_customer("ข้าวต้มมัด", "ชำระบิล")

# แสดงสถานะคิวและเวลารอโดยประมาณ
bank.show_queue()
bank.estimated_waiting_time()

# ให้บริการลูกค้า
bank.serve_customer()
bank.serve_customer()

# แสดงสถานะคิวอีกครั้งและเวลารอที่ปรับปรุงแล้ว
bank.show_queue()
bank.estimated_waiting_time()
