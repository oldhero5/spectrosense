from setuptools import setup, find_packages

setup(
    name="spectrosense",
    version="0.2.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
        "anthropic",
        "pillow"
    ],
    author="Marty H",
    author_email="bisonadapt@proton.me",
    description="AI-powered RF signal analysis and classification",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/oldhero5/spectrosense",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)