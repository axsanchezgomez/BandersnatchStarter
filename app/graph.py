from altair import Chart
from pandas import DataFrame


def chart(df: DataFrame, x: str, y: str, target: str) -> Chart:
    graph = Chart(df).mark_circle().encode(
        x=x,
        y=y,
        color=target
    )
    return graph
