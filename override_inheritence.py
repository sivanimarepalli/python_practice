# Create a base class Logger with a method log().
# Derive a class FileLogger that overrides log() but still calls the parent method using super().
class Logger:
    def __init__(self,name):
        self.name=name
    def log(self):
        print(f"Hello {self.name}, You have logged in to the system")
class FileLogger(Logger):
    def __init__(self,name):
        super().__init__(name)
    def log(self):
        print(f"Hello {self.name}, You have logged in to the file")
        super().log()

obj=FileLogger("APPLE")
obj.log()
