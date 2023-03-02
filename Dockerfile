FROM python:3.9-slim
ENV PORT 8080
WORKDIR /app
RUN apt update && apt install -y curl build-essential && rm -rf /var/lib/apt/lists/*
RUN curl -sSL https://raw.githubusercontent.com/pdm-project/pdm/main/install-pdm.py | python3 -
COPY . /app
RUN /root/.local/bin/pdm install
RUN /root/.local/bin/pdm run python preload.py
EXPOSE $PORT
ENTRYPOINT ["/root/.local/bin/pdm", "serve"]
