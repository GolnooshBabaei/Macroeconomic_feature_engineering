import pandas as pd
import tqdm
from fredapi import Fred
import numpy as np
import json
from dotenv import load_dotenv
import os

load_dotenv()

class macro_data:
    def __init__(self):
        self.states_abb_loaded = json.load(open("C:/Users/assegnista/state_abbreviations_version2.json", "r"))
        self.states_code_loaded = json.load(open("C:/Users/assegnista/state_codes.json", "r"))
        self.fred = Fred(api_key= os.getenv("FRED_KEY"))


    def download_cpi(self):
        """
        All items, all urban consumers,
        not seasonally adjusted
        Frequency: Monthly
        """
        s = ["CUUR0100SA0", "CUUR0400SA0", "CUUR0200SA0", "CUUR0300SA0"]  # NORTHEAST, WEST, MIDWEST, AND SOUTH
        regional_cpi = []
        for i in tqdm.tqdm(s):
            regional_cpi.append(self.fred.get_series(i))

        regional_cpi = pd.concat(regional_cpi, axis=1, ignore_index=True)
        regional_cpi.columns = ["NORTHEAST", "WEST", "MIDWEST","SOUTH"]
        regional_cpi["month"] = regional_cpi.index.month.astype(str)
        regional_cpi["year"] = regional_cpi.index.year.astype(str)
        regional_cpi["date"] = regional_cpi.year.str.cat(regional_cpi.month)
        return regional_cpi

    def download_unemployment_rate(self):
        """
        Ratio of the unemployed people on labor force
        Frequency: Monthly
        """
        ur_list = []
        for i in tqdm.tqdm(self.states_abb_loaded):
            tag = i + "UR"
            ur_list.append(self.fred.get_series(tag))

        ur_list = pd.concat(ur_list, axis=1, ignore_index=True)
        ur_list.columns = self.states_abb_loaded
        ur_list["month"] = ur_list.index.month.astype(str)
        ur_list["year"] = ur_list.index.year.astype(str)
        ur_list["date"] = ur_list.year.str.cat(ur_list.month)
        return ur_list

    def download_annual_income(self):
        """
        Statistics for each state (and the District of Columbia) show the combined personal incomes of the residents,
        including those whose work takes place beyond the state's borders. The data include income by industry and how
        much income comes from wages, proprietors' income, dividends, interest, rents, and government benefits.
        These statistics help assess and compare the economic well-being of state residents. Per capita personal income
        – an area's personal income divided by its population – can be used to compare incomes from one state to
        another or to the nation overall.

        Frequency: Annual
        """
        income_list = []
        for i in tqdm.tqdm(self.states_abb_loaded):
            tag = i + "PCPI"
            income_list.append(self.fred.get_series(tag))

        income_list = pd.concat(income_list, axis=1, ignore_index=True)
        income_list.columns = self.states_abb_loaded
        income_list["month"] = income_list.index.month.astype(str)
        income_list["year"] = income_list.index.year.astype(str)
        income_list["date"] = income_list.year.str.cat(income_list.month)
        return income_list

    def download_home_ownership_rate(self):
        """
        Unit: Percent
        Not Seasonally Adjusted
        Frequency: Annual
        """

        hown_list = []
        for i in tqdm.tqdm(self.states_abb_loaded):
            tag = i + "HOWN"
            hown_list.append(self.fred.get_series(tag))

        hown_list = pd.concat(hown_list, axis=1, ignore_index=True)
        hown_list.columns = self.states_abb_loaded
        hown_list["month"] = hown_list.index.month.astype(str)
        hown_list["year"] = hown_list.index.year.astype(str)
        hown_list["date"] = hown_list.year.str.cat(hown_list.month)
        return hown_list

    def download_resident_pop(self):
        """
        Unit: Thousands of persons
        Not Seasonally Adjusted
        Frequency: Annual
        """
        resident_pop_list = []
        for i in tqdm.tqdm(self.states_abb_loaded):
            tag = i + "POP"
            resident_pop_list.append(self.fred.get_series(tag))

        resident_pop_list = pd.concat(resident_pop_list, axis=1, ignore_index=True)
        resident_pop_list.columns = self.states_abb_loaded
        resident_pop_list["month"] = resident_pop_list.index.month.astype(str)
        resident_pop_list["year"] = resident_pop_list.index.year.astype(str)
        resident_pop_list["date"] = resident_pop_list.year.str.cat(resident_pop_list.month)
        return resident_pop_list

    def download_snap_benefits_recipients(self):
        """
        Unit: Persons
        Not Seasonally Adjusted
        Frequency: Monthly
        """
        snap_benefits_recipients_list = []
        for i in tqdm.tqdm(range(len(self.states_code_loaded))):
            if self.states_code_loaded[i] < 10:
                s = "BR" + str(self.states_abb_loaded[i]) + "0" + str(self.states_code_loaded[i]) +"M647NCEN"
                snap_benefits_recipients_list.append(
                    self.fred.get_series(s))
            else:
                s = "BR" + str(self.states_abb_loaded[i]) + str(self.states_code_loaded[i]) +"M647NCEN"
                snap_benefits_recipients_list.append(
                    self.fred.get_series(s))

        snap_benefits_recipients_list = pd.concat(snap_benefits_recipients_list, axis=1, ignore_index=True)
        snap_benefits_recipients_list.columns = self.states_abb_loaded
        snap_benefits_recipients_list["month"] = snap_benefits_recipients_list.index.month.astype(str)
        snap_benefits_recipients_list["year"] = snap_benefits_recipients_list.index.year.astype(str)
        snap_benefits_recipients_list["date"] = snap_benefits_recipients_list.year.str.cat(snap_benefits_recipients_list.month)
        return snap_benefits_recipients_list

    def download_house_price_index(self):
        """
           Not Seasonally Adjusted
           Frequency: Quarterly
           """
        house_price_index_list = []
        for i in tqdm.tqdm(self.states_abb_loaded):
            tag = i + "STHPI"
            house_price_index_list.append(self.fred.get_series(tag))

        house_price_index_list = pd.concat(house_price_index_list, axis=1, ignore_index=True)
        house_price_index_list.columns = self.states_abb_loaded
        house_price_index_list["month"] = house_price_index_list.index.month.astype(str)
        house_price_index_list["year"] = house_price_index_list.index.year.astype(str)
        house_price_index_list["date"] = house_price_index_list.year.str.cat(house_price_index_list.month)
        return house_price_index_list

    def download_estimatedpercentofpeople_in_poverty(self):
        """
           Unit: Person
           Not Seasonally Adjusted
           Frequency: Annual
           """

        estimatedpercentofpeople_in_poverty_list = []
        for i in tqdm.tqdm(range(len(self.states_code_loaded))):
            if self.states_code_loaded[i] < 10:
                s = "PPAA" + str(self.states_abb_loaded[i]) + "0" + str(self.states_code_loaded[i]) +"000A156NCEN"
                estimatedpercentofpeople_in_poverty_list.append(
                    self.fred.get_series(s))
            else:
                s = "PPAA" + str(self.states_abb_loaded[i]) + str(self.states_code_loaded[i]) +"000A156NCEN"
                estimatedpercentofpeople_in_poverty_list.append(
                    self.fred.get_series(s))

        estimatedpercentofpeople_in_poverty_list = pd.concat(estimatedpercentofpeople_in_poverty_list, axis=1, ignore_index=True)
        estimatedpercentofpeople_in_poverty_list.columns = self.states_abb_loaded
        estimatedpercentofpeople_in_poverty_list["month"] = estimatedpercentofpeople_in_poverty_list.index.month.astype(str)
        estimatedpercentofpeople_in_poverty_list["year"] = estimatedpercentofpeople_in_poverty_list.index.year.astype(str)
        estimatedpercentofpeople_in_poverty_list["date"] = estimatedpercentofpeople_in_poverty_list.year.str.cat(estimatedpercentofpeople_in_poverty_list.month)
        return estimatedpercentofpeople_in_poverty_list

    def download_consumer_sentiment_index_umich(self):
        """
        Not Seasonally Adjusted
        Frequency: Monthly
        """
        consumer_sentiment_index_umich = self.fred.get_series("UMCSENT")
        consumer_sentiment_index_umich = pd.DataFrame(consumer_sentiment_index_umich)
        consumer_sentiment_index_umich["month"] = consumer_sentiment_index_umich.index.month.astype(str)
        consumer_sentiment_index_umich["year"] = consumer_sentiment_index_umich.index.year.astype(str)
        consumer_sentiment_index_umich["date"] = consumer_sentiment_index_umich.year.str.cat(consumer_sentiment_index_umich.month)
        return consumer_sentiment_index_umich

    def download_nber_recession_indicator(self):
        """
        Unit: Binary (+1,0)
        Not Seasonally Adjusted
        Frequency: Monthly
        """
        nber_recession_indicator = self.fred.get_series("USREC")
        nber_recession_indicator = pd.DataFrame(nber_recession_indicator)
        nber_recession_indicator["month"] = nber_recession_indicator.index.month.astype(str)
        nber_recession_indicator["year"] = nber_recession_indicator.index.year.astype(str)
        nber_recession_indicator["date"] = nber_recession_indicator.year.str.cat(nber_recession_indicator.month)
        return nber_recession_indicator

    def download_sp500(self):
        """
           Unit: daily index value at market close.
           The market typically closes at 4 PM ET, except for holidays when it sometimes closes early.
           Not Seasonally Adjusted
           Frequency: Daily
           """
        sp500 = self.fred.get_series("SP500")
        sp500 = pd.DataFrame(sp500)
        sp500["month"] = sp500.index.month.astype(str)
        sp500["year"] = sp500.index.year.astype(str)
        sp500["date"] = sp500.year.str.cat(sp500.month)
        return sp500


class expand_dataset(macro_data):

    def __init__(self):
        super().__init__()
        self.data = None
        self.melted_df = None

    def create_original_dataset(self):
        original_dataset = pd.read_csv("C:/Users/assegnista/new_progress_filled.csv")
        issuedate_original = pd.read_csv("C:/Users/assegnista/loans_with_id.csv", usecols=["id", "issue_d"])
        issuedate_original["issue_d"] = pd.to_datetime(issuedate_original["issue_d"])
        self.data = pd.merge(original_dataset,issuedate_original, on='id')
        self.data['month'] = pd.DatetimeIndex(self.data['issue_d']).month.astype(str)
        self.data['year'] = pd.DatetimeIndex(self.data['issue_d']).year.astype(str)
        self.data["date"] = self.data.year.str.cat(self.data.month)
        return self.data

    def find_lagged_variables(self, dataframe):
        #dataframe["month"] = dataframe.index.month.astype(str)
        #dataframe["year"] = dataframe.index.year.astype(str)
        #dataframe["date"] = dataframe.year.str.cat(dataframe.month)
        list1 = list(self.data["date"])
        list2 = list(dataframe["date"])

        list_difference = []
        for item in list1:
            if item not in list2:
                if item not in list_difference:
                    list_difference.append(item)

        for i in range(0, len(list_difference)):
            list_difference[i] = int(list_difference[i])
        list_difference = sorted(list_difference, reverse=False)

        to_add = pd.DataFrame(np.zeros((len(list_difference), dataframe.shape[1])), columns=dataframe.columns)
        to_add["date"] = list_difference
        dataframe = pd.concat([dataframe, to_add])

        self.melted_df = pd.melt(dataframe, id_vars=["date"], value_vars=dataframe.drop(["month", "year", "date"], axis=1).columns).rename(columns={"variable": "addr_state"})
        self.melted_df['shifted_1'] = self.melted_df.groupby('addr_state')['value'].shift(1)
        self.melted_df['shifted_2'] = self.melted_df.groupby('addr_state')['value'].shift(2)
        self.melted_df['shifted_3'] = self.melted_df.groupby('addr_state')['value'].shift(3)
        self.melted_df['shifted_4'] = self.melted_df.groupby('addr_state')['value'].shift(4)
        self.melted_df['shifted_5'] = self.melted_df.groupby('addr_state')['value'].shift(5)
        self.melted_df['shifted_6'] = self.melted_df.groupby('addr_state')['value'].shift(6)

        self.melted_df["date"] = self.melted_df["date"].astype(str)
        self.melted_df["year"] = self.melted_df["date"].apply(lambda x: x[0:4])
        return self.melted_df

    def add_macro_variables_to_dataset(self, data, melted_df, on_cols= ["date", "addr_state"]):

        dataset_with_macro_factors = pd.merge(data, melted_df, on= on_cols, how="left")

        return dataset_with_macro_factors






