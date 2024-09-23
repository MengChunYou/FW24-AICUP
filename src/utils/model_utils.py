from typing import Tuple
from rich import print as rp
import pandas as pd
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score


def split(data: pd.DataFrame, label: str, test_size: float) -> Tuple:
    """
    split data into train, validation and test sets
    """
    train_x, test_x, train_y, test_y = train_test_split(
        data.drop(columns=label),
        data[label],
        test_size=test_size,
        random_state=42
    )

    return train_x, train_y, test_x, test_y

def feature_selection(data: pd.DataFrame, label: str) -> pd.DataFrame:
    """
    select features
    """
    data = shuffle(data)
    rf_regressor = RandomForestRegressor()
    rf_regressor.fit(data.drop(columns=label), data[label])
    feature_importances = pd.DataFrame(
        {
            "Feature": data.drop(columns=label).columns,
            "Importance": rf_regressor.feature_importances_
        }
    )
    return feature_importances

def metrics(y_true: pd.Series, y_pred: pd.Series) -> float:
    """
    calculate metrics
    """
    mse = mean_squared_error(y_true, y_pred)
    r_2 = r2_score(y_true, y_pred)
    rp(f"[bold green]Mean Squared Error: {mse}[/bold green] | [bold green]R2 Score: {r_2}[/bold green]")
