from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

# ✅ Project Configuration
REPO_NAME = "Movie_Recommendation_System"
AUTHOR_USER_NAME = "Rakshatrivedi31"
SRC_REPO = "src"
AUTHOR_EMAIL = "rakshatrivedi31@example.com"
LIST_OF_REQUIREMENTS = ["streamlit", "pandas", "numpy", "scikit-learn", "requests"]

setup(
    name=SRC_REPO,
    version="0.0.1",
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A Streamlit-based Movie Recommendation System using Machine Learning.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/Rakshatrivedi31/Movie_Recommendation_System",  # 🔗 Fully filled
    packages=[SRC_REPO],
    license="MIT",
    python_requires=">=3.7",
    install_requires=LIST_OF_REQUIREMENTS
)
