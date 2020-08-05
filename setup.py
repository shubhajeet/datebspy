import setuptools

long_description = ""
with open("README.md","r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="datebs", # Replace with your own username
    version="0.0.5",
    author="Sujit Maharjan",
    author_email="shubhajeet.per@gmail.com",
    description="convert date from BS to AD and vice versa",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/shubhajeet/datebspy",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
