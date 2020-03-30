from flask import Flask, request



# UPLOAD_FOLDER = '/home/raza/Desktop'

app = Flask(__name__)

# app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
@app.route("/analyze", methods = ['GET', 'POST'])
def home():
	if request.method == "POST":
		image = request.files['image']
		# print(image)
		# filename = secure_filename(image.filename)
		# image.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
		return {'result': 10}
	else:
		return "hroku"

if __name__ == "__main__":
	app.run(threaded = True)
