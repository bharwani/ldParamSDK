import ldclient
from ldclient.config import Config
from ldclient import Context
import logging
import sys
import time
from flask import (Flask, abort, jsonify, make_response, render_template,
                   request, url_for)
import urllib.parse


root = logging.getLogger()
root.setLevel(logging.DEBUG)
ch = logging.StreamHandler(sys.stdout)
ch.setLevel(logging.DEBUG)
formatter = logging.Formatter(
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
ch.setFormatter(formatter)
root.addHandler(ch)

app = Flask(__name__)

@app.route('/api/v1/flags', methods=['POST'])
def flagger():
    if request.method == 'POST':
        # Grab some info
        data = request.json
        serverKey = request.args.get('sdk', type=str)
        print(serverKey)
        #app.logger.debug('POST request with parameter: ' + serverKey.get('sdk') + ' and body data: '+ serverKey)
        ldclient.set_config(Config(serverKey))
        client = ldclient.get()

        #Wait for SDK to initialize
        if ldclient.get().is_initialized():
            app.logger.info("SDK successfully initialized!")
        else:
            app.logger.info("SDK failed to initialize")
            exit()

        # TODO: Build context from request body JSON
        context = Context.builder(data).name("Sandy").build()
        #context = Context.builder(data).name("Sandy").build
        
        # TODO: switch to allFlags()
        flag_value = client.variation("gold-view", context, False)
        #flagValues = ldclient.get().all_flags_state(context)

        #ldclient.get().flush()
        #ldclient.get().close()
        return f'POST request: gold-view has value: {flag_value}'
    else:
        abort(405)
        #return 'Method not allowed", 405

if __name__ == '__main__':
    app.run(debug=True)