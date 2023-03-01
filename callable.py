#the callable() method returns True 
#if the object passed appears callable
#if not, it returns False

#syntax - callable(object)

x = 5
print(callable(x)) #False

def testFunction():
    print("Test")

y = testFunction

print(callable(y)) #True
print(callable(testFunction)) #True

class Foo:
    def __call(self):
        print("Test")

fooObj = Foo()

fooObj() #Test

print(callable(Foo)) #True