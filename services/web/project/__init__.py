from flask import Flask, jsonify
import json
import os

app = Flask(__name__)


def get_info_kubernetes():
    d = {
        "node_name": os.environ.get('NODE_NAME'),
        "pod_name": os.environ.get('POD_NAME'),
        "pod_namespace": os.environ.get('POD_NAMESPACE'),
        "pod_id": os.environ.get('POD_IP'),
        "pod_service_account": os.environ.get('POD_SERVICE_ACCOUNT')        
    }
    return d


@app.route("/")
def get_info():
    di = get_info_kubernetes()
    return jsonify(di)



    
