# RESTful API web server dockerized on Python

This is a basic Hello-Wolrd appplication.

## Requirements

**Linux**

- `Docker` installed
- `docker-compose` installed
- Any browser like `Chrome` or any rest consumer application like `Postman` installed

## Usage

Running in linux console.

### Set up

Clone this repository.

```bash
git clone https://github.com/federicozacayan/restful-api-python.git
```
Run the following command in the the docpyenv folder.

```bash
sudo docker build -t pyenv:1.0 .
```

### Run

Run the following command in the  the root folder.

```bash
sudo docker build -t pyenv:2.0 . && sudo docker run -p 5000:5000 --name deploywith pyenv:2.0
```

### Stop

Press `CTRL+C` on the console.

### Clean your disk

Run the following command to remove the container first and his image after.

```bash
sudo docker rm python-project_api_1 && sudo docker rmi python-project_api
```

Run the following command to remove what we name the base image.

```bash
sudo docker rmi pyenv:1.0
```

## Tutorial

You can find a tutorial of this project in the following site.

[https://federicozacayan.github.io/tutorial/restful-api-python/](https://federicozacayan.github.io/tutorial/restful-api-python/)

