from src.logger.logger import logger
from src.pipeline.data_ingestion_pipeline import DataIngestionPipeline
from src.pipeline.prepare_base_model_pipeline import PrepareBaseModelTrainingPipeline
from src.pipeline.model_trainer_pipeline import ModelTrainingPipeline
from src.pipeline.model_evaluation_pipeline import ModelEvaluationPipeline

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

STAGE_NAME = "PREPARE_BASE_MODEL_STAGE"
try:
    logger.info("="*100)
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = PrepareBaseModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    logger.info("="*100)
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "MODEL_TRAINING_STAGE"
try:
    logger.info("="*100)
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    logger.info("="*100)
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "MODEL_EVALUATION_STAGE"
try:
    logger.info("="*100)
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = ModelEvaluationPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")
    logger.info("="*100)
except Exception as e:
    logger.exception(e)
    raise e