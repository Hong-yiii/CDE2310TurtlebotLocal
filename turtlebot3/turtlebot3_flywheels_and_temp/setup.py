from setuptools import setup
import os
from glob import glob

package_name = 'turtlebot3_flywheels_and_temp'

setup(
    name=package_name,
    version='0.0.0',
    packages=[package_name],
    data_files=[
        ('share/ament_index/resource_index/packages', ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.py')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='you@example.com',
    description='Bringup for AMG8833 and flywheels',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'amg8833_publisher = turtlebot3_flywheels_and_temp.amg8833_publisher:main',
        ],
    },
)