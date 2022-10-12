import hana_ml
from hana_ml import dataframe
import numpy as np

def on_input(data):
    conn = hana_ml.dataframe.ConnectionContext(
        api.config.hanaConnection['connectionProperties']['host'],
        api.config.hanaConnection['connectionProperties']['port'],
        api.config.hanaConnection['connectionProperties']['user'],
        api.config.hanaConnection['connectionProperties']['password'],
        encrypt='true',
        sslValidateCertificate='false'
    )

# insert your specific code / script here ...
    df_hana = (conn.table('PP_All_BL_Sales_Order_Data', schema='PA09700UXXX')) #Check your table and schema name in DI Metadata Explorer!
    df_hana=df_hana.select('Order_ID','Book_ID')

    from hana_ml.algorithms.pal.association import Apriori

    min_support=0.0005
    min_confidence=0.05
    min_lift=5

    ap = Apriori(min_support=min_support,
             min_confidence=min_confidence,
             max_len = 2,
             min_lift=min_lift
             )

    ap.fit(data=df_hana)
    ap.result_.save(where='APRIORI_BOOK_ASSOCIATION_IDS',force=True)

# output some quality metrics
    result = {"number_of_associations": str(ap.result_.shape[0])}
    api.send("result", api.Message(result))

api.set_port_callback("trigger", on_input)