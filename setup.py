
from setuptools import setup, find_packages

setup(
    name = "nonebot-plugin-read_60s",
    version = "0.2.4",
    description = "Send news pictures to friends or group chat",
    license = "MIT Licence",

    url = "https://github.com/bingganhe123/60s-",
    author = "bingganhe",
    author_email = "3143799170@qq.com",

    packages = find_packages(),
    include_package_data = True,
    python_requires='>=3.9, <4',
    zip_safe = False,
    install_requires = [
        'nonebot-plugin-apscheduler>=0.1.2',
        'nonebot2>=2.0.0.a16',
        'requests>=2.27.1']
)
