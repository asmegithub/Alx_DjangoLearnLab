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

## API Endpoints Overview

## Post Endpoints

### 1. Create a Post

- **Endpoint**: `POST /posts/`
- **Description**: Creates a new post.
- **Request Headers**:
  - `Authorization`: Bearer token obtained during user authentication.
- **Request Body**:

  ```json
  {
    "title": "Post Title",
    "content": "This is the content of the post."
  }
  ```

  ## this is what the response look like

```json
{
  "id": 1,
  "title": "Post Title",
  "content": "This is the content of the post.",
  "author": "yourusername",
  "created_at": "2024-09-28T08:20:53.957660Z",
  "updated_at": "2024-09-28T08:20:53.957701Z"
}
```

### 2. Retrieve a Post

- **Endpoint**: `GET /posts/{id}/`
- **Description**: Retrieves a post by its ID.
- **Request Headers**:
  - `Authorization`: Bearer token obtained during user authentication.
- **Response Body**:

```json
{
  "id": 1,
  "title": "My first post",
  "content": "Hey family this is my first post in my own social media",
  "author": "new-3",
  "comments": [
    {
      "id": 1,
      "content": "wow, welcome boss!\r\n\r\nMay this media be among the largest social medias in the world!",
      "post": 1,
      "author": "new-3",
      "created_at": "2024-09-28T08:40:33.065621Z",
      "updated_at": "2024-09-28T08:40:33.065650Z"
    }
  ],
  "created_at": "2024-09-28T08:20:53.957660Z",
  "updated_at": "2024-09-28T08:20:53.957701Z"
}
```

### 3. Update a Post

- **Endpoint**: `PUT /posts/{id}/`
- **Description**: Updates an existing post.
- **Request Headers**:
  - `Authorization`: Bearer token obtained during user authentication.
- **Request Body**:

  ```json
  {
    "title": "Updated Post Title",
    "content": "This is the updated content of the post."
  }
  ```

- **Response Body**:

  ```json
  {
    "id": 1,
    "title": "Updated Post Title",
    "content": "This is the updated content of the post.",
    "author": "yourusername",
    "created_at": "2024-09-28T08:20:53.957660Z",
    "updated_at": "2024-09-28T09:20:53.957701Z"
  }
  ```

### 4. Delete a Post

- **Endpoint**: `DELETE /posts/{id}/`
- **Description**: Deletes a post by its ID.
- **Request Headers**:
  - `Authorization`: Bearer token obtained during user authentication.
- **Response Body**:

  ```json
  {
    "detail": "Post deleted successfully."
  }
  ```

### 5. List All Posts

- **Endpoint**: `GET /posts/`
- **Description**: Retrieves a list of all posts.
- **Request Headers**:
  - `Authorization`: Bearer token obtained during user authentication.
- **Response Body**:

  ```json
  [
    {
      "id": 1,
      "title": "Post Title",
      "content": "This is the content of the post.",
      "author": "yourusername",
      "created_at": "2024-09-28T08:20:53.957660Z",
      "updated_at": "2024-09-28T08:20:53.957701Z"
    },
    {
      "id": 2,
      "title": "Another Post Title",
      "content": "This is the content of another post.",
      "author": "anotherusername",
      "created_at": "2024-09-29T10:15:30.123456Z",
      "updated_at": "2024-09-29T10:15:30.123456Z"
    }
  ]
  ```

```

```

##

## Follow Management

### 1. Follow a User

- **Endpoint**: `GET /follow/<user_id:int>`
- **Description**: Follow another user.
- **Request Headers**:
  - `Authorization`: Bearer token obtained during user authentication.
- **Request Body**:

  ```json
  {
    "target_user_id": 2
  }
  ```

- **Response Body**:

  ```json
  {
    "detail": "You are now following the user."
  }
  ```

### 2. Unfollow a User

- **Endpoint**: `DELETE /unfollow/`
- **Description**: Unfollow a user.
- **Request Headers**:
  - `Authorization`: Bearer token obtained during user authentication.
- **Request Body**:

  ```json
  {
    "target_user_id": 2
  }
  ```

- **Response Body**:

  ```json
  {
    "detail": "You have unfollowed the user."
  }
  ```

### 3. List Followers

- **Endpoint**: `GET /followers/`
- **Description**: Retrieve a list of users who follow the authenticated user.
- **Request Headers**:
  - `Authorization`: Bearer token obtained during user authentication.
- **Response Body**:

  ```json
  [
    {
      "id": 1,
      "username": "follower1",
      "email": "follower1@example.com"
    },
    {
      "id": 2,
      "username": "follower2",
      "email": "follower2@example.com"
    }
  ]
  ```

### 4. List Following

- **Endpoint**: `GET /following/`
- **Description**: Retrieve a list of users that the authenticated user is following.
- **Request Headers**:
  - `Authorization`: Bearer token obtained during user authentication.
- **Response Body**:

  ```json
  [
    {
      "id": 3,
      "username": "following1",
      "email": "following1@example.com"
    },
    {
      "id": 4,
      "username": "following2",
      "email": "following2@example.com"
    }
  ]
  ```

  ## Follow/Unfollow Users

  ### 1. Follow User

  - **Endpoint**: `GET /follow/<user_id>/`
  - **Description**: Follow a user specified by `user_id`.
  - **Request Headers**:
    - `Authorization`: Bearer token obtained during user authentication.
  - **Response Body**:

    - `status`: Confirmation message indicating the user has been followed.

    ```json
    {
      "status": "you followed <username> !"
    }
    ```

  ### 2. Unfollow User

  - **Endpoint**: `GET /unfollow/<user_id>/`
  - **Description**: Unfollow a user specified by `user_id`.
  - **Request Headers**:
    - `Authorization`: Bearer token obtained during user authentication.
  - **Response Body**:

    - `status`: Confirmation message indicating the user has been unfollowed.

    ```json
    {
      "status": "You unfollowed <username> !"
    }
    ```

## Feed Access

### 1. Retrieve Feed

- **Endpoint**: `GET /feeds/`
- **Description**: Retrieve posts from users that the authenticated user is following.
- **Request Headers**:
  - `Authorization`: Bearer token obtained during user authentication.
- **Response Body**:

  ```json
  [
    {
      "id": 1,
      "title": "Post Title",
      "content": "This is the content of the post.",
      "author": "following1",
      "created_at": "2024-09-28T08:20:53.957660Z",
      "updated_at": "2024-09-28T08:20:53.957701Z"
    },
    {
      "id": 2,
      "title": "Another Post Title",
      "content": "This is the content of another post.",
      "author": "following2",
      "created_at": "2024-09-29T10:15:30.123456Z",
      "updated_at": "2024-09-29T10:15:30.123456Z"
    }
  ]
  ```

## User Model Changes

The User model has been updated to include the following fields:

- `followers`: A many-to-many relationship to represent users who follow this user.
- `following`: A many-to-many relationship to represent users that this user is following.

These fields allow for efficient management of follow relationships and feed generation.
