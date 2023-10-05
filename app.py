import os
from flask import Flask, render_template, request, redirect, url_for, flash
import cv2
import numpy as np

app = Flask(__name__)
app.secret_key = os.urandom(24)

# Load the pre-trained Haar Cascade Classifier for face detection
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # Check if a file was uploaded
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        # Check if the file has a filename
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)

        if file:
            # Save the uploaded file to a temporary directory
            filename = os.path.join('uploads', file.filename)
            file.save(filename)

            # Perform face detection on the uploaded image
            img = cv2.imread(filename)
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = face_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))

            # Draw rectangles around detected faces
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)

            # Save the image with detected faces
            result_filename = os.path.join('static', 'result_' + file.filename)
            cv2.imwrite(result_filename, img)

            return render_template('index.html', result_image=result_filename)

    return render_template('index.html')

if __name__ == '__main__':
    if not os.path.exists('uploads'):
        os.makedirs('uploads')
    if not os.path.exists('static'):
        os.makedirs('static')
    app.run(debug=True)

