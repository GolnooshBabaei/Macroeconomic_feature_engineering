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
data = ex_class.create_original_dataset()
melted = ex_class.find_lagged_variables(ex_class.download_house_price_index(), settings=["date", "addr_state"])
    #melted_snap = ex_class.find_lagged_variables(ex_class.download_house_price_index(), settings=["date", "addr_state"])
#"date", "addr_state"
#expanded_datasett = ex_class.add_macro_variables_to_dataset(ex_class.create_original_dataset(), ex_class.find_lagged_variables(ex_class.download_estimatedpercentofpeople_in_poverty(), settings=["year", "addr_state"]), on_cols=["year", "addr_state"])
print(melted)
print(melted.isna().sum())
print(melted.shape)
print(melted["date"])



#enemployment rate: yes
#cpi: yes
#annual income: yes
#homeownership rate: yes
#resident pop: yes
#snap: yes
#house price index: no
#estimated people in poverty:
