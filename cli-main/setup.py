from setuptools import setup

setup(
    name="mycli",
    packages=["mycli"],
    entry_points={"console_scripts": ["mycli = mycli:cli"]}
)
