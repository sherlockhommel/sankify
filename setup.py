from setuptools import setup, find_packages

setup(
    name="sankify",
    version="0.0.1",
    description='',
    author="Fabian Hommel",
    author_email="",
    packages=find_packages(),
    include_package_data=True,
    python_requires="==3.8.*",
    install_requires=["pandas", "streamlit", "loguru", "more-itertools", "plotly"]
)