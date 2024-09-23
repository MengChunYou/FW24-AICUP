from typing import Any, Dict

from ..base.base_trainer import BaseTrainer


class StackTrainer(BaseTrainer):
    def __init__(self, model: str, params: Dict[str, Any]) -> None:
        super(StackTrainer, self).__init__(model, params)
        self.models = []
        self.params = params