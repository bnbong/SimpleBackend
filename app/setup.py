from setuptools import setup, find_packages

setup(
    name="fastapi-simplebackend",
    description="Simple API server for test",
    author="bnbong",
    author_email="bbbong9@gmail.com",
    packages=find_packages(where="app"),
    use_scm_version=True,
)
