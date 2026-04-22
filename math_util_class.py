# Create a class MathUtils with:
# A @staticmethod for add(a, b).
# A @classmethod that returns the class name.
# Show how both are called without creating an object.
class MathUtils:
    @staticmethod
    def add(a,b):
        return a+b
    @classmethod
    def class_name(cls):
        return __class__.__name__
print(MathUtils.add(4,6))
print(MathUtils.class_name())
