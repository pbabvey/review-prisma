import os
import sqlite3

import altair as alt
import pandas as pd
from vega_datasets import data


def query_db(depth_min, grad_min):
    """Return well data given minimum depth and gradient."""
    conn = sqlite3.connect(os.path.join('data', 'wells.db'))

    query = f"""
    SELECT latitude, longitude, depth, gradient
    FROM wells
    WHERE depth > {depth_min} and gradient > {grad_min}
    """
    cursor = conn.cursor()

    return cursor.execute(query).fetchall()


def plot():
    """Return JSON of Altair chart."""

    df_cars = data.cars()
    df_cars['Year'] = df_cars["Year"].dt.year

    chart = alt.Chart(df_cars).mark_point().encode(x='Horsepower', y="Miles_per_Gallon", color="Origin",
        tooltip=['Name', 'Year', 'Origin']

    )


    return chart.to_json()
