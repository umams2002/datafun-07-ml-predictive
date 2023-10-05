""" List of employee working"""

from Employee import Employee
from decimal import Decimal

class EmployeeList(Employee):

    def __init__(self, firstname, lastname, employeeid, salary,base_salary):
        super().__init__(firstname, lastname, employeeid, salary)
        self.base_salary = base_salary

    @property
    def base_salary(self):
        return self._base_salary

    @base_salary.setter
    def base_salary(self, salary):
        """Set base salary or raise ValueError if invalid."""
        if salary < Decimal('0.00'):
            raise ValueError('Base salary must be >= to 0')
        
        self._base_salary = salary

    def __repr__(self):
        """Return string representation for repr()."""
        return ('Salaried' + super().__repr__() +      
            f'\nbase salary: {self.base_salary:.2f}')