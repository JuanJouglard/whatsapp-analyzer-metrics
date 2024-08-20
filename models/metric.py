from dataclasses import dataclass
from typing import Dict, Literal, List

@dataclass
class Metric:
    chart_type: Literal["bar", "line", "pie"]
    data: List[Dict[str, int]]
    key: str
    title: str

