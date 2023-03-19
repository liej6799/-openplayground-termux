import setuptools
from pathlib import Path

base_path = Path(__file__).parent
long_description = (base_path / "README.md").read_text()

setuptools.setup(
  name="openplayground-cli",
  version="0.0.1",
  author="ading2210",
  description=" CLI app for OpenPlayground utilizing openplayground-api (nat.dev)",
  long_description=long_description,
  long_description_content_type="text/markdown",
  packages=setuptools.find_packages(),
  classifiers=[
    "Programming Language :: Python :: 3",
    "License :: OSI Approved :: GNU General Public License (GPL)",
    "Operating System :: OS Independent"
  ],
  python_requires=">=3.6",
  py_modules=["openplayground-cli"],
  package_dir={"": "openplayground-cli/src"},
  install_requires=["rich-click", "openplayground-api"],
  url="https://github.com/liej6799/openplayground-cli"
)