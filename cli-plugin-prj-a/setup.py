from setuptools import setup

setup(
    name="mycli-prj-a",
    packages=["mycli_prj_a"],
    entry_points={"mycli": ["mycli_prj_a.package = mycli_prj_a:package",
                            "mycli_prj_a.convert = mycli_prj_a:convert"]}
)
