from includedall import macro_data, expand_dataset

if __name__ == "__main__":
    my_eco_class = macro_data()
    #x = my_eco_class.download_house_price_index()
    #x_df = my_eco_class.create_dataframe(x)
    #transposed_x = my_eco_class.prepare_dataframe()
    ex_class = expand_dataset()
    #data = ex_class.create_original_dataset()
    melted = ex_class.find_lagged_variables(ex_class.download_unemployment_rate())


    print(melted)
    #print(transposed_x)

