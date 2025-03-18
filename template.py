import os 
from pathlib import Path
import logging

project_name = "Chicken_Diseases"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/__init__.py",
    f"src/components/__init__.py",
    f"src/utils/__init__.py",
    f"src/utils/common.py",
    f"src/config/__init__.py",
    f"src/config/configuration.py",
    f"src/pipeline/__init__.py",
    f"src/entity/__init__.py",
    f"src/entity/config.py",
    f"src/constants/__init__.py",
    f"src/logger/__init__.py",
    f"src/logger/logger.py",
    f"src/exception/__init__.py",
    f"src/exception/exception.py",
    "config/config.yaml",
    "params.yaml",
    "main.py",
    "app.py",
    "Dockerfile",
    "setup.py",
    "research/research.ipynb",
    "templates/index.html",
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory; {filedir} for the file: {filename}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File already exists: {filepath}")

logging.info("Project template created successfully!")
