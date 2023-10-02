# import os 
# from pathlib import Path    #to convert path to specified os format
# import logging  #we eant to log all the information during runtime as well

# logging.basicConfig(level=logging.INFO,format='[%(asctime)s]:%(message)s:')
# # Project Implementation start
# # we will be creating one folder called src inside src there is project name 
# #inside the project folder it will contain all components

# #.github-> use whenever we will be doing the ci/cd deployment
# #.gitkeep-without this if you commit  this code in your github,empty folder(workflows)
# #  wont be uploaded so you should have some files alter on we will delete it
# # __init__.py->constructor file->eg-we have created one folder textsummarizer and inside 
# # it i have created some component so i will write from text summarizer import so 
# # to do this thing i have to install this folder as my local package so and when installing
# # as local pakcage this constructor file is needed
# # components/init--ye waala init components ka constructor hai pichle waala textsummarizer 
# # ka tha or hm component ko b local package lenge

# project_name="textSummarizer"
# # //ye kch nhi file or folder banre hai
# list_of_files = [
#     ".github/workflows/.gitkeep",
#     f"src/{project_name}/__init__.py",
#     f"src/{project_name}/components/__init__.py",
#     f"src/{project_name}/utils/__init__.py",
#     f"src/{project_name}/utils/common.py",
#     f"src/{project_name}/logging/__init__.py",
#     f"src/{project_name}/config/__init__.py",
#     f"src/{project_name}/config/configuration.py",
#     f"src/{project_name}/pipeline/__init__.py",
#     f"src/{project_name}/entity/__init__.py",
#     f"src/{project_name}/constants/__init__.py",
#     "config/config.yaml",
#     "params.yaml",  #here i will keep my model related parameter    
#     "app.py",
#     "main.py",
#     "Dockerfile", #-- docker image of our source code
#     "requirements.txt",
#     "setup.py", #-help you to do local pakage
#     "reseach/trials.ipynb"  #-contain all the notebook experiment
# ]

# # logic for how above all file will be created
# for filepath in list_of_files:
#     filepath = Path(filepath) # converting filepath to specified operating system format
#     filedir,filename = os.path.split(filepath) #return two thing --splitting file and folder

#     if filedir != "":   #when there is no folder it will create one
#         os.makedirs(filedir, exist_ok=True)
#         logging.info(f"Creating directory:{filedir} for the file {filename}")   # setting up log

#         #size=0 isliye kahi same name file hui or usme code hua to ye replace krdega or hmara code chle jaayega 
#         #pr same name waali file kese hogi?? ya ye dusre folder ki baat krra h??
#         if(not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
#             with open(filepath,'w') as f:
#                 pass
#                 logging.info(f"Creating empty file: {filepath}")

#         else:
#             logging.info(f"{filename} is already exists")
            

import os
from pathlib import Path
import logging

logging.basicConfig(level=logging.INFO, format='[%(asctime)s]: %(message)s:')


project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/conponents/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]


for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory:{filedir} for the file {filename}")

    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath,'w') as f:
            pass
            logging.info(f"Creating empty file: {filepath}")


    
    else:
        logging.info(f"{filename} is already exists")