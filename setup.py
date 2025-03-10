from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    '''
    THIS FUNCTION WILL RETURN THE LIST OF REQUIRMENTS
    '''
    requirments=[]
    with open(file_path) as file_obj:
        requirments=file_obj.readlines()
        requirments=[req.replace("\n","") for req in requirments]
        
        if HYPEN_E_DOT in requirments:
            requirments.remove(HYPEN_E_DOT)
    return requirments    
setup(
    name='mlproject',
    version='0.0.1',
    author='John',
    author_email='johnalladi0306@gmail.com',
    packages=find_packages(),
    install_requirements=get_requirements('requirments.txt')
    
    
)