class A:
    def show(self):
        print("Showing A")
class B:
    def show(self):
        print("Showing B")
class C(A,B):
    def show(self):
        print("Showing C")

obj=C()
obj.show()