FROM pyenv:1.0

WORKDIR /usr/src/app

COPY . .

ENTRYPOINT ["python"]

CMD ["app.py"]


###############   TO BUILD   ###################
# sudo docker build -t pyenv:2.0 .
# sudo docker run -p 5000:5000 --name deploywith pyenv:2.0


###############   TO CLEAN   ###################
# sudo docker rm deploywith
# sudo docker rmi pyenv:2.0
