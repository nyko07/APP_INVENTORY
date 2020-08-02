import setuptools

with open("../../Notification/README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Notification",
    version="0.0.1",
    author="Alvaruto",
    author_email="alvaruto@gmail.com",
    description="Notification",
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