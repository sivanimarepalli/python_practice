# Create two classes Writer and Reader with methods write() and read().
# Derive a class Editor that inherits from both and uses both methods.
class Writer:
    def __init__(self,name):
        self.name=name

    def write(self):
        print(f"Hello {self.name},This is the write function in Writer class")
    def read(self):
        print("This is the read function in Writer class")
class Reader:
    def __init__(self,name):
        self.name=name
    def write(self):
        print(f"Hello {self.name},This is the write function in Reader class")
    def read(self):
        print("This is the read function in Reader class")
class Editor (Writer,Reader):
    def __init__(self,name):
        super().__init__(name)
obj=Editor("ABC")
Writer.write(obj)
Writer.read(obj)
Reader.write(obj)
Reader.read(obj)

