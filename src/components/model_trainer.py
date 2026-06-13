import os
import sys
from dataclasses import dataclass

from catboost import CatBoostRegressor
from sklearn.ensemble import (
    AdaBoostRegressor,
    GradientBoostingRegressor,
    RandomForestRegressor
)
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.tree import DecisionTreeRegressor
from xgboost import XGBRegressor

from src.exception import CustomException
from src.logger import logging
from src.utils import save_object, evaluate_model


@dataclass
class MTCON:
    trained_model_f_p = os.path.join("artifacts", "model.pkl")


class MDT:
    def __init__(self):
        self.model_trainer_config = MTCON()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info("Splitting training and test input data")

            X_train = train_array[:, :-1]
            y_train = train_array[:, -1]

            X_test = test_array[:, :-1]
            y_test = test_array[:, -1]

            models = {
                "Linear Regression": LinearRegression(),
                "Decision Tree": DecisionTreeRegressor(),
                "Random Forest": RandomForestRegressor(),
                "Gradient Boosting": GradientBoostingRegressor(),
                "K-Nearest Neighbors": KNeighborsRegressor(),
                "XGBoost": XGBRegressor(),
                "CatBoost": CatBoostRegressor(verbose=0),
                "AdaBoost": AdaBoostRegressor()
            }

            logging.info("Model training started")

            model_report = evaluate_model(
                X_train=X_train,
                y_train=y_train,
                X_test=X_test,
                y_test=y_test,
                models=models
            )

            best_model_score = max(model_report.values())

            best_model_name = max(
                model_report,
                key=model_report.get
            )

            best_model = models[best_model_name]

            logging.info(
                f"Best model found: {best_model_name} "
                f"with score {best_model_score}"
            )

            if best_model_score < 0.6:
                raise CustomException(
                    "No suitable model found with score greater than 0.6",
                    sys
                )

            save_object(
                file_path=self.model_trainer_config.trained_model_f_p,
                obj=best_model
            )

            predicted = best_model.predict(X_test)

            r2_square = r2_score(y_test, predicted)

            logging.info(
                f"Final R2 Score of best model: {r2_square}"
            )

            return r2_square

        except Exception as e:
            raise CustomException(e, sys)