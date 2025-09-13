from setuptools import setup, find_packages
from typing import List

Hyp = '-e .'

def get_requires(file_path:str)->List[str]:
    requires = []
    with open(file_path) as f:
        requires = f.readlines()
        requires = [req.replace("\n","") for req in requires]
        if Hyp in requires:
            requires.remove(Hyp)
    return requires

setup(
    name='MLpackage',
    version='0.1.0',
    packages=find_packages(),
    install_requires=get_requires('requirements.txt'),
    author='Daipayan',
    author_email= 'senguptadaipayan@gmail.com'
)