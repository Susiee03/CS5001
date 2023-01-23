'''CS5001, final project, made by Shuyao Yu'''

from school import *
from culture import *

class Neighbourhood:
    '''
    Class: Neighbourhood.
    
    It has attributes, including neighbourhood name.
    And the school_lst and cultural_lst are default empty.
    There are two methods, calling add_school_lst and add_cultural_lst. After calling these
    two methods, the school_lst and cultural_lst can all be added into lst, so we can use these
    data to do the analysis.
    It know how to print the human readable format, and can compare the different
    objects and shows the Boolen True or False. 
    
    '''
    
    def __init__(self, name):
        '''
        Name/Purpose : __init__. The default method of the class
        Parameters:
           self -- the current object
           name : the name of local area
        
        Raises: ValueError if length is zero, TypeError if information is not string
'''
        if not isinstance(name, str):
            raise TypeError("name must be string")
        elif len(name)==0 :
            raise ValueError(" information can't be empty")
        
        self.name=name
        self.school_lst=[]
        self.cultural_lst=[]

    def add_school_lst(self, school):
        '''
        Name/Purpose : add_school_lst. adding related information for neighbourhood class.
        Parameters:
           self -- the current object
          School : a school object
        
        Raises: NotImplemented if the parameter is not a School object
       '''
        if not isinstance(school, School):
            return NotImplemented
        
        self.school_lst.append(school)

    def add_cultural_lst(self, culture):
        '''
        Name/Purpose : add_school_lst. adding related information for neighbourhood class.
        Parameters:
           self -- the current object
          School : a cultural_space object
        
        Raises: NotImplemented if the parameter is not a Cultural_space object
       '''
        if not isinstance(culture, Cultural_space):
            return NotImplemented 
                
        self.cultural_lst.append(culture)
    
            
    def __str__(self):
        '''
    Name/Purpose: __str__, present the human reading format
    Parameter: self
    Return: the format object information
        '''
        
        output='It is '+self.name + ' with '+str(self.school_lst)+' and '+ str(self.cultural_lst)

        return output

    def __eq__(self, other):
        '''
    Name/Purpose: __eq__, test the equality of two objects
    Parameter: self, other
    Return: Boolen True or False
    '''
        if not isinstance(other, Neighbourhood):
            return NotImplemented        

        return self.name==other.name
    
