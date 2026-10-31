from setuptools import setup,find_packages
from typing import List

def get_req()->List[str]:
    '''
    this fucntional install all package
   '''
    requerment_lst:List[str]=[]
    try:
        with open('requirements.txt','r') as file:
            lines = file.readlines()
            for line in lines:
                requerment=line.strip()
                if requerment and requerment!='-e .':
                    requerment_lst.append(requerment)
    except FileNotFoundError:
        print("file not found")
    return requerment_lst
print(get_req())



setup(
    name="harshil",
    author="harshiluamryai",
    packages= find_packages(),
    install_requires=get_req()

)

