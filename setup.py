from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / "README.md").read_text(encoding="utf-8")


setup(
   
    name="HW2345",  
    version="1.0.0",  
    description="HW2345 translates a Lua codebase into a Python codebase.",  
    long_description=long_description, 
    long_description_content_type="text/markdown",  
    url="https://github.com/Aoishi28/CSC510_Group8_HW2",  
    author="1. Ameya Chavan 2. Amisha Waghela 3. Aoishi Das 4. Kunal Shah 5. Swarnamalya M",  
    author_email="author@example.com", 
    classifiers=[  
        "Development Status :: 5 - Production/Stable",
        
        "Intended Audience :: Computer Users",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.8",
        
        
    ],
   
    keywords="hw2345, setuptools",  
    package_dir={"": "src"}, 
    packages=find_packages(where="src"),
    python_requires=">=3.7, <4",
    install_requires=["attrs, colorama, iniconfig, packaging, pluggy, py, pyparsing, pytest, tomli"],  
    
)
