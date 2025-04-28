from flask import Flask, render_template, request
from sentence_transformers import util
from transformers import pipeline, AutoTokenizer, AutoModelForSeq2SeqLM
from youtube_transcript_api import YouTubeTranscriptApi
from urllib.parse import urlparse, parse_qs

app = Flask(__name__)

# Load model and tokenizer
model_name = "facebook/bart-large-cnn"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)
summarizer = pipeline("summarization", model=model, tokenizer=tokenizer)

# Helper function to extract YouTube video ID
def extract_video_id(youtube_url):
    query = urlparse(youtube_url)
    if query.hostname == 'youtu.be':
        return query.path[1:]
    if query.hostname in ['www.youtube.com', 'youtube.com']:
        if query.path == '/watch':
            return parse_qs(query.query).get('v', [None])[0]
        elif query.path.startswith(('/embed/', '/v/')):
            return query.path.split('/')[2]
    return None

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        youtube_url = request.form.get("youtube_url")
        try:
            video_id = extract_video_id(youtube_url)
            if not video_id:
                return render_template("index.html", error="Invalid YouTube URL.")

            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            full_text = " ".join([item['text'] for item in transcript])

            # Split into chunks for summarization (approx. 1000 characters)
            max_chunk = 1000
            chunks = [full_text[i:i + max_chunk] for i in range(0, len(full_text), max_chunk)]

            summarized_chunks = []
            for chunk in chunks:
                summary_result = summarizer(chunk, max_length=50, min_length=25, do_sample=False)
                if summary_result and len(summary_result) > 0 and 'summary_text' in summary_result[0]:
                    summary = summary_result[0]['summary_text']
                else:
                    summary = ""
                summarized_chunks.append(summary)

            summary = " ".join(summarized_chunks)

            return render_template("index.html", summary=summary, youtube_url=youtube_url)

        except Exception as e:
            return render_template("index.html", error=str(e))

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
