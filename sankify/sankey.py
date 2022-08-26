from typing import List

import pandas as pd
import plotly.graph_objects as go
from loguru import logger
from more_itertools import pairwise, flatten


def plot_sankey(df: pd.DataFrame, id_col: str, sankey_columns: List[str]) -> go.Figure:
    links = []
    for col_a, col_b in pairwise(sankey_columns):
        links += list(
            df
            .reset_index()
            .groupby([col_a, col_b])[id_col]
            .nunique()
            .reset_index()
            .itertuples(index=False, name=None)
        )

    labels = list(flatten([df[col].unique().tolist() for col in sankey_columns]))
    logger.debug(f"Links: {links}")
    logger.debug(f"Labels: {labels}")

    source, target, value = zip(*links)
    logger.debug("Mapping source and target values to indices...")
    source, target = [labels.index(s) for s in source], [labels.index(t) for t in target]
    logger.debug(f"Source {source}, target: {target}, value: {value}")

    data = go.Sankey(
        node={'label': labels},
        link={
            'source': source,
            'target': target,
            'value': value
        }
    )
    return go.Figure(data)
