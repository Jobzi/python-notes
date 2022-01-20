class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __eq__(self, __o: object) -> bool:
        return self.x == __o.x and self.y == __o.y


p1 = Point(1, 2)
p2 = Point(2, 3)

#overloading +
print(p1+p2)
# overloading if __eq__
print(p1 == p2)

""" Overlaading about operator
Operator	            Expression	Internally
Addition	            p1 + p2 	p1.__add__(p2)
Subtraction         	p1 - p2 	p1.__sub__(p2)
Multiplication	        p1 * p2 	p1.__mul__(p2)
Power	                p1 ** p2	p1.__pow__(p2)
Division	            p1 / p2 	p1.__truediv__(p2)
Floor Division	        p1 // p2	p1.__floordiv__(p2)
Remainder (modulo)	    p1 % p2	    p1.__mod__(p2)
Bitwise Left Shift	    p1 << p2	p1.__lshift__(p2)
Bitwise Right Shift	    p1 >> p2	p1.__rshift__(p2)
Bitwise AND	            p1 & p2 	p1.__and__(p2)
Bitwise OR	            p1 | p2 	p1.__or__(p2)
Bitwise XOR	            p1 ^ p2	    p1.__xor__(p2)
Bitwise NOT	            ~p1	        p1.__invert__()
"""

# overloading the less than operator
class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({0},{1})".format(self.x, self.y)

    def __lt__(self, other):
        self_mag = (self.x ** 2) + (self.y ** 2)
        other_mag = (other.x ** 2) + (other.y ** 2)
        return self_mag < other_mag

p1 = Point(1,1)
p2 = Point(-2,-3)
p3 = Point(1,-1)

# use less than
print(p1<p2)
print(p2<p3)
print(p1<p3)

""" 
Overloading Comparison Operators
Python does not limit operator overloading to arithmetic operators only. We can overload comparison operators as well.
Operator	                Expression	    Internally
Less than	                p1 < p2	        p1.__lt__(p2)
Less than or equal to	    p1 <= p2	    p1.__le__(p2)
Equal to	                p1 == p2	    p1.__eq__(p2)
Not equal to	            p1 != p2	    p1.__ne__(p2)
Greater than	            p1 > p2	        p1.__gt__(p2)
Greater than or equal to    p1 >= p2    	p1.__ge__(p2)
"""