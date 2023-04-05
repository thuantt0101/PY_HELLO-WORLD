# The super() function in Python makes class inheritance more manageable 
# and extensible. The function returns a temporary object that allows reference to a parent class by the keyword super.

# The super() function has two major use cases:

# To avoid the usage of the super (parent) class explicitly.
# To enable multiple inheritances​.

class Parent:
    def self_intro(self):
        print("this is parent class")
    
    def parent_method(self):
        print("this is a parent method")

class Children(Parent):
    def self_intro(self):
        print("this is a children class")
    
    def family_intro(self):
        self.self_intro() # Same as Children.selt_intro(self)
        Parent.self_intro(self) # Parent is called directly

c = Children()
c.family_intro()

# We could do the same above using super() method

class Children2(Parent):
    def self_intro(self):        
        print("this is a childen2 class")
    
    def family_intro(self):
        self.self_intro()
        super().self_intro() 
        # super() function now return a object from Children class is Parent and call self_intro()
        # viec nay giup tranh bi loi chinh ta
        # hoac ban co nhu cau doi ten lop cha
        # hoac co nhu cau ke thua tu lop khac

c1 = Children2()
c1.family_intro()



