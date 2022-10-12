import json

# Global vars to keep track of model status
model = None
model_ready = False

# Validate input data is JSON
def is_json(data):
  try:
    json_object = json.loads(data)
  except ValueError as e:
    return False
  return True

# When Model Blob reaches the input port
def on_model(model_blob):
    global model
    global model_ready

    import pickle
    model = pickle.loads(model_blob)
    model_ready = True
    api.logger.info("Model Received & Ready")

# Client POST request received
def on_input(msg):
    error_message = ""
    success = False
    prediction = None
    try:
        api.logger.info("POST request received from Client - checking if model is ready")
        if model_ready:
            api.logger.info("Model Ready")
            api.logger.info("Received data from client - validating json input")

            user_data = msg.body.decode('utf-8')
            # Received message from client, verify json data is valid
            if is_json(user_data):
                api.logger.info("Received valid json data from client - ready to use")

                # apply your model
                # load new data
                books = json.loads(user_data)["book_description"]

                # preprocessing
                import nltk
                import ssl

                try:
                    _create_unverified_https_context = ssl._create_unverified_context
                except AttributeError:
                    pass
                else:
                    ssl._create_default_https_context = _create_unverified_https_context

                from nltk.corpus import stopwords
                nltk.download("stopwords")
                stopwords=set(stopwords.words("english"))
                import regex as re

                #Transform to lower case
                books=[ x.lower() for x in books ]
                #Remove punctuation
                books=[ re.sub("[-,\.!?;\'\(\)]", ' ', x) for x in books ]
                #Remove stopwords
                books=[ ' '.join([ t for t in x.split() if not t in stopwords]) for x in books]
                # Remove short tokens
                books=[' '.join( [t for t in x.split() if len(t) > 1]) for x in books]
                #Remove extra spaces
                books=[ re.sub(' +', ' ', x) for x in books]
                # Remove duplicate tokens
                books=[ ' '.join(list(dict.fromkeys(x.split()))) for x in books]


                # GloVe Vectorization
                import gensim.downloader as gensim_api
                word_embedding = gensim_api.load("glove-wiki-gigaword-100")  # load pre-trained word-vectors from gensim-data
                import numpy as np
                features=[]
                for book in books:
                    tokens_features=[]
                    for word in book.split():
                        try:
                            tokens_features.append(word_embedding[word])
                        except:
                            continue
                    features.append(np.mean(np.array(tokens_features),axis=0))

                # deploy cluster model
                predictions = model.predict( features)
                success = True
            else:
                api.logger.info("Invalid JSON received from client - cannot apply model.")
                error_message = "Invalid JSON provided in request: " + user_data
                success = False
        else:
            api.logger.info("Model has not yet reached the input port - try again.")
            error_message = "Model has not yet reached the input port - try again."
            success = False
    except Exception as e:
        api.logger.error(e)
        error_message = "An error occurred: " + str(e)

    if success:
        # apply carried out successfully, send a response to the user
        msg.body = json.dumps({'Cluster:': predictions.tolist()})
    else:
        msg.body = json.dumps({'Error': error_message})

    new_attributes = {'message.request.id': msg.attributes['message.request.id']}
    msg.attributes =  new_attributes
    api.send('output', msg)

api.set_port_callback("model", on_model)
api.set_port_callback("input", on_input)
