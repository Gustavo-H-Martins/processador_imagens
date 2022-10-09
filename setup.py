from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup(
    name="processamento_de_imagem",
    version="0.0.1",
    author="Gustavo H Lopes",
    author_email="gustavojoana10@gmail.com",
    description="Pacote de processamento de imagem usando Skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/",
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.8',
)

# python -m pip install --upgrade pip
# python -m pip install --user twine  
# python -m pip install --user setuptools

# python setup.py sdist bdist_wheel
