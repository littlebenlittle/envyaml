
import setuptools

setuptools.setup(
    name="envyaml-blittle",
    version="0",
    packages=setuptools.find_packages(),
    install_requires=[
        'pyyaml>=5.1.2',
    ],
    author="Ben Little",
    author_email="ben.little6@gmail.com",
    description="Use a simple yaml file to import environment variables.",
    python_requires='>=3.6',
)
