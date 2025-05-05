FROM python:3.11.9-slim AS builder

WORKDIR /root

RUN apt update \
    && apt install git -y \
    && apt clean \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --upgrade pip

COPY app/ /root/app/
COPY setup.py /root
COPY data/ /root/data/

RUN pip install .

RUN python app/preprocessor_loader.py

FROM python:3.11.9-slim

WORKDIR /root

ARG VERSION

LABEL version=$VERSION

ENV MODEL_SERVICE_VERSION=$VERSION

COPY --from=builder /usr/local /usr/local
COPY --from=builder /root/output/preprocessor.joblib /root/output/preprocessor.joblib

ENTRYPOINT ["python"]
CMD ["-m", "app.main"]