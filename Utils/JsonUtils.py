import json

import numpy as np
from flask import jsonify

from Utils.JSON import NumpyArrayEncoder


def ToJson(user) :
    angle = np.rad2deg(np.angle(user.frog_state.data))
    numpyData = {"id": user.id, "state": user.frog_state.data.real, "angle": angle}
    encodedNumpyData = json.dumps(numpyData, cls=NumpyArrayEncoder)

    return jsonify(encodedNumpyData)