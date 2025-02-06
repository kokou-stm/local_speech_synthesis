FROM python-3.9

WORKDIR /app

COPY ./requirements.txt /app/requirements.txt

RUN  pip install --no-cache-dir --upgrade -r requirements.txt

COPY ./* /app/

CMD ["fastapi", "run", "app/main.py", "--port", "80"  ]