'''CS5001, final project, made by Shuyao Yu'''

from school_function import *
from culture_function import *
from neighbourhood_function import *
from neighbourhood import *
from visualization import *

CSV_URL1='https://opendata.vancouver.ca/explore/dataset/schools/download/?format=csv&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B'
CSV_URL2='https://opendata.vancouver.ca/explore/dataset/cultural-spaces/download/?format=csv&disjunctive.type=true&disjunctive.primary_use=true&disjunctive.ownership=true&refine.year=2020&timezone=America/Los_Angeles&lang=en&use_labels_for_header=true&csv_separator=%3B'

def main():
    try:
        #school data download and clean:
        school_data=file_download(CSV_URL1)
        school_lst=data_lst(school_data)
        school_name=get_school_name(school_lst)
        school_category=get_school_category(school_lst)
        local_area=get_school_local_area(school_lst)
        #Create the school class object
        school_obj_lst=create_school_object(school_name, school_category, local_area)


        #Cultural_space data download and clean:
        cultural_space=cultural_file_download(CSV_URL2)    #download the cultural_space data
        cultural_data=cultural_lst(cultural_space)
        cultural_name=get_space_name(cultural_data)
        space_type=get_space_type(cultural_data)
        space_local_area=get_space_local_area(cultural_data)


        #Create the Cultural space class object
        cultural_obj_lst=create_culture_object(cultural_name, space_type, space_local_area)


        #Create Neighbourhood object, combining School class and Cultural_space class
        union_area=getting_total_area(local_area, space_local_area)
        union_area.sort()
        area_obj_lst=create_neighbourhood_object(union_area)


        # Calling Neighbourhood method
        adding_school_method(area_obj_lst, school_obj_lst)       
        adding_cultural_method(area_obj_lst, cultural_obj_lst)


        #Do the data analysis, count_dict, showing the number of schools and cultural spaces in each neighbourhood
        count_dict=create_count_dict(area_obj_lst)
        xticklabels=get_xlabel(area_obj_lst)
        display_count_dict=display_dict(count_dict)    

        ratio_dict=cultural_space_per_school(area_obj_lst)
        display_ratio_dict=display_cultural_space_per_school(ratio_dict)

        show_diagram(display_count_dict, xticklabels, display_ratio_dict)

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
      
if __name__ == '__main__':
    main()
