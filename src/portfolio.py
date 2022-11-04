import numpy as np
import pandas as pd
from datetime import datetime

class Portfolio():
    def __init__(self, data):
        self.data = data
        
        
    def get_stock_position_by_name(self, date, firstname, lastname, permno):
        p_data = self.data[(self.data["firstname"]==firstname) & (self.data["lastname"]==lastname)].copy()
        if len(p_data) == 0:
            print(f"{firstname} {lastname} is not in dataset. ")
            return None, None, None
        ps_data = p_data[p_data["permno"]==permno].copy()
        if len(ps_data) == 0:
            print(f"{firstname} {lastname} did not have stock {permno}. ")
            return None, None, None
        
        date = datetime.fromisoformat(date)
        ps_data["evtdate"] = ps_data["evtdate"].apply(datetime.fromisoformat)
        ps_data["evtdate_end"] = ps_data["evtdate_end"].apply(datetime.fromisoformat)
        
        for i in np.arange(len(ps_data)):
            if date < min(ps_data["evtdate"]):
                return datetime.fromisoformat("2011-12-31"), 0, -1
            if date >= ps_data["evtdate"].iloc[i] and date <= ps_data["evtdate_end"].iloc[i]:
                return ps_data["evtdate"].iloc[i], ps_data["position"].iloc[i], ps_data["init_pos"].iloc[i]
    
    def get_portfolio_by_name(self, date, firstname, lastname):
        p_data = self.data[(self.data["firstname"]==firstname) & (self.data["lastname"]==lastname)]
        if len(p_data) == 0:
            print(f"{firstname} {lastname} is not in dataset. ")
            return None
        
        portfolio = pd.DataFrame()
        for stock in np.unique(p_data["permno"]):
            portfolio = pd.concat([portfolio, 
                                   pd.DataFrame([[stock] + list(self.get_stock_position_by_name(date, firstname, lastname, stock))])])
        portfolio.columns = ["permno", "evtdate", "position", "init_pos"]
        return portfolio
    
    
    def get_stock_position_by_fecid(self, date, fecid, permno):
        p_data = self.data[self.data["fecid"]==fecid]
        if len(p_data) == 0:
            print(f"{fecid} is not in dataset. ")
            return None, None, None
        ps_data = p_data[p_data["permno"]==permno].copy()
        if len(ps_data) == 0:
            print(f"{firstname} {lastname} did not have stock {permno}. ")
            return None, None, None
        
        date = datetime.fromisoformat(date)
        ps_data["evtdate"] = ps_data["evtdate"].apply(datetime.fromisoformat)
        ps_data["evtdate_end"] = ps_data["evtdate_end"].apply(datetime.fromisoformat)
        
        for i in np.arange(len(ps_data)):
            if date < min(ps_data["evtdate"]):
                return datetime.fromisoformat("2011-12-31"), 0, -1
            if date >= ps_data["evtdate"].iloc[i] and date <= ps_data["evtdate_end"].iloc[i]:
                return ps_data["evtdate"].iloc[i], ps_data["position"].iloc[i], ps_data["init_pos"].iloc[i]
    
    def get_portfolio_by_fecid(self, date, fecid):
        p_data = self.data[self.data["fecid"]==firstname]
        if len(p_data) == 0:
            print(f"{fecid} is not in dataset. ")
            return p_data
        
        portfolio = pd.DataFrame()
        for stock in np.unique(p_data["permno"]):
            portfolio = pd.concat([portfolio, 
                                   pd.DataFrame([[stock] + list(self.get_stock_position_by_fecid(date, firstname, lastname, stock))])])
        portfolio.columns = ["permno", "evtdate", "position", "init_pos"]
        return portfolio
