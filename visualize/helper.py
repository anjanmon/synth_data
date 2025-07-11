from dataclasses import dataclass

import numpy as np
import pandas as pd
import plotly.express as px



@dataclass
class DataViewer:
    """
    Only 1 Dimensional arrays supported for now"""
    x: [np.ndarray|pd.Series|list[int|float]]
    y: [np.ndarray |pd.Series|list[int|float]]

    def __post_init__(self):
    self.x = np.asarray(self.x)
    self.y = np.asarray(self.y)
    if self.x.ndim != 1 or self.y.ndim != 1:
        raise ValueError("x and y must be 1D")
    if len(self.x) != len(self.y):
        raise ValueError("x and y must be of equal length.")

    def plot(self, kind="bar", **kwargs):
    plot_funcs = {
        "bar": px.bar,
        "line": px.line,
        "scatter": px.scatter,
    }
    try:
        plot_func = plot_funcs[kind]
    except KeyError:
        raise ValueError(f"Unsupported plot kind: {kind}. Choose from {list(plot_funcs)}.")

    fig = plot_func(x=self.x, y=self.y, **kwargs)
    fig.show()