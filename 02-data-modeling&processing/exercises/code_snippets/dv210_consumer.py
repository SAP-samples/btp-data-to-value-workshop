import json
import hana_ml
from hana_ml import dataframe
import pandas as pd

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

# Load the Hana ML model
#def on_trigger(data):

conn = hana_ml.dataframe.ConnectionContext(
    api.config.hanaConnection['connectionProperties']['host'],
    api.config.hanaConnection['connectionProperties']['port'],
    api.config.hanaConnection['connectionProperties']['user'],
    api.config.hanaConnection['connectionProperties']['password'],
    encrypt='true',
    sslValidateCertificate='false')

try:
    # Load your HANA_ML model here
    model = (conn.table('APRIORI_BOOK_ASSOCIATION_IDS', schema='PA09700UXXX#DI')) #Check your table and schema name in DI Metadata Explorer!
    model_ready = True
    api.logger.info("Model Received & Ready")
except Exception as e:
    api.logger.error(e)
    error_message = "An error occurred while loading the model: " + str(e)


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
                # obtain your results
                book_ID = json.loads(user_data)["book"]
                filter_string='ANTECEDENT = '+str(book_ID)
                prediction = model.filter(filter_string).sort('LIFT',desc=True).select('CONSEQUENT').collect().values.tolist()
                if len(prediction) == 0:
                    prediction='No rule available for this book'

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
        msg.body = json.dumps({'recommendation': prediction})
    else:
        msg.body = json.dumps({'Error': error_message})

    new_attributes = {'message.request.id': msg.attributes['message.request.id']}
    msg.attributes =  new_attributes
    api.send('output', msg)

api.set_port_callback("input", on_input)
