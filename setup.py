import setuptools

setuptools.setup(
    name="rv_curve_jura",
    version="0.1",
    author="Will Ceva",
    author_email='william.ceva@unige.ch',
    description="Does a very basic RV curve calculation and plots it",
    packages=setuptools.find_packages(),
    install_requires = ["numpy>=1.5","matplotlib"],
    classifiers=["Programming Language :: Python :: 3",
                 "Operating System :: OS Independent",
                 ],
)
