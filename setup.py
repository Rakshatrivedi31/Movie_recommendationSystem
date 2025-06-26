from setuptools import setup, find_packages

# Define constants
SRC_REPO = 'src'  # Replace with actual source folder if different
AUTHOR_NAME = 'Raksha Trivedi'
LIST_OF_REQUIREMENTS =['streamlit']

# Read long description from README.md (optional)
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name=SRC_REPO,
    version='0.0.1',
    author=AUTHOR_NAME,
    author_email='rakshatrivedi00@gmail.com',
    description='A small example package for movie recommendation',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=find_packages(),
    install_requires= LIST_OF_REQUIREMENTS,
    python_requires='>=3.7',
)
