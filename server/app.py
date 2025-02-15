from flask import Flask, render_template, url_for
import os

app = Flask(__name__)

@app.route("/")
def home():
    # Path to image directory
    image_dir = os.path.join(app.static_folder, "images")
    
    # Get list of image filenames
    image_files = [f for f in os.listdir(image_dir) if f.endswith((".jpg", ".png"))]

    # Pass image filenames to the template
    return render_template("index.html", images=image_files)

if __name__ == "__main__":
    app.run(debug=True)
