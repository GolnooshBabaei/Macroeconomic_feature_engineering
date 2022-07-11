import pandas as pd
from Macroeconomy import expand_dataset

if __name__ == "__main__":
    pd.set_option("display.max_columns", 10000)


ex_class = expand_dataset()

expanded_datasett = ex_class.add_macro_variables_to_dataset(ex_class.create_original_dataset(), ex_class.find_lagged_variables(ex_class.download_estimatedpercentofpeople_in_poverty(), settings=["year", "addr_state"]), on_cols=["year", "addr_state"])
print(expanded_datasett)
print(expanded_datasett.isna().sum())
print(expanded_datasett.shape)

