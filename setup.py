from setuptools import setup
from setuptools import find_packages
from setuptools.command.install import install


class InstallWrapper(install):
    """Install punkt."""

    def run(self):
        # Run this first so the install stops in case
        # these fail otherwise the Python package is
        # successfully installed
        self._post_install()
        # Run the standard PyPi copy
        install.run(self)

    def _post_install(self):
        """Post-installation for installation mode."""
        print("Downloading punkt")
        import nltk
        nltk.download('punkt')
        print("Download succeeded")


with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="readability-metrics",
    version="1.0.0",
    author="Eric Wiener",
    author_email="ericwiener3@gmail.com",
    description="Calculates multiple readability metrics for large documents.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/EricWiener/readability-metrics",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ],
    install_requires=[
        'nltk',
    ],
    packages=["metrics"],
    cmdclass={
        'install': InstallWrapper
    },
)
