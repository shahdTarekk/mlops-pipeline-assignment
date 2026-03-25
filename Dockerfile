FROM python:3.10-slim

ARG RUN_ID

WORKDIR /app

RUN echo "Simulating model download for MLflow Run ID: ${RUN_ID}"

CMD ["sh", "-c", "echo Deployment container started for Run ID: ${RUN_ID}"]
