class DescriptorClassStorage(object):
    """ descriptor example """
    def __init__(self, default=None):
        self.value = default

    def __get__(self, instance, cls):
        return self.value

    def __set__(self, instance, value):
        self.value = value


class StoreClass(object):
    attr = DescriptorClassStorage(10)


store1 = StoreClass()
store2 = StoreClass()

print(store1.attr, store2.attr)  # 10, 10

store1.attr = 30

print(store1.attr, store2.attr) # 30, 30