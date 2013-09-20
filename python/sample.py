import unittest

# Here's our "unit".
def my_partial_fn(x):       # line 1
    if x:                   #      2
        y = 10              #      3
    return y                #      4

def IsEven(n):
    if n % 2 == 0:
        return True
    else: 
        return False

def IsOdd(n):
    return n % 2 == 1

# Here's our "unit tests".
class IsOddTests(unittest.TestCase):

    def testOne(self):
        self.failUnless(IsOdd(1))

    def testTwo(self):
        self.failIf(IsOdd(2))

    def testThree(self):
        self.failIf(IsEven(1))

    def testFour(self):
        self.failUnless(my_partial_fn(1));

def main():
    unittest.main()

if __name__ == '__main__':
    main()
