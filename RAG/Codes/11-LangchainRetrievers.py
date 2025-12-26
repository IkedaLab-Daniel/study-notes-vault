""" Setup """
# > Ignore Warning
def warn(*args, **kwargs):
    pass
import warnings
warnings.warn = warn
warnings.filterwarnings('ignore')

# > Load ENV file
from dotenv import load_dotenv
import os

load_dotenv()

