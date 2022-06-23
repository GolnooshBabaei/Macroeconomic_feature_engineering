import pandas as pd

from Macroeconomic_methods import macro_data, expand_dataset

if __name__ == "__main__":
    pd.set_option("display.max_columns", 10000)

    my_eco_class = macro_data()
    cpi = my_eco_class.download_cpi()
    #x_df = my_eco_class.create_dataframe(x)
    #transposed_x = my_eco_class.prepare_dataframe()
    #ex_class = expand_dataset()
    #x = ex_class.download_cpi()
    #data = ex_class.create_original_dataset()
    #melted = ex_class.find_lagged_variables(ex_class.download_annual_income())
    #melted_snap = ex_class.find_lagged_variables(ex_class.download_snap_benefits_recipients())

    #expanded_datasett = ex_class.add_macro_variables_to_dataset(data, melted_snap)
    #print(data)
    print(cpi)

