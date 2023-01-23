'''CS5001, final project, made by Shuyao Yu'''

from culture import *
from neighbourhood import *
from school_function import *
import pandas
HEADER=('Neighbourhood', 'School', 'Cultural') 

# Data analysis, according to neighbourhood class
def getting_total_area(local_area, space_local_area):
    '''
    Name/purpose: getting_total_area. Generating all the local area that owned by School and Cultural_space
    Parameter: local_area, space_local_area. The local area list of school and cultural space.
    Return: res. A list of total local area
    Raises: TypeError. The input parameter must be a list.   

    '''
    if not isinstance(local_area, list) and not isinstance(space_local_area, list):
        raise TypeError("The input must be a list. ")
    
    set_school_area=set(local_area)
    set_space_area=set(space_local_area)
    total_area=set_school_area.union(set_space_area)
    res=list(total_area)
    return res


def create_neighbourhood_object(total_local_area):
    '''
    Name/purpose: create_neighbourhood_object. Create the neighbourhood object based on Neighbourhood  class
    Parameter: total_local_area. The lists formed before.
    Return: obj_lst. A list contains all the neighbourhood ojects.
    Raises: TypeError. The input parameter must be lists.   
    '''
    if not isinstance(total_local_area, list):
        raise TypeError("The input parameter must be a list. ")

    obj_lst=[]
    for i in range(len(total_local_area)):
        neighbourghood_object=Neighbourhood(total_local_area[i])
        obj_lst.append(neighbourghood_object)
    return obj_lst


def adding_school_method(area_obj_lst, school_obj_lst):
    '''
    Name/purpose: adding_school_method. Call the Neighbourhood class method: add_school_lst. 
    Parameter: area_obj_lst, school_obj_lst. Two object lists.
    Return: None
    Raises: TypeError. The input parameter must be lists.   
    '''
    if not isinstance(area_obj_lst, list) and not isinstance(school_obj_lst, list):
        raise TypeError("The input parameter must be a list. ")

    for i in range(len(area_obj_lst)):
        for j in range(len(school_obj_lst)):            
            if area_obj_lst[i].name==school_obj_lst[j].local_area:
                area_obj_lst[i].add_school_lst(school_obj_lst[j])

            
def adding_cultural_method(area_obj_lst, cultural_obj_lst):
    '''
    Name/purpose: adding_cultural_method. Call the Neighbourhood class method: add_culture_lst. 
    Parameter: area_obj_lst, cultural_obj_lst. Two object lists.
    Return: None
    Raises: TypeError. The input parameter must be lists.   
    '''
    if not isinstance(area_obj_lst, list) and not isinstance(cultural_obj_lst, list):
        raise TypeError("The input parameter must be a list. ")
    
    for i in range(len(area_obj_lst)):
        for j in range(len(cultural_obj_lst)):
            if area_obj_lst[i].name==cultural_obj_lst[j].local_area:
                area_obj_lst[i].add_cultural_lst(cultural_obj_lst[j])
                

# data analysis function    
def create_count_dict(area_obj_lst):
    '''
    Name/purpose: create_count_dict. Using Neighbourhood class to analysis two data, count the num
    of school and cultural space per area, store the result in a dictionary.
    Parameter: area_obj_lst. Neighbourhood object list.
    Return: count_dict. A dictionary
    Raises: TypeError. The input parameter must be lists.   
    '''
    if not isinstance(area_obj_lst, list):
        raise TypeError("The input parameter must be a list. ")

    local_area=[]
    school_num=[]    
    cultural_space_num=[]
    count_dict={}
    for item in area_obj_lst:
        local_area.append(item.name)
        school_num.append(len(item.school_lst))        
        cultural_space_num.append(len(item.cultural_lst))
    data=(local_area, school_num, cultural_space_num)    
    count_dict=dict(zip(HEADER, data))
    return count_dict

def get_xlabel(area_obj_lst):
    '''
    Name/purpose: get_xlabel. Get x label to create the dataframe graph
    Parameter: area_obj_lst. Neighbourhood object list.
    Return: local_area. A list that will be the x label in graph
    Raises: TypeError. The input parameter must be lists.   
    '''
    if not isinstance(area_obj_lst, list):
        raise TypeError("The input parameter must be a list. ")
    local_area=[]
    for item in area_obj_lst:
        local_area.append(item.name)
    return local_area


def display_dict(count_dict):  
    '''
    Name/purpose: display_dict. Display the dict just created.
    Parameter: count_dict. The analysis dictionary
    Return: count_data
    Raises: TypeError. The input parameter must a dictionary.   
    '''
    if not isinstance(count_dict, dict):
        raise TypeError("The input parameter must be a dictionary. ")

    count_data=pandas.DataFrame(count_dict)
    return count_data


def cultural_space_per_school(area_obj_lst):
    '''
    Name/purpose: create_count_dict. Using Neighbourhood class to analysis two data.
    Calculate the number of cultural spaces per school in each area, store the result in a dictionary.
    Parameter: area_obj_lst. Neighbourhood object list.
    Return: count_dict. A dictionary
    Raises: TypeError. The input parameter must be lists.   
    '''
    if not isinstance(area_obj_lst, list):
        raise TypeError("The input parameter must be a list. ")

    local_area=[]
    school_num=[]    
    cultural_space_num=[]
    ratio=[]
    ratio_dict={}
    for item in area_obj_lst:
        local_area.append(item.name)
        school_num.append(len(item.school_lst))        
        cultural_space_num.append(len(item.cultural_lst))
        if len(item.school_lst)==0:
            ratio.append('NA')  # NoneZeroDivision
        else:
            ratio.append(round(len(item.cultural_lst)/len(item.school_lst), 3))
    for i in range(len(local_area)):
        ratio_dict[local_area[i]]=ratio[i]
    return ratio_dict
    
def display_cultural_space_per_school(ratio_dict):
    '''
    Name/purpose: display_cultural_space_per_school. Display the dict just created.
    Parameter: ratio_dict. The analysis dictionary
    Return: ratio_display_dict
    Raises: TypeError. The input parameter must a dictionary.   
    '''
    if not isinstance(ratio_dict, dict):
        raise TypeError("The input parameter must be a dictionary. ")

    ratio_display_dict={}
    for k,v in ratio_dict.items():
        if v != 'NA':
            ratio_display_dict[k]=v
    return ratio_display_dict



