from setuptools import setup
import os
from glob import glob

package_name = 'amg8833_sensor'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='ubuntu',
    maintainer_email='your@email.com',
    description='AMG8833 ROS 2 Publisher',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'amg8833_publisher = amg8833_sensor.amg8833_publisher:main'
        ],
    },
)

