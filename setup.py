from setuptools import find_packages, setup
from typing import List

def get_requirements(file_path: str) -> List[str]:
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.strip() for req in requirements]
        HYPEN_E_DOT = "-e ."
        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
    return requirements

setup(
    name="ML Project",
    version="0.0.1",
    author="ritesh",
    author_email="riteshlandage123@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements("requirements.txt")
)
