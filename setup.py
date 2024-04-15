from setuptools import setup, find_packages,setup

setup(
    name='mcqgenerator',
    version='0.1',
    author='Adarsh Maurya',
    author_email="adarsh@onionreads.com",
    packages=find_packages(),
    install_requires=[
        "openai","langchain", "streamlit", "python-dotenv", "PyPDF2", "huggingface_hub","transformers","bitsandbytes","accelerate" ]
)