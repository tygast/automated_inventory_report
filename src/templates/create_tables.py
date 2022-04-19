# -*- coding: utf-8 -*-
# %%
import matplotlib.pyplot as plt
import pandas as pd


# %%
def create_type_table(df: pd.DataFrame, formatter: list[dict]) -> plt.Axes:
    row_count = int(len(df) / 2)
    headers = [col.get("header", None) for col in formatter]
    formatter_values_to_list = [val["values"] for val in formatter]

    rows = []
    for i in range(0, len(df)):
        sub_list = []
        for grp in formatter_values_to_list:
            sub_list.append(grp[i])
        rows.append(sub_list)

    fig, ax = plt.subplots()

    table = ax.table(
        cellText=rows,
        cellColours=[["#ffffff"] * 12, ["#d8dcd6"] * 12] * row_count
        if (len(df) % 2) == 0
        else ([["#ffffff"] * 12, ["#d8dcd6"] * 12] * row_count) + [["#ffffff"] * 12],
        cellLoc="center",
        colLabels=headers,
        colColours=["#789b73"] * len([col.get("header", None) for col in formatter]),
        colLoc="center",
        loc="top",
    )

    for c in table.get_children():
        c.set_edgecolor("none")
        if c._text.get_text() in headers:
            c.set_height(0.22)
            c.set_fontsize(16)
            c._text.set_fontweight("bold")
        else:
            c.set_height(0.16)
            c.set_fontsize(14)

    table.auto_set_font_size(False)
    table.auto_set_column_width(col=list(range(len(formatter))))

    plt.axis("off")
    plt.figure(tight_layout=True)

    return fig


# %%
def create_location_table(title: str, formatter: dict) -> plt.Axes:
    headers = ["Location", "Product A", "Product B"]

    fig, ax = plt.subplots()

    ax.set_title(label=title, fontsize=14, fontweight="bold", x=0.27, y=1.0)
    table = ax.table(
        cellText=[
            [prod, formatter[prod].get("A", None), formatter[prod].get("B", None)]
            for prod in list(formatter.keys())
        ],
        cellColours=[["#ffffff"] * 3, ["#d8dcd6"] * 3] * 5,
        cellLoc="center",
        colLabels=headers,
        colColours=["#789b73", "#789b73", "#789b73"],
        colLoc="center",
        loc="center",
    )

    for c in table.get_children():
        c.set_edgecolor("none")
        if (
            len(c._text.get_text()) > 4
            and c._text.get_text() != "Product A"
            and c._text.get_text() != "Product B"
        ):
            c._text.set_horizontalalignment("left")
        if c._text.get_text() in headers:
            c.set_height(0.10)
            c.set_fontsize(10)
            c._text.set_fontweight("bold")
        else:
            c.set_height(0.08)
            c.set_fontsize(8)

    table.auto_set_font_size(False)
    table.auto_set_column_width(col=list(range(len(formatter))))

    plt.axis("off")
    plt.figure(tight_layout=True)

    return fig
