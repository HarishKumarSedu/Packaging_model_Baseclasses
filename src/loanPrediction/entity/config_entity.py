from src.loanPrediction.constants import *
from pathlib import Path 
from dataclasses import dataclass

@dataclass(frozen=True)
class DataingestionTemplate:
    root_dir : Path 
    test_data_url: Path 
    train_data_url: Path 
    test_unzip_dir: Path 
    train_unzip_dir: Path 
    local_data_path : Path 