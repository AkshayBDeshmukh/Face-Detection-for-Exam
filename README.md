# Face-Detection-for-Exam
The code you've provided is a Flask web application that performs face detection using the face-api.js library and displays the results on a web page. It combines both server-side Python code and client-side JavaScript to achieve this. Here's a detailed description of the code:

### Server-side (Python) code:

1. Import necessary modules: The code starts by importing the required Python modules, including Flask, OpenCV (cv2), NumPy, and others.

2. Create a Flask application: An instance of the Flask web application is created with the name 'app', and a secret key is set for session management.

3. Load the pre-trained Haar Cascade Classifier: A pre-trained Haar Cascade Classifier for face detection is loaded using OpenCV. This classifier is used as a fallback for face detection in case the face-api.js library fails to detect faces.

4. Define a route for the homepage ('/') that handles both GET and POST requests.

5. In the POST request handler:
   - It checks if a file was uploaded.
   - If no file was uploaded, it displays a flash message and redirects to the homepage.
   - If a file is uploaded:
     - It saves the uploaded file to a temporary directory under the 'uploads' folder.
     - Performs face detection on the uploaded image using both the Haar Cascade Classifier and face-api.js library (client-side).
     - Draws rectangles around detected faces using OpenCV on the server-side image.
     - Saves the server-side image with detected faces to the 'static' folder.
     - Renders the 'index.html' template with the path to the result image.

6. In the GET request handler, it renders the 'index.html' template without any result image.

7. If the script is run directly (not imported as a module), it creates 'uploads' and 'static' directories if they don't exist and starts the Flask web application in debug mode.

### Client-side (JavaScript) code (inside 'index.html'):

1. HTML Structure: The HTML file defines the basic structure of the web page. It includes a title, an h1 header, and a <div> element with the id 'videoContainer' where the video feed and face detection results will be displayed.

2. JavaScript:
   - It creates an HTML5 video element and configures it to autoplay and have specific dimensions.
   - It attempts to access the user's camera using `navigator.mediaDevices.getUserMedia` and sets the video stream as the source for the video element.
   - The face-api.js library is loaded from a CDN, and face detection models are loaded using `faceapi.nets`. The models include the TinyFaceDetector, face landmarks, and face recognition.
   - The `startFaceDetection` function is called when the video starts playing. Inside this function:
     - A canvas is created from the video element to draw face detection results.
     - The canvas dimensions are set to match the video dimensions.
     - Face detection is performed at regular intervals (every 100 milliseconds) using `faceapi.detectAllFaces`. Detected faces are drawn on the canvas along with face landmarks.

Overall, this code creates a web application that allows users to upload images for server-side face detection using OpenCV's Haar Cascade Classifier and performs real-time face detection from the user's camera feed using face-api.js on the client-side. Detected faces are displayed with rectangles and landmarks on a canvas element.
