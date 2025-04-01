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
    maintainer='nathan',
    maintainer_email='raamanathan2002@gmail.com',
    description='AMG8833 thermal sensor ROS 2 publisher',
    license='Apache-2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'amg8833_publisher = amg8833_sensor.amg8833_publisher:main'
        ],
    },
    data_files=[
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'scripts'), glob('scripts/*.py'))
    ],
)
