__repr__ is for developers

__str__ is more for laymans

!r returns the value of r in single quotes (')

main difference between __repr__ and __str__ is that __str__ is used by the print and __repr__ is used when we directly call the object. main use of __repr__ is for debugging , so that we can see which class it belongs to and how it is behaving.



###opertor overloading
arthmetic operators - need two operands and returns the result for that
when we write "a"+"b" we get "ab"

there is already defined work for the operator and its mainly for the integres and float numbers
but let say we want them to work more , thats called operator overloading, defining extra work for them in class itself.

eg. 

def __sub__(self,other):
    return math.dist(self.coords,other.coords)
#here it return the distance between two points a and b with some coordinates in the plane.

if not defined it return the invalid operation error.



@property : a method that pretends to be an attribute
@setter , @getter , @deleter
@cached_property : calculate/compute it and keep it in memory


