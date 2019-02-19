from django.db.models import users subject grade
from django.shortcuts import render


import numpy as np

terms = []
subjects = []
units = []
grades = []
term_gwa = []
computed_grade = []
add_gpa = []
add_gwa = []
add_units = []
cgpa = 0.0
total_units_earned = 0.0


# In[2]:


def get_data():
    # code goes here
    choice = 'y'
    choice2 = 'y'
    print("Enter the following information\n\n")

    while True:
        term = input("Term/SY:")
        terms.append(term)
        units.clear()
        grades.clear()
        add_gwa.clear()
        while True:
            subject = input("Enter subject: ")
            unit = input("Enter units: ")
            grade = input("Enter grade: ")
            subjects.append(subject)
            units.append(float(unit))
            grades.append(float(grade))
            choice2 = input("Do you wish to add more subjects?[y/n]: ")
            if(choice2.lower() == 'n' or choice2.lower() == 'no'):
                break
        term_gwa.append(compute_gwa(units, grades))
        choice = input("Do you want to add a new term?[y/n]: ")
        if(choice.lower() == 'n' or choice.lower() == 'no'):
            break
    cgpa = compute_cgpa(term_gwa, add_units)
    print_data(term_gwa, cgpa)
    return


# In[3]:


def add_term_units(units):
    add_units.append(units)
    
    return


# In[4]:


def compute_gwa(units, grades):
    total_units = sum(units)
    gwa = np.dot(units, grades)
    add_gwa.append(gwa)
    computed_gwa = sum(add_gwa)/total_units
    add_term_units(total_units)
    
    return computed_gwa


# In[5]:


def compute_cgpa(term_gwa, total_units):
    total_units_earned = sum(total_units)
    gpa = np.dot(np.squeeze(np.asarray(term_gwa)), add_units)
    computed_gpa = gpa/total_units_earned
    
    return computed_gpa


# In[6]:


def print_data(term_gwa, cgpa):
    print(term_gwa)
    print(cgpa)
    
    return


# In[7]:


get_data()


# In[8]:


gpa = np.dot(np.squeeze(np.asarray(term_gwa)), add_units)
print(gpa)
print(add_units)
print(gpa/12.00)


# In[9]:


add_units.append(7.00)


# In[10]:


print(add_units)


# In[ ]:




