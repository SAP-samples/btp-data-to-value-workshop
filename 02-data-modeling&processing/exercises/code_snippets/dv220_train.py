import hana_ml
from hana_ml import dataframe
import pandas as pd
import numpy as np


def on_input(data):
    conn = hana_ml.dataframe.ConnectionContext(
    api.config.hanaConnection['connectionProperties']['host'],
    api.config.hanaConnection['connectionProperties']['port'],
    api.config.hanaConnection['connectionProperties']['user'],
    api.config.hanaConnection['connectionProperties']['password'],
    encrypt='true',
    sslValidateCertificate='false')

# insert your specific code / script here ...
    import hana_ml.dataframe as dataframe
    df_hana = (conn.table('Book_Author_Dimension_View', schema='D2VUXXXX'))

    books= df_hana.select(['Book_ID','Book_Description']).collect()
    del df_hana
    books=books.dropna(axis=0,subset=['Book_Description'])

    import nltk
    import ssl

    try:
        _create_unverified_https_context = ssl._create_unverified_context
    except AttributeError:
        pass
    else:
        ssl._create_default_https_context = _create_unverified_https_context

    nltk.download('stopwords')
    from nltk.corpus import stopwords
    Stopwords=set(stopwords.words("english"))
    import regex as re

    #Transform to lower case
    books['tokens']=books['Book_Description'].apply(lambda x: x.lower())
    #Remove punctuation
    books['tokens']=books['tokens'].map(lambda x: re.sub("[-,\.!?;\'\(\)]", ' ', x))
    #Remove stopwords
    books['tokens']=books['tokens'].apply(lambda x: ' '.join([ t for t in x.split() if not t in Stopwords]))
    # Remove short tokens
    books['tokens']=books['tokens'].apply(lambda x:' '.join( [t for t in x.split() if len(t) > 1] ))
    #Remove extra spaces
    books['tokens']=books['tokens'].map(lambda x: re.sub(' +', ' ', x))
    # Remove duplicate tokens
    books['tokens']=books['tokens'].apply(lambda x: ' '.join(list(dict.fromkeys(x.split()))))
    books=books.drop_duplicates('tokens')

    #download word embedding
    import gensim.downloader as gensim_api
    model = gensim_api.load("glove-wiki-gigaword-100")
    features=[]
    for i,book in books.iterrows():
        tokens_features=[]
        for word in book['tokens'].split():
            try:
                tokens_features.append(model[word])
            except:
                continue
        features.append(np.mean(np.array(tokens_features),axis=0))

    for i in range(100):
        feature='f_'+str(i)
        books[feature]=[f[i] for f in features]

    del features
    embedding=['f_'+str(i) for i in range(100)]

    #Fit Kmeans algorithm
    from sklearn.cluster import MiniBatchKMeans
    n_clus=10
    km = MiniBatchKMeans(n_clusters = n_clus,  batch_size=50 , random_state=42, max_iter=1000)
    y_kmeans = km.fit_predict(books[embedding])

    # Silhouette
    from sklearn.metrics import silhouette_score
    score = silhouette_score(books[embedding], km.labels_)

    # to send metrics to the Submit Metrics operator
    metrics_dict = {"SILHOUETTE": str(np.round_(score,2))}

    # send the metrics to the output port - Submit Metrics operator will use this to persist the metrics
    api.send("metrics", api.Message(metrics_dict))

    # create & send the model blob to the output port - Artifact Producer operator will use this to persist the model and create an artifact ID
    import pickle
    model_blob = pickle.dumps(km)
    api.send("modelBlob", model_blob)


api.set_port_callback("trigger", on_input)
