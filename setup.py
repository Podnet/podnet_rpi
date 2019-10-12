import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="podnet_rpi",
    version="0.1.0",
    author="Apoorva Singh",
    author_email="apoorvasingh157@gmail.com",
    description="Client library for Raspberry Pi's for communicating with Podnet.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Podnet/podnet_rpi",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3.6",
        "License :: OSI Approved :: MIT License",
        "Operating System :: POSIX :: Linux",
        "Development Status :: 4 - Beta"
    ],
    python_requires='>=3.6',
)