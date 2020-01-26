import pandas as pd

# Import csv files
rb_2013 = pd.read_csv("../data/Rushing "
                       "Stats/2013_Rushing_stats.csv")

rb_2014 = pd.read_csv("../data/Rushing "
                       "Stats/2014_Rushing_stats.csv")

rb_2015 = pd.read_csv("../data/Rushing "
                       "Stats/2015_Rushing_stats.csv")

rb_2016 = pd.read_csv("../data/Rushing "
                       "Stats/2016_Rushing_stats.csv")

rb_2017 = pd.read_csv("../data/Rushing "
                       "Stats/2017_Rushing_stats.csv")

rb_2018 = pd.read_csv("../data/Rushing "
                       "Stats/2018_Rushing_stats.csv")

# Join dataframes based on unique player id
rb_2013_2014 = pd.merge(rb_2013, rb_2014, how="left", on=["Player", "Player"])
rb_2014_2015 = pd.merge(rb_2014, rb_2015, how="left", on=["Player", "Player"])
rb_2015_2016 = pd.merge(rb_2015, rb_2016, how="left", on=["Player", "Player"])
rb_2016_2017 = pd.merge(rb_2016, rb_2017, how="left", on=["Player", "Player"])
rb_2017_2018 = pd.merge(rb_2017, rb_2018, how="left", on=["Player", "Player"])

# Concatenate all frames below one another
rb_dfs = [rb_2013_2014, rb_2014_2015, rb_2015_2016, rb_2016_2017, rb_2017_2018]
rb_df = pd.concat(rb_dfs)
