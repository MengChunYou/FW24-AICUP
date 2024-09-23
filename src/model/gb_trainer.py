from typing import Any, Dict
from xgboost import XGBRegressor
from lightgbm import LGBMRegressor
from catboost import CatBoostRegressor

from ..base.base_trainer import BaseTrainer


class XGBTrainer(BaseTrainer):
    """
    Gradient Boosting Trainer
    """
    def __init__(self, model: str, params: Dict[str, Any]) -> None:
        super(XGBTrainer, self).__init__(model, params)
        self.model = XGBRegressor(**params)


class LGBMTrainer(BaseTrainer):
    """
    Gradient Boosting Trainer
    """
    def __init__(self, model: str, params: Dict[str, Any]) -> None:
        super(LGBMTrainer, self).__init__(model, params)
        self.model = LGBMRegressor(**params)


class CatTrainer(BaseTrainer):
    """
    Gradient Boosting Trainer
    """
    def __init__(self, model: str, params: Dict[str, Any]) -> None:
        super(CatTrainer, self).__init__(model, params)
        self.model = CatBoostRegressor(**params)
