from flask import Flask, render_template, request
# if you encounter dependency issues using 'pip install flask-uploads'
# try 'pip install Flask-Reuploaded'
from flask_uploads import UploadSet, configure_uploads, IMAGES
from model import predict_class
app = Flask(__name__)

photos = UploadSet('photos', IMAGES)

# path for saving uploaded images
app.config['UPLOADED_PHOTOS_DEST'] = './static/img'
configure_uploads(app, photos)

# professionals have standards :p
@app.route('/home', methods=['GET', 'POST'])
def home():
    welcome = "Hello, World !"
    return welcome

# the main route for upload and prediction
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST' and 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        test = predict_class()
        answer = "For {} : <br>The prediction of the image is : {}".format(filename, test)
        return answer
    return render_template('upload.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
