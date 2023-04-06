
# In Python, the @classmethod decorator is used to declare a method in the class as a 
# class method that can be called using ClassName.MethodName(). 
# The class method can also be called using an object of the class.

# The @classmethod is an alternative of the classmethod() function. It is recommended to use the 
# @classmethod decorator instead of the function because it is just a syntactic sugar.

# @classmethod Characteristics
# Declares a class method.
# The first parameter must be cls, which can be used to access class attributes.
# The class method can only access the class attributes but not the instance attributes.
# The class method can be called using ClassName.MethodName() and also using object.
# It can return an object of the class.

# class Student:
#     name = 'unknown' # class attribute
#     def __init__(self):
#         self._age = 20 # instance attribute

#     @classmethod
#     def tostring(cls):
#         print('Student Class Attributes: name=', cls.name)
        # print('Student Class Attributes: name=', cls.name,'age = ', cls._age)        

    # Above, the Student class contains a class attribute name 
    # and an instance attribute age. The tostring() method is decorated with 
    # the @classmethod decorator that makes it a class method, which can be 
    # called using the Student.tostring(). Note that the first parameter of any class 
    # ethod must be cls that can be used to access the class's attributes. You can give 
    #     any name to the first parameter instead of cls.

# Access Class Method
# Student.tostring()

# Calling Class Method using Object
# std = Student()
# std.tostring()

# The class method can also be used as a factory method to get an object of the class, as shown below.
class Student:
    
    def __init__(self, name, age):
        self.name = name  # instance attribute
        self.age = age # instance attribute

    @classmethod
    def getobject(cls):
        return cls('Steve', 25)
    
std = Student.getobject()
print(std.name)
print(std.age)


# @classmethod
# Declares a class method.
# It can access class attributes, but not the instance attributes.
# It can be called using the ClassName.MethodName() or object.MethodName().
# It can be used to declare a factory method that returns objects of the class.

# @staticmethod
# Declares a static method.
# It cannot access either class attributes or instance attributes.
# It can be called using the ClassName.MethodName() or object.MethodName().
# It cannot return an object of the class.