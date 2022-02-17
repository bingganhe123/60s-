#!/usr/bin/env python
#-*- coding:utf-8 -*-

#############################################
# File Name: setup.py
# Author: mage
# Mail: mage@woodcol.com
# Created Time:  2018-1-23 19:17:34
#############################################


from setuptools import setup, find_packages

setup(
    name = "nonebot-plugin-read_60s",
    version = "0.1.9",
    keywords = ("pip", "pathtool","timetool", "magetool", "mage"),
    description = "time and path tool",
    long_description = "time and path tool",
    license = "MIT Licence",

    url = "https://github.com/fengmm521/pipProject",
    author = "mage",
    author_email = "mage@woodcol.com",

    packages = find_packages(),
    include_package_data = True,
    platforms = "any",
    zip_safe = False,
    install_requires = ['requests',
                        'Config',
                        'require',
                        'AsyncIOScheduler',
                        'json',
                        'nonebot',
                        'Message',
                        'BaseSettings',
                        'Extra',
                        'Field'
                        ]
)
