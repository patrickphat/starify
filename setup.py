import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

# Setup tools
setuptools.setup(
     name='starify',
     version='0.0.1b1',
     author="Truong-Phat Nguyen",
     author_email="me@patrickphat.com",
     description="Starify: convert string to asterisks for confidentiality display",
     long_description=long_description,
     long_description_content_type="text/markdown",
     url="https://github.com/patrickphat/starify",
     packages=setuptools.find_packages(exclude=['docs', 'tests', 'experiments']),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
     python_requires='>3.6',
     install_requires =[],
     extras_require={
         'dev': [
             'pytest',
             'coverage',
             ],
     }
 )
