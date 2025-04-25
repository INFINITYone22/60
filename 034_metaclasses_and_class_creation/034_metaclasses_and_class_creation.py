class MyMeta(type):
    def __new__(cls, name, bases, attrs):
        attrs['attribute'] = 'Custom attribute'
        return super().__new__(cls, name, bases, attrs)

class MyClass(metaclass=MyMeta):
    pass

instance = MyClass()
print(instance.attribute)
