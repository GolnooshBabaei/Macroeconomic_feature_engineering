from includedall import macro_data

if __name__ == "__main__":
    my_eco_class = macro_data()
    x = my_eco_class.download_house_price_index()
    #x_df = my_eco_class.create_dataframe(x)
    #transposed_x = my_eco_class.prepare_dataframe()

    print(x)
    #print(transposed_x)

