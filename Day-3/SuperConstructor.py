class Parent:
    def __init__(self):
        print("Parent Cpnstructor")
class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child Constructor")

obj = Child()