from flask import Flask, render_template, request, jsonify
import yt_dlp, os
import requests

app = Flask(__name__)

# Replace this with your actual YouTube Data API key
YOUTUBE_API_KEY = 'AIzaSyCvBdRTroPIKd7RSlS6sDtcOlMXWfmhRsY'
SEARCH_URL = 'https://www.googleapis.com/youtube/v3/search'

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/search')
def search_youtube():
    query = request.args.get('q')
    params = {
        'key': YOUTUBE_API_KEY,
        'part': 'snippet',
        'q': query,
        'type': 'video',
        'maxResults': 5
    }
    response = requests.get(SEARCH_URL, params=params)
    return jsonify(response.json())

@app.route('/stream')
def get_stream_url():
    print("🔍 Received request for /stream")
    video_id = request.args.get('video_id')
    video_url = f"https://www.youtube.com/watch?v={video_id}"

    ydl_opts = {
        'quiet': True,
        'skip_download': True,
        'format': 'bestaudio[ext=m4a]/bestaudio/best',
        'noplaylist': True,
        'cookiefile': 'cookie.txt',
        'quiet': True,
         'skip_download': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(video_url, download=False)
        return jsonify({'stream_url': info['url']})

if __name__ == '__main__':
    app.run(debug=True, use_reloader=False)
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
