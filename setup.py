import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="anjie", # Replace with your own username
    version="1.0.0",
    author="Babatunde Adewole",
    author_email="adewole63@gmail.com",
    description="This python library provides corpus in English and various local african languages e.g(Youruba, Hausa, Pidgin), it also does sentiment analysis on brands",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Free-tek/Anjie_local_language_corpus_generator",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
