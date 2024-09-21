# Social Media API

## Overview

This project is a social media API that allows users to register, authenticate, and interact with the platform. Below are the steps to set up the project, register and authenticate users, and a brief overview of the user model.

## Setup Process

1. **Clone the Repository**

   ```sh
   git clone https://github.com/asmegithub/social_media_api.git
   cd social_media_api
   ```

2. **Install Dependencies**

   ```sh
   pip install -r requirements.txt
   ```

3. **Run Migrations**

   ```sh
   python manage.py migrate
   ```

4. **Start the Server**
   ```sh
   python manage.py runserver
   ```

## User Registration

To register a new user, send a POST request to the `/register/` endpoint with the following JSON payload:

```json
{
  "username": "yourusername",
  "email": "youremail@example.com",
  "password": "yourpassword"
}
```

## User Authentication

To authenticate a user, send a POST request to the `/login/` endpoint with the following JSON payload:

```json
{
  "username": "yourusername",
  "password": "yourpassword"
}
```

The response will include a token that you can use to authenticate subsequent requests.

## User Model Overview

The User model includes the following fields:

- `username`: A unique identifier for the user.
- `email`: The user's email address.
- `password`: A hashed password for secure authentication.
- `date_joined`: The date and time when the user registered.

Additional fields and methods can be added to the User model as needed to support more features.
