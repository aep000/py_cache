import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()
setuptools.setup(name='pycache',
      version='1.0',
      description="Extensible General Purpose caching package",
      long_description=long_description,
      long_description_content_type="text/markdown",
      url="https://github.com/aep000/py_cache",
      author="aep000",
      keywords = "caching flask redis cache",
      author_email="alexparson1@gmail.com",
      packages=['pycache'],
      )
