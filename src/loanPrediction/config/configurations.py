from src import logger 
from src.loanPrediction.utils.common import read_yaml, create_directories
from src.loanPrediction.constants import *
from src.loanPrediction.entity.config_entity import DataingestionTemplate

class ConfigurationManager:

    def __init__(self,
                 config_file = CONFIG_YAML_FILE_PATH) :
        self.config = read_yaml(config_file)

        create_directories([self.config.artifacts_root])
    
    def data_ingestion_configuration(self)->DataingestionTemplate:
        config = self.config.data_ingestion 
        create_directories([config.root_dir])
        data_ingestion = DataingestionTemplate(
                root_dir  = config.root_dir, 
                test_data_url = config.test_data_url,
                train_data_url = config.train_data_url,
                test_unzip_dir = config.test_unzip_dir,
                train_unzip_dir = config.train_unzip_dir,
                local_data_path  = config.local_data_path, 
        )

        return data_ingestion