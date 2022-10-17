FROM python:3.10
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# VOLUME [ "/app" ]
# VOLUME [ "/PKI" ]

# EXPOSE 8000
ENTRYPOINT [ "python", "-u", "ca.py" ]
CMD [ "--help" ]

# la -u è per mostrare i print nel log (UNBUFFERED=1)