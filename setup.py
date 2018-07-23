from setuptools import setup, find_packages
from os.path import join, dirname

import project

setup(
    name='task-manager',
    version=project.__version__,
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.rst')).read(),

    # install_requires=[
    #     'PyDrive',
    # ],
    entry_points={
        'console_scripts': [
            'tdcre = project.main:task_dir_create',
        ]
    },
    # include_package_data=True,
    # test_suite='tests',
)
