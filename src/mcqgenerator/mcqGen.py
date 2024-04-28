import os
import traceback
import pandas as pd
from dotenv import load_dotenv

from src.mcqgenerator.utils import read_file,get_file_data
from src.mcqgenerator.logger import logging

# importing ncessary modules

from langchain import PromptTemplate, HuggingFaceHub
from langchain.chains import LLMChain
from langchain.chains import SequentialChain


# setting hf token
HF_API_TOKEN = os.environ.get("HF_API_TOKEN")
print(HF_API_TOKEN)

# setting up the chain

