from flask import Flask, render_template, request, flash
from encode import EncodedImage
import os

app = Flask(__name__)

@app.route("/")
def login():
    return render_template("login.html")

@app.route("/encode", methods=["GET", "POST"])
def encode():
    k = None
    f = None
    image_submited = False
    if request.method == "POST":
        # saves the uploaded image
        print("file uploaded")
        f = request.files["uploaded_image"]
        f.save("static/resources/uploaded_image.png")
        image_submited = True

        # encodes the image with the given text
        text = request.form.get("encoded_text")
        e = EncodedImage(text, "static/resources/")
        e.create_text_image()
        e.encode_image()
        e.create_image("encoded_image.png")
        k = e.key
        

    return render_template("encode.html", image_submited=image_submited, key=k)

@app.route("/decode", methods=["GET", "POST"])
def decode():
    image_submited = False
    if request.method == "POST":
        f = request.files["encoded_image"]
        f.save("static/resources/uploaded_image.png")
        image_submited = True

        key = int(request.form.get("key"))
        e = EncodedImage(None, "static/resources/")
        e.decode_image(key)
        e.create_image("decoded_image.png")

    return render_template("decode.html", image_submited=image_submited)

if __name__ == "__main__":
    app.run(debug=True)