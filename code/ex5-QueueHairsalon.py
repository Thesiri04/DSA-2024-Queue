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
    
    def size(self):
        return len(self.items)
    
    def display(self):
        for idx, customer in enumerate(self.items, start=1):
            print(f"{idx}. {customer['name']} - {customer['service']} (รอประมาณ {customer['waiting_time']} นาที)")

class HairSalon:
    def __init__(self):
        self.queue = Queue()
        self.service_times = {
            "ตัดผม": 30,
            "สระ": 20,
            "ย้อมสี": 60
        }
        self.poped_wait_time = 0
    
    def add_customer(self, name, service):
        waiting_time = self.calculate_waiting_time()
        self.queue.enqueue({"name": name, "service": service, "waiting_time": waiting_time + self.service_times[service]})
        print(f"เพิ่มลูกค้า: {name} ({service})")
    
    def calculate_waiting_time(self):
        if self.queue.is_empty():
            return 0
        return sum([self.service_times[customer['service']] for customer in self.queue.items])
    
    def show_queue(self):
        print("แสดงคิว:")
        if self.queue.is_empty():
            print("ไม่มีลูกค้าในคิว")
        else:
            self.queue.display()
    
    def call_next_customer(self):
        if not self.queue.is_empty():
            customer = self.queue.dequeue()
            print(f"เรียกลูกค้า: {customer['name']}")
            self.update_waiting_times(time_to_deduct = self.service_times[customer['service']])
        else:
            print("ไม่มีลูกค้าในคิว")
    
    def update_waiting_times(self, time_to_deduct):
        for customer in self.queue.items:
            customer['waiting_time'] -= time_to_deduct

    def print(self):
        print(self.queue.items)

# สร้างระบบร้านตัดผม
salon = HairSalon()

# เพิ่มลูกค้าเข้าคิว
salon.add_customer("สมชาย", "ตัดผม")
salon.add_customer("สมหญิง", "ย้อมสี")
salon.add_customer("เนย", "สระ")

# salon.print()

# แสดงคิว
salon.show_queue()

# เรียกลูกค้าคนถัดไป
salon.call_next_customer()
# salon.print()

#แสดงคิวอีกครั้ง
salon.show_queue()
