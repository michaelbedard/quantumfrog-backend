import json

import numpy as np
from flask import jsonify
from json import JSONEncoder

class NumpyArrayEncoder(JSONEncoder):

    def default(self, obj):
        if isinstance(obj, np.ndarray):
            return obj.tolist()
        return JSONEncoder.default(self, obj)

def toJson(user) :
    amplitudes = user.frog_state.data.real
    angle = np.rad2deg(np.arctan(amplitudes[1]/amplitudes[0]))
    numpyData = {"id": user.id, "state": amplitudes, "angle": angle}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)


    return jsonify(encodedNumpyData)

