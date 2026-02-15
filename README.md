# CV-Server

Flask app that processes video through a pipeline of image filters and effects.

## What it does
- Pipes video frames through a bunch of image processing layers
- Three stages( More can be added ): pre-processing, rendering, post-processing
- Shows the results in your browser in real-time


## Quick start
1. Install stuff: `pip install flask opencv-python numpy`
2. Run it: `python CVserver.py`
3. Open `http://localhost:5000`

## Files
- `CVserver.py` - main Flask server
- `Layers.py` - where the image processing magic happens
- `templates/index.html` - the web UI
