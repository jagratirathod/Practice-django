from django.db import models

# Create your models here.


class MyModel(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    
    def __str__(self):
        return self.name

    @property
    def full_description(self):
        return f"{self.name}: {self.description}"
    
    # MyModel.objects.get(id=1).full_description


class Employee(models.Model):
    name = models.CharField(max_length=100)
    position = models.CharField(max_length=50)
    salary = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


    @classmethod
    def get_high_paid_employees(cls, min_salary):
        """
        A class method to retrieve all employees with a salary greater than or equal to the specified amount.
        """
        return cls.objects.filter(salary__gte=min_salary)


        # Employee.get_high_paid_employees(min_salary=50000)
        # Employee.get_high_paid_employees(500)
    


class Department(models.Model):
    name = models.CharField(max_length=255)
    city = models.CharField(max_length=50)

    def __str__(self):
        return self.name


    # @staticmethod
    # def my_static_method():
    #     return "This is a static method."

    # Department.my_static_method()

    # ---------------------------------------------------------------------

    # @staticmethod
    # def my_static_method(name):
    #     return f"This is an instance method. Name: {name}"
    
    # Department.my_static_method("riya")
    
    # -----------------------------------------------------------------------

    # @staticmethod
    # def my_static_method(self):
    #     return f"This is an instance method. Name: {self.name}"
    
    # TypeError: my_static_method() missing 1 required positional argument: 'self'

    # In staticmethod , self will not work

    # --------------------------------------------------------------------------

    # def instance_method(self):
    #     # This is an instance method
    #     return f"This is an instance method. Name: {self.name}, City: {self.city}"

    # Department.objects.last().instance_method()

# -------------------------------------------------------------------------------
    
    def instance_method():
        return f"This is an instance method. Name:"

    # Department.instance_method()

    # Department.objects.last().instance_method()                                     - wrong way
    # TypeError: instance_method() takes 0 positional arguments but 1 was given