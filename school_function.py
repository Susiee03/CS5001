'''CS5001, final project, made by Shuyao Yu'''

from school import *
from requests.exceptions import HTTPError
import requests
HEADER_INDEX=0
SCHOOL_NAME_INDEX=2
SCHOOL_CATEGORY_INDEX=1
SCHOOL_AREA_INDEX=4

def file_download(link):
     '''
    Name/purpose: file_download. Download the data from website.
    Parameter: link. Website link.
    Return: school_data. Converting the csv data content into a list.
    '''
     try:
        with requests.Session() as s: 
            download = s.get(link)      
            school_data=download.text.rstrip().split('\r')     
            del school_data[HEADER_INDEX]
        return school_data    
    
     except HTTPError:
        print('HTTP error 403: Forbidden')
     except NameError:
          print('Please input a valid web address')
     except ConnectionError:
        print("Connection Error, please check your web connection")
     except Exception:
        print('Some error occurs')


        
def data_lst(school_data):
     '''
    Name/purpose: data_lst. Create a list that including the school basic information.
    Parameter: School_data, the downloading csv files information
    Return: data_lst. Cleaning the school's unrelated information and put useful information in a list.
    Raises: TypeError. The input parameter must be a list.   
     '''
     if not isinstance(school_data, list):
          raise TypeError("The input must be a list. ")

     data_lst=[]
     for i in range(len(school_data)):
         data_lst.append(school_data[i].split(';')) 
     return data_lst     #nested list

def get_school_name(school_lst):
     '''
    Name/purpose: get_school_name. Putting school names in a list.
    Parameter: School_lst, the list forming from the data_lst(school_data) function.
    Return: school_name. A list contains only school_name
    Raises: TypeError. The input parameter must be a list.   
     '''
     if not isinstance(school_lst, list):
          raise TypeError("The input must be a list. ")
    
     school_name=[]
     for item in school_lst:
         school_name.append(item[SCHOOL_NAME_INDEX])
     return school_name

def get_school_category(school_lst):
     '''
    Name/purpose: get_school_category. Putting school category in a list.
    Parameter: School_lst, the list forming from the data_lst(school_data) function.
    Return: school_category. A list contains only school category
    Raises: TypeError. The input parameter must be a list.   
     '''
     if not isinstance(school_lst, list):
          raise TypeError("The input must be a list. ")

     school_category=[]
     for item in school_lst:
         school_category.append(item[SCHOOL_CATEGORY_INDEX])
     return school_category

def get_school_local_area(school_lst):
     '''
    Name/purpose: get_school_local_area. Putting school's local area in a list.
    Parameter: School_lst, the list forming from the data_lst(school_data) function.
    Return: local_area. A list contains only school local area
    Raises: TypeError. The input parameter must be a list.   
     '''
     if not isinstance(school_lst, list):
          raise TypeError("The input must be a list. ")

     local_area=[]
     for item in school_lst:
         local_area.append(item[SCHOOL_AREA_INDEX])     
     return local_area


def create_school_object(school_name, school_category, local_area):
    '''
    Name/purpose: create_school_object. Create the school object based on School class
    Parameter: school_name, school_category, local_area. The lists formed before.
    Return: obj_lst. A list contains all the school ojects.
    Raises: TypeError. The input parameter must be lists.   

    '''
    if not isinstance(school_name, list) and not isinstance(school_category, list) and not isinstance(local_area, list):
        raise TypeError("The input parameter must be a list. ")
    
    obj_lst=[]
    for i in range(len(school_name)):
        school_object=School(school_name[i], school_category[i], local_area[i])
        obj_lst.append(school_object)
    return obj_lst

        


