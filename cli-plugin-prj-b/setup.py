from setuptools import setup

setup(
    name="mycli-prj-b",
    packages=["mycli_prj_b"],
    entry_points={"mycli": ["mycli_prj_b.create = mycli_prj_b:create"]}
)
