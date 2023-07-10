from flask import Flask, request, jsonify
from youtube_transcript_api import YouTubeTranscriptApi

app = Flask(__name__)

@app.route('/transcript-api', methods=['GET'])
def get_transcript():
    video_id = request.args.get('videoId', default = "", type = str)
    if video_id:
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            print("Transcript for video {} fetched successfully.".format(video_id))  # This message will be logged in your server console
            return jsonify(transcript)
        except Exception as e:
            return jsonify({'error': str(e)}), 500
    else:
        return jsonify({'error': 'videoId parameter is required'}), 400

if __name__ == '__main__':
    app.run(port=3000, debug=True)
