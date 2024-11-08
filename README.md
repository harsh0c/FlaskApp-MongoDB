# Flask CRUD Application for User Management

This is a Flask-based REST API that performs **CRUD** (Create, Read, Update, Delete) operations on a MongoDB database for managing a **User** resource. The application includes REST API endpoints to handle user management, including creating, reading, updating, and deleting user records.

## Table of Contents
- [Technologies Used](#technologies-used)
- [Features](#features)
- [Setup Instructions](#setup-instructions)
  - [Using Docker](#using-docker)
  - [Running Locally without Docker](#running-locally-without-docker)
- [API Endpoints](#api-endpoints)
- [Testing with Postman](#testing-with-postman)


## Technologies Used

- **Flask** - A Python web framework for building the REST API.
- **MongoDB** - NoSQL database for storing user data.
- **Flask-PyMongo** - MongoDB integration for Flask.
- **Docker** - Containerization tool to run the application.
- **Postman** - For testing and validating the API.

## Features

- **Create a User**: Add new users with name, email, and password.
- **Read Users**: Fetch all users or a specific user by ID.
- **Update User**: Update a user’s information.
- **Delete User**: Remove a user from the database.
- **MongoDB Integration**: Uses MongoDB to persist user data.
- **Containerized with Docker**: The application is Dockerized for easy deployment and consistency across different environments.

## Setup Instructions

### Using Docker

1. **Clone the repository**:
   ```bash
   git clone https://github.com/harsh0c/FlaskApp-MongoDB
   cd FlaskApp-MongoDB
2. **Build and run the Docker containers**:
    To build and start the application, run the following command:
    ```bash
    docker-compose up --build
3. **Access the application**:
The application will be accessible at http://localhost:5001.
MongoDB will be running inside a Docker container and accessible on the same network.

4. **Stop the containers**:
    To stop the containers, run:
    ```bash
    docker-compose down

### Running locally without docker
1. **Clone the repository:**
    ```bash
    git clone https://github.com/harsh0c/FlaskApp-MongoDB
    cd FlaskApp-MongoDB

2. **Set up a virtual environment:**
    ```bash
    python3 -m venv venv
    source venv/bin/activate
3. **Install dependencies:**
    ```bash
    pip install -r requirements.txt
4. **Set up MongoDB**:
- Ensure you have MongoDB running locally or use a cloud MongoDB service (e.g., MongoDB Atlas).
-   Update the MONGO_URI in config.py to point to your MongoDB instance.

5. **Run the application**:
    ```bash
    python run.py
6. **Access the application**:
The app will be running at http://localhost:5001

## API Endpoints

### `GET /users - Returns a list of all users.`
- **Example request**:
  
  ```bash
  curl http://localhost:50001/users
### `GET /users/<id> - Returns a user by ID.`
- **Example request**:
  
  ```bash
  curl http://localhost:5001/users/672e2144269d97a47d283ecd
### `POST /users - Creates a new user.`
- **Example request body**:
  
  ```json
  {
    "name": "Harsh",
    "email": "harsh@example.com",
    "password": "password123"
  }

### `PUT /users/<id> - Updates a user by ID.`
- **Example request**:
  
  ```json
  {
    "name": "Harsh Chandra",
    "email": "harsh.updated@example.com"
  }
### `DELETE /users/<id> - Deletes a user by ID.`


### Testing with Postman
1. Import Postman Collection:
- Import the flask-mongodb.postman_collection.json file located in the repository into Postman.
- This collection includes all the pre-configured API requests for testing the CRUD operations.

2. Send requests:
- Use Postman to test each endpoint by sending GET, POST, PUT, and DELETE requests and verify the correct responses.