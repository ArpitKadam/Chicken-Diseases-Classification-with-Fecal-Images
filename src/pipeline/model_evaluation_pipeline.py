from src.config.configuration import ConfigurationManager
from src.logger.logger import logger
from src.components.model_evaluation import Evaluation

STAGE_NAME = "MODEL EVALUATION STAGE"

class ModelEvaluationPipeline:
    def __init__(self):   
        pass

    def main(self):
        config = ConfigurationManager()
        eval_config = config.get_validation_config()
        evaluation = Evaluation(eval_config)
        evaluation.evaluation()
        evaluation.save_score()