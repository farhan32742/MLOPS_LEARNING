import os 
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO)


list_of_files = [
".github/workflows/.gitkeep",
"src/__init__.py",
"src/components/__init__.py",
"src/components/data_ingestion.py",
"src/components/data_transformation.py",
"src/components/model_trainer.py",
"src/components/model_evalution.py",
"src/pipeline/__init__.py",
"src/pipeline/training_pipeline.py",
"src/pipeline/prediction_pipeline.py",
"src/utils/utils.py",
"src/utils/__init__.py",
"src/logger/logging.py",
"src/exception/exception.py",
"tests/unit/__init__.py",
"tests/integration/__init__.py",
"init_setup.sh",
"requirements.txt",
"requirements_dev.txt",
"setup.py",
"setup.config",
"pyproject.toml",
"tox.ini",
"experimen/experiments.ipynb"

]


for file_path in list_of_files:
    file_path = Path(file_path)
    file_dir,file_name = os.path.split(file_path)

    if file_dir != "":
        os.makedirs(file_dir,exist_ok=True)
        logging.info(f"Creating directory:{file_dir} for the file {file_name}")


    if (not os.path.exists(file_path)) or (os.path.getsize(file_path==0)):
        with open(file_path,"w") as f:
            pass
            logging.info(f"creating empty files")

    else:
        logging.info(f"{file_name} is already exists")