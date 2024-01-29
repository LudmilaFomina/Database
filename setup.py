from setuptools import find_packages, setup

def parse_requirements():
    with open('requirements.txt') as req:
        return [x.strip() for x in req.readlines()
                if not x.startswith('-e') and
                not x.startswith('git+') and
                not x.startswith('https://')]

setup(
    name="database",
    version="0.0.2",
    url="https://github.com/LudmilaFomina/Database",
    author="Liudmila Fomina",
    description="Database. Name - Date of birth matching",
    install_requires=parse_requirements(),
    )