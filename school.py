'''CS5001, final project, made by Shuyao Yu'''

class School:
    '''
    Class: School
    
    It has attributes, including school_name, school_category, local_area.
    It know how to print the human readable format, and can compare the different
    objects and shows the Boolen True or False. 

    '''
    
    def __init__(self, school_name, school_category, local_area):
        '''
        Name/Purpose : __init__. The default method of the class
        Parameters:
           self -- the current object
           school_name : the name of school
           school_category: the category of school
           local_area: the area of school
        
        Raises: ValueError if string is empty, TypeError if information is not string
'''
        if not isinstance(school_name, str) and not isinstance(school_category, str) and not isinstance(local_area, str):
            raise TypeError("information must be string")
        self.school_name=school_name
        self.school_category=school_category
        self.local_area=local_area

    def __str__(self):
        '''
    Name/Purpose: __str__, present the human reading format
    Parameter: self
    Return: the format object information
        '''
        output=self.school_name+' is a '+self.school_category+ ', locates at '+self.local_area
        return output

    def __eq__(self, other):
        '''
    Name/Purpose: __eq__, test the equality of two objects
    Parameter: self, other
    Return: Boolen True or False
    '''
        if not isinstance(other, School):
            return NotImplemented        
        return self.school_name==other.school_name
