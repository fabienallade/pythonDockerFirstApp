FROM python:3.9
LABEL maintener="ALLADE Fabien"
WORKDIR /home/workspace/
RUN pip install Flask
COPY . .
COPY ./requirements.txt /home/workspace/
RUN pip install -r requirements.txt
ENTRYPOINT [ "python" ]
CMD ["app.py"]
EXPOSE 5000