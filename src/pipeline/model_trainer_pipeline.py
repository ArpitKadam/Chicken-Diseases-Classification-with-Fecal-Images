from src.components.model_trainer import Training
from src.config.configuration import ConfigurationManager
from src.logger.logger import logger

STAGE_NAME = "MODEL TRAINING STAGE"

class ModelTrainingPipeline:
    def __init__(self):
        pass

    def main(self):
        config = ConfigurationManager()
        training_config = config.get_training_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()