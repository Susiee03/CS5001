'''CS5001, final project, made by Shuyao Yu'''

import requests
from requests.exceptions import HTTPError
from culture import *
OUTLINER_INDEX=223
HEADER_INDEX=0
CULTURAL_NAME_INDEX=1
CULTURAL_TYPE_INDEX=3
CULTURAL_AREA_INDEX=6

def cultural_file_download(csv_link):
     '''
    Name/purpose: cultural_file_download. Download the cultural_space data from website.
    Parameter: link. csv link.
    Return: cultural_space. Converting the cultural_space csv data content into a list.
    '''
     try:         
        with requests.Session() as s:
            download = s.get(csv_link)
            cultural_space=download.text.rstrip().split('\r')
            del cultural_space[HEADER_INDEX]
        return cultural_space
    
     except HTTPError:
        print('HTTP error 403: Forbidden')
     except ConnectionError:
        print("Connection Error, please check your web connection")
     except Exception:
        print('Some error occurs')
     except NameError:
          print('Please input a valid web address')
     except PermissionError:
          print('Not permitted, please check your permission.')


def cultural_lst(cultural_space):
    '''
    Name/purpose: cultural_lst. Create a list that including the cultural space basic information.
    Parameter: cultural_space, the downloading csv files information in the list.
    Return: data_lst. Cleaning the cultural space unrelated information and put useful information in a list.
    Raises: TypeError. The input parameter must be a list.   
    '''
    if not isinstance(cultural_space, list):
        raise TypeError("The input must be a list. ")
    
    data_lst=[]
    for i in range(len(cultural_space)):
        data_lst.append(cultural_space[i].split(';'))
    del data_lst[OUTLINER_INDEX]
    return data_lst

def get_space_name(data_lst):
    '''
    Name/purpose: get_space_name. Putting cultural space names in a list.
    Parameter: data_lst, the list forming from the cultural_lst(cultural_space) function.
    Return: cultural_name. A list contains only cultural space_name
    Raises: TypeError. The input parameter must be a list.   
    '''
    if not isinstance(data_lst, list):
        raise TypeError("The input must be a list. ")

    cultural_name=[]
    for item in data_lst:
        cultural_name.append(item[CULTURAL_NAME_INDEX])
    return cultural_name

def get_space_type(data_lst):
    '''
    Name/purpose: get_space_type. Putting cultural space type in a list.
    Parameter: data_lst, the list forming from the cultural_lst(cultural_space) function.
    Return: space_type. A list contains only cultural space type
    Raises: TypeError. The input parameter must be a list.   
    '''
    if not isinstance(data_lst, list):
        raise TypeError("The input must be a list. ")

    space_type=[]
    for item in data_lst:
        space_type.append(item[CULTURAL_TYPE_INDEX])
    return space_type
    


def get_space_local_area(data_lst):
    '''
    Name/purpose: get_space_local_area. Putting cultural space local area in a list.
    Parameter: data_lst, the list forming from the cultural_lst(cultural_space) function.
    Return: local_areea. A list contains only cultural space local area
    Raises: TypeError. The input parameter must be a list.   

    '''
    if not isinstance(data_lst, list):
        raise TypeError("The input must be a list. ")
    
    local_area=[]
    for item in data_lst:
        local_area.append(item[CULTURAL_AREA_INDEX])
    return local_area


def create_culture_object(cultural_name, space_type, local_area):
    '''
    Name/purpose: create_culture_object. Create the Cultural_space object based on Cultural_space  class
    Parameter: cultural_name, space_type, local_area. The lists formed before.
    Return: obj_lst. A list contains all the cultural_space ojects.
    Raises: TypeError. The input parameter must be lists.   
    '''
    if not isinstance(cultural_name, list) and not isinstance(space_type, list) and not isinstance(local_area, list):
        raise TypeError("The input parameter must be a list. ")

    obj_lst=[]
    for i in range(len(cultural_name)):
        cultural_object=Cultural_space(cultural_name[i], space_type[i], local_area[i])
        obj_lst.append(cultural_object)
    return obj_lst






