### Day 21 snake game part two - Class inheritance and list slicing

### Class inheritance

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale")


class Fish(Animal):
    def __init__(self):
        super().__init__()

    def breathe(self):
        super().breathe()
        print("underwater")

    def swim(self):
        print("Moving in water")


nemo = Fish()
nemo.swim()
nemo.breathe()
print(nemo.num_eyes)

### List slicing

list = [1, 2, 3, 4, 5, 6]

print(list[2:5]) # 3, 4 , 5
print(list[2:]) # From item with index 2 to the end of the list
print(list[:5]) # From the beginning to item with index 5
print(list[::2]) # From the beginning to the end of the list, skipping every second item
print(list[::-1]) # From the end to the beginning of the list
print(list[2:5:2]) # From item with index 2 to item with index 5, skipping every other element
#Works with tuples as well