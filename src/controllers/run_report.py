# -*- coding: utf-8 -*-
# %%
import pandas as pd

from databases.connections import db_connect
from services import email_recips, email_utils
from sql.db_A import SQL
from templates.create_tables import create_type_table, create_location_table
from utilities.data_builder import (
    TODAY,
    configure_df,
    create_type_df,
    location_formatter,
    type_formatter,
)


# %%
def generate_report():
    Engine_A = db_connect.Engine_A()
    df = pd.read_sql(SQL, Engine_A)

    new_df = configure_df(
        df=df,
        columns=["metric_1", "metric_2", "metric_3"],
        combine=["diameter", "effectivelength"],
        property_type="area_name",
        sort_by=["metric_1", "oil_forecast", "area_name", "location_name"],
        date="start_dt",
    )

    type_A_df = create_type_df(df=new_df, alloc="YES")
    type_B_df = create_type_df(df=new_df, alloc="NO")

    type_A = create_type_table(df=type_A_df, formatter=type_formatter(type=type_A_df))
    type_B = create_type_table(df=type_B_df, formatter=type_formatter(type=type_B_df))

    east_locations = create_location_table(
        title="EAST - Locations A, B, G, & H",
        formatter=location_formatter(df=new_df, direction="EAST"),
    )
    west_locations = create_location_table(
        title="WEST - Locations C, D, E, & F",
        formatter=location_formatter(df=new_df, direction="WEST"),
    )

    construct_email = email_utils.EmailMsg(
        email_recips.get_recipiant_list("shift_supervisors"),
        f"Asset Inventory for Low Producing Areas - {TODAY.strftime('%B %d')}",
    )

    construct_email.convert_plots_to_attachment(
        f"Type A Assets under 400 UPD Total Product - {TODAY.strftime('%m-%d-%Y')}.pdf",
        type_A,
    )
    construct_email.convert_plots_to_attachment(
        f"Type B Assets under 400 UPD Total Product - {TODAY.strftime('%m-%d-%Y')}.pdf",
        type_B,
    )

    construct_email.add_image(figure_id="west-locations", figure=west_locations)
    construct_email.add_image(figure_id="east-locations", figure=east_locations)

    construct_email.send()


# %%
if __name__ == "__main__":
    generate_report()
