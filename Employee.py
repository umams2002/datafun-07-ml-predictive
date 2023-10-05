""" Employee base class"""

class Employee:
    def __init__(self, firstname,lastname, employeeid, salary):
        self._firstname = firstname
        self._lastname = lastname
        self._employeeid = employeeid
        self._salary = salary
    
    @property
    def firstname(self):
        return self._firstname
    
    @property
    def lastname(self):
        return self._lastname
    
    @property
    def employeeid(self):
        return self._employeeid
    
    @property
    def salary(self):
        return self._salary
    

    def __repr__(self):
        """Return string representation for repr()."""
        return ('Employee: ' + 
                f'{self.firstname} {self.lastname}\n' +
                f'employeeid: {self.employeeid}\n' +
                f'salary: {self.salary}')