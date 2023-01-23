'''CS5001, final project, made by Shuyao Yu'''

class Cultural_space:
    '''
    Class: Cultural_space
    
    It has attributes, including cultural_name, space_type, and local_area.
    It know how to print the human readable format, and can compare the different
    objects and shows the Boolen True or False. 
    '''
    def __init__(self, cultural_name, space_type, local_area):
        '''
        Name/Purpose : __init__. The default method of the class
        Parameters:
           self -- the current object
           cultural_name : the name of cultural space
           space_type: the type of cultural space
           local_area: the area of cultural space
        
        Raises: ValueError if string is empty, TypeError if information is not string
    '''
        
        if not isinstance(cultural_name, str) and not isinstance(space_type, str) and not isinstance(local_area, str):
            raise TypeError("information must be string")
        
        self.name=cultural_name
        self.cultural_type=space_type
        self.local_area=local_area

    def __str__(self):
        '''
    Name/Purpose: __str__, present the human reading format
    Parameter: self
    Return: the format object information
        '''
        output=self.name+' is a '+self.cultural_type+', locates at '+self.local_area
        return output


    def __eq__(self, other):
        '''
    Name/Purpose: __eq__, test the equality of two objects
    Parameter: self, other
    Return: Boolen True or False
    '''
        if not isinstance(other, Cultural_space):
            return NotImplemented        
        return self.name==other.name
