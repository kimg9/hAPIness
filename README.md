# hAPIness

## API Objective

The goal of this API is to provide a high-performance and secure back-end solution for creating and tracking technical issues. This API will serve as the foundation for front-end applications on various platforms (web, mobile, etc.), enabling users to report technical issues, track their resolution, and manage associated tickets.

## Local Installation

### Environment Variables to Configure

```bash
export SECRET_KEY="your_secret_key_here"
export DEBUG="False"  # This application is not yet ready for production deployment
export DATABASE_ENGINE="django.db.backends.postgresql"
export DATABASE_NAME="your_database_name_here"
```

## Using the API

### Available Endpoints

- **USERS**
  - `GET /api/user/`
  - `POST /api/user/`
  - `GET /api/user/{id}/`
  - `PUT /api/user/{id}/`
  - `DELETE /api/user/{id}/`

- **PROJECTS**
  - `GET /api/project/`
  - `POST /api/project/`
  - `GET /api/project/{id}/`
  - `PUT /api/project/{id}/`
  - `DELETE /api/project/{id}/`

- **ISSUES**
  - `GET /api/issue/`
  - `POST /api/issue/`
  - `GET /api/issue/{id}/`
  - `PUT /api/issue/{id}/`
  - `DELETE /api/issue/{id}/`

- **COMMENTS**
  - `GET /api/comment/`
  - `POST /api/comment/`
  - `GET /api/comment/{id}/`
  - `PUT /api/comment/{id}/`
  - `DELETE /api/comment/{id}/`

- **Authentication**
  - `POST /api/token/` : JWT Token
  - `POST /api/token/refresh/` : Refresh JWT Token