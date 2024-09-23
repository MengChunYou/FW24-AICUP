"""
main script
"""
import os
from argparse import ArgumentParser
import pandas as pd
import gdown

from .utils.utils import (
    load_data,
    load_yaml,
    date_time_transfer
)
from .utils.model_utils import (
    split,
    feature_selection,
    metrics
)
from .model.gb_trainer import (
    XGBTrainer,
    LGBMTrainer,
    CatTrainer
)
from .model.stack_trainer import StackTrainer


def parsing_args() -> ArgumentParser:
    """
    parse arguments
    """
    parser = ArgumentParser()
    parser.add_argument(
        "--folder_path", "-fp", type=str,
        default="data/train_data"
    )
    parser.add_argument(
        "--is_valid", "-iv", action="store_true", default=False
    )
    parser.add_argument(
        "--model_type", "-mt", type=str, default="xgb"
    )
    return parser.parse_args()


if __name__ == "__main__":
    if not os.path.exists('data/train_data'):
        DRIVE_URL = "https://drive.google.com/drive/folders/1EwByrnWjyS5ruG3FxWRjEDoi0dsrqKUA?usp=sharing"
        gdown.download_folder(DRIVE_URL, 'data/train_data', quiet=False)

    args = parsing_args()
    xgb_config = load_yaml("config/xgb.yml")
    data = load_data(args.folder_path).sort_values("LocationCode", ascending=True).iloc[:10000, :]
    data['DateTime'] = date_time_transfer(data['DateTime'])
    x_train, y_train, x_test, y_test = split(data, "Power(mW)", 0.2)

    if args.is_valid:
        x_train, y_train, x_valid, y_valid = split(
            pd.concat([x_train, y_train], axis=1),
            "Power(mW)",
            0.2
        )

    feature_importances = feature_selection(data, "Power(mW)").sort_values("Importance", ascending=False)
    print(feature_importances)

    model_map = {
        "xgb": XGBTrainer,
        "lgbm": LGBMTrainer,
        "cat": CatTrainer,
        "stack": StackTrainer
    }
    trainer = model_map[args.model_type](model=args.model_type, params=xgb_config)
    trainer.fit(x_train, y_train)
    y_pred = trainer.predict(x_test)
    metrics(y_test, y_pred)
