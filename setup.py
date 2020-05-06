import setuptools
 
with open("README.md", "r") as fh:
    long_description = fh.read()
 
setuptools.setup(
    #Here is the module name.
    name="Csv2Xml",
 
    #version of the module
    version="0.0.1",
 
    #Name of Author
    author="Suraj Kumar Dey",
 
    #your Email address
    author_email="surajdey8603@gmail.com",
 
    #Small Description about module
    description="Csv2Xml is a libary used to convert a CSV(comma-separated values) file to XML(extensible markup language).",
 
    
    py_modules=["Csv2Xml"],
    package_dir={'':'Csv2Xml'},
 
    #Specifying that we are using markdown file for description
    long_description=long_description,
    long_description_content_type="text/markdown",
 
    #Any link to reach this module, if you have any webpage or github profile
    url="https://github.com/suraj1709",
    packages=setuptools.find_packages(),
 
    #classifiers like program is suitable for python3, just leave as it is.
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
            
    install_requires=["Pandas"]
)