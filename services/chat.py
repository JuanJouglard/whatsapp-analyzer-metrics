from abc import ABC, abstractmethod
from pandas import DataFrame

from models.metric import Metric
from typing import List


class MetricsService(ABC):

    @abstractmethod
    def get_chat_metrics(self) -> List[Metric]:
        pass


class PandasMetricsSerivce(MetricsService):

    def __init__(self, df: DataFrame):
        self.df = df


    def get_chat_metrics(self) -> List[Metric]:
        return [
                {
                    "chart_type": "line",
                    "key": "messages_per_person",
                    "title": "Messages per person",
                    "data": get_messages_per_person(self.df)
                    }
                ]

def get_messages_per_person(df: DataFrame):
    return df.groupby(by="user").count().set_index(["user"])
