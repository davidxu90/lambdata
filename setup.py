import setuptools

REQUIRED = [
    "numpy",
    "pandas"
]

with open("README.md", "r") as fh:
    LONG_DESCRIPTION = fh.read()

setuptools.setup(
    name="lambdata",
    version="0.0.1",
    description="A Python package",
    long_description=LONG_DESCRIPTION,
    long_description_content="text/markdown",
    url="https://github.com/davidxu90/lambdata",
    packages=setuptools.find_packages(),
    python_requires=">=3.6",
    install_requires=REQUIRED,
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
