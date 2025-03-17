from flask import Flask, request, render_template, send_from_directory
import os
import yt_dlp

app = Flask(__name__)

# Set the folder where downloaded videos will be stored
DOWNLOAD_FOLDER = os.path.join(os.getcwd(), "downloads")
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER

# Ensure the downloads folder exists
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download_video():
    video_url = request.form.get("video_url")

    if not video_url:
        return "Error: No URL provided", 400

    try:
        ydl_opts = {
            'outtmpl': os.path.join(DOWNLOAD_FOLDER, '%(title)s.%(ext)s'),
            'format': 'best',
        }

        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info = ydl.extract_info(video_url, download=True)
            filename = ydl.prepare_filename(info)
            filename = os.path.basename(filename)

        return f"Download complete! <a href='/files/{filename}'>Click here to download</a>"

    except Exception as e:
        return f"Error: {str(e)}", 500

@app.route('/files/<filename>')
def serve_file(filename):
    return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
