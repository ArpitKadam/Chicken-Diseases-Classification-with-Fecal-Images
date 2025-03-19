from src.logger.logger import logger
from src.pipeline.data_ingestion_pipeline import DataIngestionPipeline

STAGE_NAME = "DATA_INGESTION_STAGE"
try:
    logger.info("="*100)
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    logger.info("="*100)
except Exception as e:
    logger.exception(e)
    raise e