from setuptools import setup, find_packages

setup(
    name="dab_python_pkg", 
    version="0.0.1",
    description="This contains the code in the ./src dir",
    packages=find_packages(where="./src"),
    package_dir={"": "./src"},
    install_requires=["setuptools"],
    entry_points={
        "cmd_group1":["run=dab_main.main:main"]
    },
    python_requires="==3.11.*"
)