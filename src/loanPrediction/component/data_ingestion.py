from src import logger
import zipfile
import urllib.request as request 

class DataIngestion:

    def __init__(self, data_ingestion) -> None:
        self.data_ingestion_args = data_ingestion

    def get_data(self):
        filename, header = request.urlretrieve(
           url=self.data_ingestion_args.test_data_url,
           filename=self.data_ingestion_args.test_unzip_dir
            )
        logger.info(f' test data downloaded !....')
        if filename:
            self.extract_data(filename,self.data_ingestion_args.local_data_path)
        else:
            logger.info('! test data is not extractable ')
        filename, header = request.urlretrieve(
           url=self.data_ingestion_args.train_data_url,
           filename=self.data_ingestion_args.train_unzip_dir
            )
        logger.info(f' test data downloaded !....')
        if filename:
            self.extract_data(filename,self.data_ingestion_args.local_data_path)
        else:
            logger.info('! train data is not extractable ')

    def extract_data(self, file_path, extract_to):
        with zipfile.ZipFile(file_path, 'r') as zip_ref_file :
            zip_ref_file.extractall(extract_to)

