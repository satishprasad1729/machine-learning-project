from setuptools import setup
from typing import List


#Declaring variable for setup function
Project_Name='housing-predictor'
Version="0.0.1"
Author='Satish Prasad'
Description='This is my first machine learning project'
Packages=['housing']
Requirement_File_Name='requirements.txt'


def get_requirements_lists()->List[str]:
    '''
    Description:this function is going to return requirements list
    that is mentioned in requirements.txt file

    return This function will return list of libraries contained in requirement.txt file
    '''
    with open(Requirement_File_Name) as requirement_file:
       return requirement_file.readlines()

setup(
name=Project_Name,
version=Version,
author=Author,
description=Description,
packages=Packages,
install_requires=get_requirements_lists()
)

if __name__=='__main__':
    print(get_requirements_lists())