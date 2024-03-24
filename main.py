from src import logger

from src.loanPrediction.config.configurations import ConfigurationManager
import urllib.request as request 
objconfig = ConfigurationManager()
data_ingestion_args = objconfig.data_ingestion_configuration()

filename, header = request.urlretrieve(
    url=data_ingestion_args.test_data_url,
    filename=data_ingestion_args.unzip_dir
)
print(header)