from flask import Flask, request
import json
import urllib.request
from fastai.vision import *
from io import BytesIO


UPLOAD_FOLDER = '/home/raza/Desktop'

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route("/analyze", methods = ['GET', 'POST'])
def home():
	if request.method == "POST":
		image = request.files["file"].read()
# print(image)
		defaults.device = torch.device('cpu')
		path = Path('.')
		learner = load_learner(path, 'export.pkl')

		img = open_image(BytesIO(image))
		prediction = learner.predict(img)[0]

		print(str(prediction))

		return {'result': str(prediction)}
	return "hroku"


if __name__ == "__main__":
	app.run(threaded = True)
