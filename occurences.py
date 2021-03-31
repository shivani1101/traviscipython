def findOccurences(source,matchChar):
    """Assumes source is a string and matchChar is a matchCharacter
    return number of occurences"""
    occurence = 0
    for char in source:
        if char==matchChar: occurence+=1
    return occurence

def isPrime(number):
    """assumes number is an integer finds
    if it is also prime"""
    if number==2: return True
    for factor in range(2,int(math.sqrt(number))+1):
        if isDivisible(number,factor): return False
    return True

def isDivisible(number,factor):
    """finds if the number is divisble by factor 
    returns a boolean"""
    return number%factor==0

def multiply(factor1, factor2):
    if factor1>factor2: return multiply(factor2, factor1)
    Sum=0
    for i in range(0,factor1):
        Sum=Sum+factor2
    return Sum

def recursive(factor1, factor2):
    if factor1>factor2: return recursive(factor2, factor1)
    if factor1==1: return factor2
    return recursive(factor1-1,factor2)+factor2

def factorial(n):
    if n <=2: return n
    return n*factorial(n-1)

def fibonacci(n):
    if n<=1: return n
    return fibonacci(n-1)+fibonacci(n-2)

def palindrome(string):
    """check if string is a palindrome"""
    if string=='':return True
    if string[0]==string[-1]: return palindrome(string[1:-1])
    return False

def perfectCube(nCube):
    cube = False
    for integer in range(int(abs(nCube)**(1/3))+2): 
        if integer**3==abs(nCube):
            cube = True
            break
    return cube

def biggestOdd(list1):
    bigOdd = 0
    for integer in list1:
        if(integer%2==1 and (bigOdd==0 or integer>bigOdd)):
            bigOdd = integer
    return bigOdd

def biggestBuried(s):
    s+=' '
    list1 =[]
    string =''
    for i in s:
        if i.isdigit():
            string+=i
        else:
            if string=='':  pass
            else:   list1.append(int(string))
            string=''            
    if list1:
        string=max(list1)
    else:
        string=0
    return string

def binary(x):
    if x ==0:
        return '0'
    if x == 1:
        return '1'
    return binary(x//2)+binary(x%2)

import unittest
import math
class findOccurencesTests(unittest.TestCase):
    def test0(self):
        self.assertEqual(findOccurences('','a'),0)
    def test1(self):
        self.assertEqual(findOccurences('hello','a'),0)
    def test3(self):
        self.assertEqual(findOccurences('a','a'),1)
    def test4(self):
        self.assertEqual(findOccurences('hello','e'),1)
    def test5(self):
        self.assertEqual(findOccurences('hello','l'),2)

class isPrimeTests(unittest.TestCase):
    def test0(self):
        self.assertTrue(isPrime(2))
    def test1(self):
        self.assertTrue(isPrime(3))
    def test2(self):
        self.assertFalse(isPrime(4))
    def test3(self):
        self.assertFalse(isPrime(6)) 
    def test4(self):
        self.assertFalse(isPrime(15))
    def test5(self):
        self.assertTrue(isPrime(31))
    def test6(self):
        self.assertTrue(isPrime(100000007))

class isDivisibleTests(unittest.TestCase):
    def test0(self):
        self.assertTrue(isDivisible(4,2))

class palindromeTests(unittest.TestCase):
    def test0(self):
        self.assertFalse(palindrome("abc"))
    def test1(self):
        self.assertTrue(palindrome("a"))
    def test2(self):
        self.assertTrue(palindrome('madamimadam'))
    def test3(self):
        self.assertTrue(palindrome(""))

class biggestOddTests(unittest.TestCase):
    def test0(self):
        self.assertTrue(perfectCube(0))
    def test1(self):
        self.assertTrue(perfectCube(1))
    def test3(self):
        self.assertFalse(perfectCube(2))  
    def test4(self):
        self.assertTrue(perfectCube(8))
    def test5(self):
        self.assertTrue(perfectCube(-125)) 

class perfectCubeTests(unittest.TestCase):
    def test0(self):
        self.assertEqual(biggestOdd([]),0)
    def test1(self):
        self.assertEqual(biggestOdd([1,2,3,4]),3)
    def test3(self):
        self.assertEqual(biggestOdd([4,2,0,8]),0)  
    def test4(self):
        self.assertEqual(biggestOdd([1]),1)
    def test5(self):
        self.assertEqual(biggestOdd([1,2,3,4,5,6,7,8,9]),9)
    def test6(self):
        self.assertEqual(biggestOdd([-1,1]),1)

class biggestBuriedTests(unittest.TestCase):
    def test0(self):
        self.assertEqual(biggestBuried('abcd51kkk3kk19ghi'),51)
    def test1(self):
        self.assertEqual(biggestBuried('kkk32abce@@-33bb14zzz'),33)
    def test3(self):
        self.assertEqual(biggestBuried('this15isast22ring-55'),55)  
    def test4(self):
        self.assertEqual(biggestBuried('uguyfytdtyr'),0)

class binaryTests(unittest.TestCase):
    def test0(self):
        self.assertEqual(binary(0),'0')
    def test1(self):
        self.assertEqual(binary(11),'1011')

if __name__ == '__main__':
    unittest.main(exit=False)
