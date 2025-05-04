FROM python:3.11.9-slim AS builder

WORKDIR /root

RUN apt update \
    && apt install git -y \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install --upgrade pip \
    && pip install --no-cache-dir --prefix /install -r requirements.txt


FROM python:3.11.9-slim

WORKDIR /root

COPY --from=builder /install /usr/local
COPY app/ /root/app

# TODO get preprocessor joblib from github
COPY model/preprocessor.joblib /root/model/preprocessor.joblib

ENTRYPOINT ["python"]
CMD ["app/serve_model.py"]