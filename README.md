# RESTful API web server dockerized on Python

This is a basic Hello-Wolrd appplication.

## Requirements

It is assumed you have Linux OS, but you can run this project in Windows or MacOS also, just use the alternative  lines commands.

**Linux**

- `Docker` installed
- `docker-compose` installed
- Any rest consumer application like `Postman` installed or any plugin REST client in any browser (like "Advanced REST client" in Chrome )

## Set up

Running in linux console.

### Prepare

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
sudo docker rm deploywith && sudo docker rmi pyenv:2.0
```

Run the following command to remove what we name the base image.

```bash
sudo docker rmi pyenv:1.0
```

## Tutorial

You can find a tutorial of this project in the following site.

[https://federicozacayan.github.io/tutorial/restful-api-python/](https://federicozacayan.github.io/tutorial/restful-api-python/)

## Usage

All the responses have `ContentType application/json` header.

### List all products

**Definition**

`GET /produc`

**Response**

- `200 OK` on success.

```json
{
  "product": [
    {
      "id": 1,
      "name": "Federico Zacayan"
    },
    {
      "id": 2,
      "name": "Software Developer"
    }
  ],
  "q": 2
}
```

### Registering a new product

**Definition**

`POST /product`

**Arguments**

- `"name":string` a friendly name for this product.

**Response**

- `201 Created` on success.

```json
{
  "status": 201
}
```

## Lookup product details

`GET /product/<identifier>`

**Response**

- `200 OK` on success.

```json
{
  "id": 1,
  "name": "Federico Zacayan"
}
```

## Delete a product

**Definition**

`DELETE /product/<identifier>`

**Response**

- `500 Internal Error` if the product does not exist.
- `200 No Content` on success.
```json
{
  "status": "200"
}
