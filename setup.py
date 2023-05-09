import setuptools

#storing info from the readme file to the long description variable, so it is 
#visible in pypi
with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name="rv_curve_jura",
    version="0.1",
    author="Will Ceva",
    author_email='william.ceva@unige.ch',
    description="Does a very basic RV curve calculation and plots it",
    packages=setuptools.find_packages(),
    long_description=long_description,
    install_requires = ["numpy>=1.5","matplotlib"],
    classifiers=["Programming Language :: Python :: 3",
                 "Operating System :: OS Independent",
                 ],
)
