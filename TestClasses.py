class MyClass1:
    def __init__(self, attr1 = 'Peng'):
        self.attr1 = attr1
        print('MyClass1: __init__, attr1 = %s' % self.attr1)
    def __str__(self):
        return 'attr1 = %s' % self.attr1
    def __del__(self):
        print('MyClass1: __del__, attr1 = %s' % self.attr1)
    def func1(self):
        print ('MyClass1: func1, attr1 = %s' % self.attr1)
    def func2(self):
        print ('MyClass1: func2, attr1 = %s' % self.attr1)

class MyClass2(MyClass1):
    def __init__(self, attr1, attr2):
        MyClass1.__init__(self, attr1)
        self.attr2 = attr2
        print('MyClass2: __init__, attr1 = %s, attr2 = %s' % (self.attr1, self.attr2))
    def __str__(self):
        return MyClass1.__str__(self) + ", attr2 = %s" % self.attr2
    def __del__(self):
        print('MyClass2: __del__, attr1 = %s' % self.attr1)
    def func1(self):
        print('MyClass2: func1, attr1 = %s, attr2 = %s' % (self.attr1, self.attr2))
    def func2(self):
        print('MyClass2: func2, attr1 = %s, attr2 = %s' % (self.attr1, self.attr2))

# With that, the file can also be imported as a module without running this code
def testCode():
    myClass1a = MyClass1('Bumm')
    myClass1b = MyClass1()
    myClass1a.func1()
    myClass1a.func2()
    print('Set myClass1a = None')
    myClass1a = None
    myClass2 = MyClass2('Zick', 'Zack')
    myClass2.func1()
    myClass2.func2()
    print(myClass2)
    print(myClass1b)
    
if __name__ == '__main__':
    testCode()