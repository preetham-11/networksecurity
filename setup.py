from setuptools import find_packages,setup
from typing import List

HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str) -> List[str]:
    '''
    This function will return the list of requirements
    '''    
    requirements = []
    try:
        with open(file_path) as file_obj:
            requirements = file_obj.readlines()
            requirements = [req.strip() for req in requirements]

            if HYPHEN_E_DOT in requirements:
                requirements.remove(HYPHEN_E_DOT)
    except FileNotFoundError:
        print("requirements.txt file not found")

    return requirements

setup(
    name='NetworkSecurity',
    version='0.0.1',
    author='Preetham',
    author_email='preethamksathish@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt'),
)