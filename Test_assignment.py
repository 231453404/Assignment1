import unittest
import operator

print("*"*10,"Original Code Below","*"*10)
def record(line):  #used to examplify a string test
    if line == line.upper():
	    return print("Name is uppercase: ",line)
    else:
	    return print("You have not entered Name in uppercase: ",line)

def add(x,y):
    return x+y

def minus(x,y):
    return x-y
    
def mul(x,y):
    return x*y
    
def divide(x,y):
    if y==0:
        print("Cannot divide by zero")
    else:
        return x/y
        

x,y=5,5
record("Jayesha")
record("JAYESHA")
print(("The Addition of"),x,"and",y,("is: "),add(x,y))
print(("The Subtraction of"),x,"and",y,("is: "),minus(x,y))
print(("The Multiplication of"),x,"and",y,("is: "),mul(x,y))
print(("The Division of"),x,"and",y,("is: "),divide(x,y))


print("*"*10,"Testing Below","*"*10)
class Testing_Example_Suite(unittest.TestCase):
    
    def test_string(self):
        self.assertTrue('Name'.isupper()) #Testing if uppercase
        self.assertTrue('NAME'.isupper()) #Testing if uppercase
        
    def test_textwritten(self):
        self.assertIsNotNone("NAME","Value is not written")  #Testing if value is written
        
    def test_add(self):
        ans = operator.add(5,5)
        self.assertEqual(ans,15)   #Testing if ans is equal
        self.assertEqual(ans,10)
        
    def test_minus(self):
        ans = operator.sub(5,5)
        self.assertEqual(ans,0)
        self.assertEqual(ans,10)

    def test_mul(self):
        ans = operator.mul(5,5)
        self.assertEqual(ans,25)
        self.assertEqual(ans,5)
        
    def test_divide(self):
        ans = 5/5
        self.assertEqual(ans,1)
        self.assertEqual(ans,0)
        
        with assertRaises(Error):       #testing Condition
            operator.divide(10,0)

unittest.main()
