import pandas as pd

from Macroeconomy import expand_dataset

if __name__ == "__main__":
    pd.set_option("display.max_columns", 10000)

    #my_eco_class = macro_data()
    #cpi = my_eco_class.download_cpi()
    #x_df = my_eco_class.create_dataframe(x)
    #transposed_x = my_eco_class.prepare_dataframe()
    ex_class = expand_dataset()
    #x = ex_class.download_cpi()
    #data = ex_class.create_original_dataset()
    #melted = ex_class.find_lagged_variables_regionbased(ex_class.download_cpi())
    #melted_snap = ex_class.find_lagged_variables(ex_class.download_snap_benefits_recipients())
#"date", "addr_state"
    expanded_datasett = ex_class.add_macro_variables_to_dataset(ex_class.create_original_dataset(), ex_class.find_lagged_variables_statebased(ex_class.download_annual_income()), on_cols=["year", "addr_state"])
    #print(data)
    print(expanded_datasett)

