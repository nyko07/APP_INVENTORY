import setuptools

with open("../../API/README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="API",
    version="0.0.1",
    author="AlvarutoyNicolas",
    author_email="alvaruto@gmail.com",
    description="API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Alvaruto1",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)