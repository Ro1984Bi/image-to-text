from app import app
from flask import render_template, request, url_for
from PIL import Image
from ml import extract_text
from werkzeug.utils import secure_filename
import numpy as np
import random
import pytesseract
import string
import os

app.config["INITIAL_FILE_UPLOADS"] = "app/static/uploads"


@app.route("/", methods=["GET", "POST"])
def index():
    full_filename = url_for("static", filename="images")
    if request.method == "POST":
        image_upload = request.files["image_upload"]
        # save the file
        filename = secure_filename(image_upload.filename)
        filepath = os.path.join(app.config["INITIAL_FILE_UPLOADS"], filename)
        image_upload.save(filepath)

        extracted_text = extract_text(filepath)
        img_url = url_for("static", filename="uploads/"+filename)

        return render_template("index.html", img_url=img_url, full_filename=filepath, text=extracted_text)

    return render_template("index.html", full_filename=full_filename)


# main function
if __name__ == "__main__":
    app.run(debug=True)
