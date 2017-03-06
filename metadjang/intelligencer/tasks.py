from .celeryconf import app
import json



@app.task
def add_to_queue(log_entry):
    #parse through the serialized object and save() models here
    data = {}
    return data
