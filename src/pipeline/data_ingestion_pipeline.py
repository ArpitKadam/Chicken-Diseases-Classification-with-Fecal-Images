from src.config.configuration import ConfigurationManager
from src.components.data_ingestion import DataIngestion
from src.logger.logger import logger

STAGE_NAME = "DATA_INGESTION_STAGE"

class  DataIngestionPipeline:
    def __init__(self):
        pass
    
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.extract_zip_file()