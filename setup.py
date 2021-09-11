import pathlib
from setuptools import setup

here = pathlib.Path(__file__).parent
readme = (here / "README.md").read_text()
setup(
    name="pygame-textinput",
    version="1.0.0",
    description="Enter text using pygame",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/Nearoo/pygame-text-input",
    author="Silas Gyger",
    author_email="silasgyger@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["pygame_textinput"],
    include_package_data=True,
    install_requires=["pygame"],
)