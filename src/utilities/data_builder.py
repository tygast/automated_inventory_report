# -*- coding: utf-8 -*-
# %%
import numpy as np
import pandas as pd


# %%
TODAY = pd.Timestamp.today()
TYPE_A = [
    " A #",
    " A#",
    " B #",
    " B#",
    " C #",
    " C#",
    " D #",
    " D#",
    " E #",
    " E#",
    " F #",
    " F#",
    " G #",
    " G#",
    " H #",
    " H#",
    " I #",
    " I#",
    " J #",
    " J#",
    " K #",
    " K#",
    " L #",
    " L#",
    " M #",
    " M#",
    " N #",
    " N#",
    " O #",
    " O#",
    " P #",
    " P#",
    " Q #",
    " Q#",
    " R #",
    " R#",
    " S #",
    " S#",
    " T #",
    " T#",
    " U #",
    " U#",
    " V #",
    " V#",
    " W #",
    " W#",
    " X #",
    " X#",
    " Y #",
    " Y#",
    " Z #",
    " Z#",
]
EAST = [
    "LOCATION A",
    "LOCATION B",
    "LOCATION G",
    "LOCATION H",
]
WEST = [
    "LOCATION C",
    "LOCATION D",
    "LOCATION E",
    "LOCATION F",
]

# %%
def configure_df(
    df: pd.DataFrame,
    columns: list[str],
    combine: list[str],
    property_type: str,
    sort_by: str,
    date: str,
) -> pd.DataFrame:
    df["abnormal"] = None
    df["years_in_service"] = None
    df["parent_location"] = None
    df[combine[0]] = df[combine[0]].astype(str)
    df[combine[1]] = df[combine[1]].astype(str)
    df["size"] = df[combine[0]] + " x " + df[combine[1]]
    df["total_product"] = df.avg_oil + df.avg_water
    df["forecast_product"] = df.oil_forecast + df.water_forecast
    for idx, row in df.iterrows():
        df.at[idx, "parent_location"] = "WEST" if row["team_name"] in WEST else "EAST"
        df.at[idx, "abnormal"] = (
            "NO"
            if "STEEL" in row[property_type] or "ALUMINIUM" in row[property_type]
            else "YES"
            if any(letter in row[property_type] for letter in TYPE_A)
            else "NO"
        )
        df.at[idx, "years_in_service"] = (
            round((TODAY - row[date]) / np.timedelta64(1, "Y"), 1)
            if row[date] != None
            else None
        )
        for col in columns:
            if row.get(col, None) < 0:
                df.at[idx, col] = 0.0000
    df[date] = [np.datetime_as_string(val, unit="D") for val in df[date].values]
    df = df.sort_values(by=sort_by, ascending=True)
    df = df.drop_duplicates(subset=["location_name"])
    return df


# %%
def create_type_df(df: pd.DataFrame, alloc: str) -> pd.DataFrame:
    east_locations = list(location_formatter(df=df, direction="EAST").keys())
    west_locations = list(location_formatter(df=df, direction="WEST").keys())
    all_locations = east_locations + west_locations
    type_df = df[df["property_name"].isin(all_locations)]
    type_df = type_df[type_df["composition"] != "IRON"]
    type_df = type_df[type_df["total_product"] < 250]
    type_df = type_df[type_df["abnormal"] == alloc]
    type_df = type_df.sort_values(
        by=["property_name", "total_product", "forecast_product", "location_name"],
        ascending=True,
    )
    return type_df


# %%
def location_formatter(df: pd.DataFrame, direction: str,) -> dict:

    direction_df = df[df["parent_location"] == direction]
    product_df = direction_df[direction_df["forecast_product"] < 250]
    warehouses = list(product_df.property_name.value_counts()[:10].index)
    location_dict = {}
    for location in warehouses:
        location_dict[location] = {
            "A": len(
                product_df[
                    (product_df["property_name"] == location)
                    & (product_df["composition"] == "IRON")
                ]
            ),
            "B": len(
                product_df[
                    (product_df["property_name"] == location)
                    & (product_df["composition"] == "STONE")
                ]
            ),
        }
    return location_dict


# %%
def type_formatter(type: pd.DataFrame) -> list[dict]:
    type_formatter = [
        {"header": "Location", "values": list(type.location_name.values)},
        {"header": "Warehouse", "values": list(type.property_name.values)},
        {"header": "Abnormal", "values": list(type.abnormal.values)},
        {"header": "Manufacturer", "values": list(type.manufacturer.values)},
        {"header": "Composition", "values": list(type.composition.values)},
        {"header": "Size", "values": list(type["size"].values)},
        {"header": "Asset ID", "values": list(type.barcode_id.values)},
        {"header": "Asset SN", "values": list(type.serial_nb.values)},
        {
            "header": "Total Procuct",
            "values": [format(val, ".2f") for val in type["total_product"].values],
        },
        {
            "header": "Forecast Procuct",
            "values": [format(val, ".2f") for val in type["forecast_product"].values],
        },
        {"header": "Manufacture Date", "values": list(type.start_dt.values)},
        {"header": "Years in Service", "values": list(type.years_in_service.values)},
    ]
    return type_formatter


# %%
