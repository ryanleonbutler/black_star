from setuptools import find_packages, setup

setup(
    name="black_star",
    version="1.0.0",
    description="Black Star - Fantasy RPG",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
)
