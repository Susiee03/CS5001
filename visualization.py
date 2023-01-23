'''CS5001, final project, made by Shuyao Yu'''

import matplotlib.pyplot as plt
import pandas as pd
DATAFRAME_TITLE='Number of schools and cultural spaces per area'
RATIO_TITLE='Cultural space per school in each area'

def make_bar_graph_from_dictionary(dictn1, title):

    plt.bar(range(len(dictn1)), list(dictn1.values()), align='center')
    plt.xticks(range(len(dictn1)), list(dictn1.keys()))
    plt.xticks(rotation=80)
    plt.title(title)
    plt.show()


def make_bar_graph_from_data_frame(df1, xticklabels, title):

    figure1, ax1 = plt.subplots()
    df1.plot(kind='bar', legend=True, ax=ax1)
    ax1.set_xticklabels(xticklabels)
    ax1.set_title(title)
    figure1.autofmt_xdate()
    plt.show()

def user_first_input():
    '''
    Name/Purpose: user_first_input, ask user to input their choice
    Parameter: None
    Return: user's choice of different data visualization
    '''
    user_first_input=input("Choose the diagram you'd like to see:  \nA, num of school and cultural space each area \nB, cultural_space_per_school in each area\nQ to exit\n")
    return user_first_input


def user_count_dict_input(display_count_dict):
    '''
    Name/Purpose: user_count_dict_input, ask user to input a specific type of data visualization
    Parameter: display_count_dict, formed in main driver file
    Return: user's specific choice
    '''
    
    area_list=list(display_count_dict['Neighbourhood'])
    user_count_input=input(f"Choose Y if you want to see the whole diagram, \nor type the specific area from {area_list} and see the specific number of school and cultural spaces in each area, \nor L to leave\n")   
    return user_count_input


def user_ratio_dict_input(display_ratio_dict):
    '''
    Name/Purpose: user_ratio_dict_input, ask user to input a specific type of data visualization
    Parameter: display_ratio_dict, formed in main driver file
    Return: user's specific choice
    '''
    if not isinstance(display_ratio_dict, dict):
        raise TypeError("The input parameter must be a dict. ")

    choice_list=list(display_ratio_dict.keys())
    user_ratio_input=input(f"Choose Y if you want to see the whole diagram, \nor type the specific local area from {choice_list} and see the specific cultural space per school in each area, \nor X to exit\n")
    return user_ratio_input


def show_diagram(display_count_dict, xticklabels, display_ratio_dict):
    '''
    Name/purpose: show_diagram. Visualized the data according to users' input
    Parameter: display_count_dict, xticklabels, display_ratio_dict. Formed in data dashboard file.
    Return: None
    Raises: TypeError. The input parameter must a dictionary.
    '''
    if not isinstance(xticklabels, list) and not isinstance(display_count_dict, dict) and not isinstance(display_count_dict, dict):
        raise TypeError("The parameter must be a list and two dictionaries. ")
    while True:
        user_choice=user_first_input()
        if user_choice.upper()=='A':  # count_dict  information visualization 
            while True:
                area_choice=user_count_dict_input(display_count_dict)
                if area_choice.upper()=='Y':
                    make_bar_graph_from_data_frame(display_count_dict, xticklabels, DATAFRAME_TITLE)
                elif area_choice in list(display_count_dict['Neighbourhood']):
                    x_label=[area_choice]
                    df_new=display_count_dict[display_count_dict['Neighbourhood']==area_choice]
                    make_bar_graph_from_data_frame(df_new, x_label, f'Number of schools and cultural spaces in {area_choice}')
                elif area_choice.upper()=='L':
                    break
                else:
                    print('Please input a valid choice or type the correct area')

        elif user_choice.upper()=='B':   # ratio dict visualization
            while True:
                ratio_choice=user_ratio_dict_input(display_ratio_dict)
                if ratio_choice.upper()=='Y':
                    make_bar_graph_from_dictionary(display_ratio_dict, RATIO_TITLE)
                elif ratio_choice in display_ratio_dict.keys():
                    v=display_ratio_dict.get(ratio_choice)
                    specific_ratio_dict={ratio_choice: v}
                    make_bar_graph_from_dictionary(specific_ratio_dict, f"Cultural space per school in {ratio_choice}")
                elif ratio_choice.upper()=='X':
                    break
                else:
                    print('Please input a valid choice or type the correct area')
            
        elif user_choice.upper()=='Q':
            break        
        else:
            print('please input a valid choice, from A, B, Q')

