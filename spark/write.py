from cfg.configs import *

# writer jdbc method 
def writer_jdbc(dataframe, name_df):
    dataframe.write.jdbc(url=cfg['postgres']['url'], 
        table=cfg[name_df]['table'],
        mode=cfg['postgres']['mode'], 
        properties=cfg['postgres']['properties'])
