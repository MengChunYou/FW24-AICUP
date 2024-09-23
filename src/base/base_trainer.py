from typing import Any, Dict
import pandas as pd


class BaseTrainer:
    """
    Base class for all trainers
    """
    def __init__(self, model: str, params: Dict[str, Any] | None = None) -> None:
        self.model = model
        self.params = params

    def fit(self, x_train: pd.DataFrame, y_train: pd.Series) -> None:
        """
        Fit the model
        """
        self.model.fit(x_train, y_train)

    def predict(self, x_test: pd.DataFrame) -> pd.Series:
        """
        Make predictions
        """
        return self.model.predict(x_test)
