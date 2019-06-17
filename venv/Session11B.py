"""
    Inheritance Types:
    1. Single Level
    2. Multi Level
    3. Hierarchy
    4. Multiple
    5. Hybrid

    Zomato : 1 to 4

    Restaurant

    Indian, Chinese, Thai

    Type
    Veg, NonVeg

    Club
    Family, DabceClub etc...

    Restaurant(Indian, Chinese)

    protected and private
    _  __


"""

# Single Level
class A:
    pass

class B(A):
    pass

# Multi Level
class C(B):
    pass

# Hierarchy
class D(A):
    pass

# Multiple
class E:
    pass

class F(A,E):
    pass

# Hybrid
class G(F):
    pass