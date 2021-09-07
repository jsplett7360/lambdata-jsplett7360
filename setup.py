from setuptools import find_packages, setuptools
with open("README.md", "r") as fh:
    long_description = fh.read()

    setup(
        name="my-lambdata-pt4",
        version="1.0",
        author="Josh Splett",
        author_email="joshua.splett@gmail.com",
        description="For example purposes",
        long_description=long_description,
        long_description_content_type="text/markdown",

        url="https://github.com/s2t2/my-lambdata-pt4",

        packages=find_packages()
    )
