
FROM python


WORKDIR /app


COPY . /app


RUN pip install --no-cache-dir nltk && \
    python -m nltk.downloader stopwords


CMD ["python", "script.py"]
