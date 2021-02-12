# Create simple Coordinate class:
class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other_obj):
        x_diff_sq = (self.x - other_obj.x) ** 2
        y_diff_sq = (self.y - other_obj.y) ** 2
        
        return (x_diff_sq + y_diff_sq) ** .5

    def __str__(self):
        return '<' + str(self.x) + ', ' + str(self.y) + '>'

# Simple class to represent fractions:
class Fraction(object):
    def __init__(self, num, denom):
        assert type(num) == int and type(denom) == int, "ints not used"
        self.num = num
        self.denom = denom
  
    def __str__(self):
        return str(self.num) + '/' + str(self.denom)
  
    def __add__(self, other):
        top = self.num*other.denom + self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
  
    def __sub__(self, other):
        top = self.num*other.denom - self.denom*other.num
        bott = self.denom*other.denom
        return Fraction(top, bott)
    
    def __float__(self):
        return self.num/self.denom

    def inverse(self):
        return Fraction(self.denom, self.num)

# Set of integers class:
class IntSet(object):
    def __init__(self):
        self.vals = []

    def insert(self, e):
        if not e in self.vals:
            self.vals.append(e)

    def member(self, e):
        return e in self.vals

    def remove(self, e):
        try:
            self.vals.remove(e)
        except:
            raise ValueError(str(e) + ' not found..')

    def __str__(self):
        self.vals.sort()
        return '{' + ','.join([str(val) for val in self.vals]) + '}'

    
if __name__ == '__main__':
    # Using objects of Coordinate class:
    coord = Coordinate(3, 4)
    origin = Coordinate(0, 0)
    print(coord.distance(origin))
    print(coord)

    # Using objects of class Fraction:
    a = Fraction(1,4)
    b = Fraction(3,4)
    c = a + b
    print(c)
    print(float(c))
    print(Fraction.__float__(c))
    print(float(b.inverse()))

    # Using objects of class IntSet:
    s = IntSet()
    print(s)
    s.insert(3)
    s.insert(4)
    s.insert(3)
    print(s)
    s.member(3)
    s.member(5)
    s.insert(6)
    print(s)
    #s.remove(3)  # leads to an error
    print(s)
    s.remove(3)