from setuptools import setup
from typing import List


# Declaring variable for setup function
Project_Name = 'housing-predictor'
Version = "0.0.5"
Author = 'Satish Prasad'
Description = 'This is my first machine learning project'
Requirement_File_Name = 'requirements.txt'
HYPHEN_E_DOT = '-e .'


def get_requirements_lists() -> List[str]:
    '''
    Description: this function is going to return requirements list
    that is mentioned in requirements.txt file

    return: This function will return list of libraries contained in requirement.txt file
    '''
    with open(Requirement_File_Name) as requirement_file:
        requirement_list = requirement_file.readlines()
        requirement_list = [requirement_name.replace("\n", "") for requirement_name in requirement_list]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list


setup(
    name=Project_Name,
    version=Version,
    author=Author,
    description=Description,
    packages=['housing'],
    install_requires=get_requirements_lists()
)

if __name__ == '__main__':
    print(get_requirements_lists())
