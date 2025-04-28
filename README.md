
# Quickview
Welcome to the YouTube Video Summarizer project!
This tool automatically fetches the transcript of a YouTube video and generates a concise summary using Python and Natural Language Processing (NLP) techniques.

## Features

- Fetches video transcript using YouTube URL

- Summarizes the transcript into key points or a paragraph

- Handles videos with and without available transcripts

- Easy-to-use command-line interface or API-ready

- Clean and modular Python code

## Tech Stack

- Python 3

- YouTube Transcript API (youtube-transcript-api)

- Hugging Face Transformers (transformers)

- BART model (for abstractive summarization)

- Sentence Transformers (sentence-transformers) (for semantic similarity and extractive summarization)

- Hugging Face Datasets (optional, if batching many examples)

- Flask 



## Installation

1. Clone the repository

```bash
  git clone https://github.com/Dhanyacodes15/quickview-project
cd quickview

```
2. Create a virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

```
3. Install dependencies
```bash
pip install -r requirements.txt

```
4. Run the project
```bash
python app.py
```

## Working

1. Enter the YouTube video URL.

2. The script fetches the transcript automatically.

3. The transcript is passed to the summarization model (BART or Sentence Transformers).

4. The final summary is displayed or saved.



## Model used

- BART (facebook/bart-large-cnn) for abstractive summarization

- Sentence Transformers (e.g., all-MiniLM-L6-v2) for extractive summarization


## Future Improvements
- Deploy a web version (Flask/FastAPI)

- Add support for multilingual transcripts

- Batch summarization for playlists

- Advanced LLM integration (like OpenAI GPT models)
- Flowchart and roadmap creation.

