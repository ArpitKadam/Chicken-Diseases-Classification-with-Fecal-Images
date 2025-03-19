from src.config.configuration import ConfigurationManager
from src.components.prepare_base_model import PrepareBaseModel
from src.logger.logger import logger

STAGE_NAME = "PREPARE_BASE_MODEL_STAGE"


class PrepareBaseModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_prepare_base_model_config()
        prepare_base_model = PrepareBaseModel(prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.update_base_model()
