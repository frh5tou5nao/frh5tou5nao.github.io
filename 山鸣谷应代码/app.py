from flask import Flask, session, request, redirect, render_template, url_for
import re
import os
import random

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='')
app.config['STATIC_URL'] = '/static'
app.secret_key = 'AGuf27^$EDQSf71'

def get_background_images():
    backgrounds_dir = os.path.join(app.static_folder, 'backgrounds')
    return [os.path.join(backgrounds_dir, img) for img in os.listdir(backgrounds_dir) if img.endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]

def get_audio_files():
        audio_dir = os.path.join(app.static_folder, 'audios')
        return [os.path.join(audio_dir, audio) for audio in os.listdir(audio_dir) if audio.endswith(('.mp3', '.wav', '.ogg'))]

@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == "POST":
        poe = request.form.get("name")
        background_images = get_background_images()
        background_image = random.choice(background_images)
        background_image_url = os.path.relpath(background_image, app.static_folder)
        audio_files = get_audio_files()
        if audio_files:
            audio_file = random.choice(audio_files)
            audio_url = os.path.relpath(audio_file, app.static_folder)
        else:
            audio_url = None
        return render_template("poem.html", msg=poe, background_image=background_image_url,audio_url=audio_url)
    else:
        return render_template("result.html")

@app.route('/result')
def result():
    return render_template('result.html')


if __name__ == "__main__":
    app.run()
