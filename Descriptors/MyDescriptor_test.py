class MyDescriptor:
    def __set__(self, instance, value):
        print(f"Setting value: {value}")
        instance._value = value

    def __get__(self, instance, owner):
        return instance._value


class MyClass:
    attribute = MyDescriptor()
    state = StateDescriptor()


# Normal usage via instance
obj = MyClass()
obj.attribute = 42  # Triggers MyDescriptor.__set__
obj.state = [0,1]

#print(obj.attribute)
#print(obj.state)
#print(type(obj.state))