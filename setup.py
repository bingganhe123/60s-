
from setuptools import setup, find_packages

setup(
    name = "nonebot-plugin-read_60s",
    version = "0.2.2",
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
    install_requires = [
        'nonebot-plugin-apscheduler>=0.1.2',
        'nonebot2>=2.0.0.a16',
        'requests>=2.27.1']
)