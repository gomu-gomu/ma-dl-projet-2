FROM python:3.9-slim
WORKDIR /app

RUN python -m venv .venv
ENV VIRTUAL_ENV=/app/.venv
ENV PATH="VIRTUAL_ENV/bin:$PATH"

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src
COPY assets/ ./assets

EXPOSE 8501

CMD ["streamlit", "run", "src/Accueille.py"]
