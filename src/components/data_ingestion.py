import os
import sys
import pandas as pd
from dataclasses import dataclass
from sklearn.model_selection import train_test_split

from src.exception import CustomException
from src.logger import logging
from src.components.data_trans import DataTransformation
from src.components.model_trainer import MDT
from src.components.model_trainer import MTCON

@dataclass
class DataIngestionConfig:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "raw.csv")


class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered Data Ingestion component")

        try:
            file_path = os.path.join("src", "eda", "StudentsPerformance.csv")
            df = pd.read_csv(file_path)

            logging.info("Dataset loaded successfully")

            # create artifacts folder
            os.makedirs(
                os.path.dirname(self.ingestion_config.train_data_path),
                exist_ok=True
            )

            # save raw data
            df.to_csv(self.ingestion_config.raw_data_path, index=False)
            logging.info("Raw data saved")

            # split data
            logging.info("Train-test split started")
            train_set, test_set = train_test_split(
                df,
                test_size=0.2,
                random_state=42
            )

            # save splits
            train_set.to_csv(self.ingestion_config.train_data_path, index=False)
            test_set.to_csv(self.ingestion_config.test_data_path, index=False)

            logging.info("Data ingestion completed")

            return (
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )

        except Exception as e:
            raise CustomException(e, sys)


if __name__ == "__main__":
    obj = DataIngestion()
    train_data, test_data = obj.initiate_data_ingestion()

    data_transformation = DataTransformation()

    # FIXED METHOD NAME
    train_arr, test_arr, _ = data_transformation.initiate_data_trans(
        train_data,
        test_data
    )
    modeltrainer=MDT()
    print(modeltrainer.initiate_model_trainer(train_arr,test_arr))