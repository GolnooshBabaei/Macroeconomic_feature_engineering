from typing import List
import pandas as pd
import tqdm
from fredapi import Fred
import numpy as np
import json


class macro_data:
    def __init__(self):
        self.states_abb_loaded = json.load(open("C:/Users/assegnista/state_abbreviations_version2.json", "r"))
        self.states_code_loaded = json.load(open("C:/Users/assegnista/state_codes.json", "r"))
        self.fred = Fred("156f8f8866d24f160c68104b9df1a2fe")


    def download_cpi(self):
        """
        All items, all urban consumers,
        not seasonally adjusted
        Frequency: Annual
        """
        s = ["CUUR0100SA0", "CUUR0400SA0", "CUUR0200SA0", "CUUR0300SA0"]  # NORTHEAST, WEST, MIDWEST, AND SOUTH
        regional_cpi = []
        for i in tqdm.tqdm(s):
            regional_cpi.append(self.fred.get_series(i))

        regional_cpi = pd.concat(regional_cpi, axis=1, ignore_index=True)
        #regional_cpi = pd.DataFrame(regional_cpi)
        regional_cpi.columns = ["NORTHEAST", "WEST", "MIDWEST","SOUTH"]
        return regional_cpi

    def download_unemployment_rate(self):
        """
        Ratio of the unemployed people on labor force
        """
        ur_list = []
        for i in tqdm.tqdm(self.states_abb_loaded):
            tag = i + "UR"
            ur_list.append(self.fred.get_series(tag))

        ur_list = pd.concat(ur_list, axis=1, ignore_index=True)
        #ur_list = pd.DataFrame(ur_list)
        ur_list.columns = self.states_abb_loaded
        return ur_list

    def download_annual_income(self):
        """
        Statistics for each state (and the District of Columbia) show the combined personal incomes of the residents,
        including those whose work takes place beyond the state's borders. The data include income by industry and how
        much income comes from wages, proprietors' income, dividends, interest, rents, and government benefits.
        These statistics help assess and compare the economic well-being of state residents. Per capita personal income
        – an area's personal income divided by its population – can be used to compare incomes from one state to
        another or to the nation overall.
        """
        income_list = []
        for i in tqdm.tqdm(self.states_abb_loaded):
            tag = i + "PCPI"
            income_list.append(self.fred.get_series(tag))

        income_list = pd.concat(income_list, axis=1, ignore_index=True)
        #income_list = pd.DataFrame(income_list)
        income_list.columns = self.states_abb_loaded
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
        #hown_list = pd.DataFrame(hown_list)
        hown_list.columns = self.states_abb_loaded
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
        #resident_pop_list = pd.DataFrame(resident_pop_list)
        resident_pop_list.columns = self.states_abb_loaded
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
        #snap_benefits_recipients_list = pd.DataFrame(snap_benefits_recipients_list)
        snap_benefits_recipients_list.columns = self.states_abb_loaded
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
        #house_price_index_list = pd.DataFrame(house_price_index_list)
        house_price_index_list.columns = self.states_abb_loaded
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
        #estimatedpercentofpeople_in_poverty_list = pd.DataFrame(estimatedpercentofpeople_in_poverty_list)
        estimatedpercentofpeople_in_poverty_list.columns = self.states_abb_loaded
        return estimatedpercentofpeople_in_poverty_list


    def download_consumer_sentiment_index_umich(self):
        """
        Not Seasonally Adjusted
        Frequency: Monthly
        """
        consumer_sentiment_index_umich = self.fred.get_series("UMCSENT")
        return consumer_sentiment_index_umich

    def download_nber_recession_indicator(self):
        """
        Unit: Binary (+1,0)
        Not Seasonally Adjusted
        Frequency: Monthly
        """
        nber_recession_indicator = self.fred.get_series("USREC")
        return nber_recession_indicator

    def download_sp500(self):
        """
           Unit: daily index value at market close.
           The market typically closes at 4 PM ET, except for holidays when it sometimes closes early.
           Not Seasonally Adjusted
           Frequency: Daily
           """
        sp500 = self.fred.get_series("SP500")
        return sp500




class expand_dataset(macro_data):

    def __init__(self):
        super().__init__()

    def create_original_dataset(self):
        self.original_dataset = pd.read_csv()
