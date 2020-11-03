import setuptools
from pathlib import Path
setuptools.setup(
    name="tsetmc_state",
    author="Mehrdad Seyfi houjaghan",
    version="1.2.2",
    long_description=Path("README.md").read_text(),
    long_description_content_type='text/markdown',
    description="A small web crawler for tsetmc.com",
    packages=setuptools.find_packages(exclude=["tests","data"]),
    project_urls={
        'Source': 'https://github.com/mrseyfi/tsetmc_state',
    },
    install_requires=[
          'requests',
      ]
)
