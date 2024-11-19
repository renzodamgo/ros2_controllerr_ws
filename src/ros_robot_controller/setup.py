from setuptools import setup
import os
from glob import glob

package_name = 'ros_robot_controller'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name, f'{package_name}.ros_robot_controller_sdk'],
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'),
         glob(os.path.join('launch', '*launch.[pxy][yma]*'))),
        (os.path.join('share', package_name, 'config'),
         glob(os.path.join('config', '*.yaml'))),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Your Name',
    maintainer_email='your@email.com',
    description='ROS 2 Robot Controller Package',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'controller_node = ros_robot_controller.controller_node:main',
        ],
    },
)
