import os
from src.constants import *
from src.utils.common import read_yaml, create_directories
from src.entity.config_entity import DataIngestionConfig, PrepareBaseModelConfig, ModelTrainingConfig, EvaluationConfig
from pathlib import Path


class ConfigurationManager:
    def __init__(self, 
                 config_file_path = CONFIG_FILE_PATH,
                 params_file_path = PARAMS_FILE_PATH):
        self.config = read_yaml(config_file_path)
        self.params = read_yaml(params_file_path)

        create_directories([self.config.artifacts_root])

    def get_data_ingestion_config(self) -> DataIngestionConfig:
        config = self.config.data_ingestion

        create_directories([config.root_dir])

        data_ingestion_config = DataIngestionConfig(
            root_dir=config.root_dir,
            source_URL=config.source_URL,
            local_data_file=config.local_data_file,
            unzip_dir=config.unzip_dir
        )

        return data_ingestion_config

    
    def get_prepare_base_model_config(self) -> PrepareBaseModelConfig:
        config = self.config.prepare_base_model

        create_directories([config.root_dir])

        prepare_base_model_config = PrepareBaseModelConfig(
            root_dir=Path(config.root_dir),
            base_model_path=Path(config.base_model_path),
            updated_base_model_path=Path(config.updated_base_model_path),
            params_batch_size=self.params.BATCH_SIZE,
            params_image_size=self.params.IMAGE_SIZE,
            params_include_top=self.params.INCLUDE_TOP,
            params_weights=self.params.WEIGHTS,
            params_learning_rate=self.params.LEARNING_RATE,
            params_classes=self.params.CLASSES,
            params_epochs=self.params.EPOCHS
        )

        return prepare_base_model_config
    

    def get_training_config(self) -> ModelTrainingConfig:
        training = self.config.model_training
        prepare_base_model = self.config.prepare_base_model
        params = self.params
        training_data = os.path.join(self.config.data_ingestion.unzip_dir, "Chicken-fecal-images")

        create_directories([
            Path(training.root_dir)
        ])

        training_config = ModelTrainingConfig(
            root_dir=Path(training.root_dir),
            trained_model_path=Path(training.trained_model_path),
            updated_base_model_path=Path(prepare_base_model.updated_base_model_path),
            training_data=Path(training_data),
            params_epochs=params.EPOCHS,
            params_batch_size=params.BATCH_SIZE,
            params_is_augmentation=params.IS_AUGMENTATION,
            params_image_size=params.IMAGE_SIZE
        )

        return training_config
    

    def get_validation_config(self) -> EvaluationConfig:

        config = self.config.model_evaluation
        create_directories([config.root_dir])

        eval_config = EvaluationConfig(
            root_dir=self.config.model_evaluation.root_dir,
            path_of_model=self.config.model_training.trained_model_path,
            training_data=os.path.join(self.config.data_ingestion.unzip_dir, "Chicken-fecal-images"),
            evaluation_score_path=Path(self.config.model_evaluation.evaluation_score_path),
            params_image_size=self.params.IMAGE_SIZE,
            params_batch_size=self.params.BATCH_SIZE,
            all_params=self.params
        )
        return eval_config