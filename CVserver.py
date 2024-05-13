from flask import Flask, render_template, Response
import cv2
import Layers
import numpy as np
import inspect as insp


app = Flask(__name__)

Sequence = []

Pre = Layers.Precompositions()
Sequence.append(Pre)

Renders = Layers.RenderTasks()
Sequence.append(Renders)

Post = Layers.Postcompositions()
Sequence.append(Post)


cap = cv2.VideoCapture("1053 12.05.2023 10.mp4")

def generate_frames():
    method_names = []

    while True:
        success, frame = cap.read() 

        if not success:
            print("Bruh")
            print("Frame Capture messed up")
            break
        for mode in Sequence:    
            methods = [method for method in dir(mode) if insp.ismethod(getattr(mode, method))]
            methods.sort()
            method_names.extend(methods)

            print(methods)

            for method in methods:
                method = getattr(mode, method)

                if callable(method) and hasattr(method, '__call__'):
                    frame = method(frame)
                elif method.__code__.co_argcount > 1:
                    print(f"Weird number of arguments were were passed in {method} call\n Only one argument is expected")
                else:
                    print("Something real bad is happening")



        ret, buffer = cv2.imencode('.jpg', frame)

        if not ret:
            print("Bruh")
            print("JPEG conversion messed up")
            break

        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        
    return method_names    
        


def original_frames():
     cap = cv2.VideoCapture("1053 12.05.2023 10.mp4")

     while True:
        success, frame = cap.read() 

        if not success:
            print("Bruh")
            print("Frame Capture messed up")
            break
        
        height, width = frame.shape[:2]
        border_size = 120
        cropped_image = frame[border_size:height-border_size, border_size:width-border_size]
        frame = cropped_image

        ret, buffer = cv2.imencode('.jpg', frame)

        if not ret:
            print("Bruh")
            print("JPEG conversion messed up")
            break

        frame_bytes = buffer.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        

@app.route('/')
def index():
    method_names = generate_frames()
    return render_template('index.html',method_names=method_names)

@app.route('/video_feed')
def video_feed():
    return Response(generate_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

@app.route('/original_feed')
def original_feed():
    return Response(original_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == "__main__":
    app.run(debug=True)
