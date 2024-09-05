# Project API

## Overview

This Django REST Framework project provides APIs for managing projects, contributors, issues, and comments. The project adheres to clean code practices, including PEP8 compliance and detailed docstrings. Poetry is used for dependency management and packaging.

## Setup

### Installing Dependencies

This project uses Poetry for dependency management. To install the necessary dependencies, run the following commands:

```bash
# Install Poetry if you don't have it already
curl -sSL https://install.python-poetry.org | python3 -

Or 

pip install poetry

# Install project dependencies
poetry install
```

### Running the Project

To start the Django server, use:

```bash
poetry run python manage.py runserver
```

## Authentication

### Register

- **Endpoint**: `POST /api/user/register/`
- **Body**: JSON
  ```json
  {
      "email": "your-email@example.com",
      "user_name": "your_username",
      "password": "your_password"
  }
  ```
- **Response**: JSON
  ```json
  {
      "message": "Account created successfully",
      "user": {
          "email": "your-email@example.com",
          "user_name": "your_username"
      }
  }
  ```

### Login

- **Endpoint**: `POST /api/token/`
- **Body**: JSON
  ```json
  {
      "email": "your-email@example.com",
      "password": "your_password"
  }
  ```
- **Response**: JSON
  ```json
  {
      "refresh": "your_refresh_token",
      "access": "your_access_token"
  }
  ```

## Endpoints

### Projects

#### Get All Projects

- **URL:** `/api/projects/`
- **Method:** GET
- **Permissions:** Authenticated users
- **Description:** Retrieve all projects visible to the authenticated user.

#### Create Project

- **URL:** `/api/projects/`
- **Method:** POST
- **Permissions:** Authenticated users
- **Description:** Create a new project.
- **Data:**
  ```json
  {
      "name": "Project Name 2",
      "description": "Project Description",
      "type": "BE"
  }
  ```

#### Get Project Details

- **URL:** `/api/projects/{project_id}/`
- **Method:** GET
- **Permissions:** Authenticated users
- **Description:** Retrieve details of a specific project.

#### Update Project

- **URL:** `/api/projects/{project_id}/`
- **Method:** PUT
- **Permissions:** Owner or read-only
- **Description:** Update details of a specific project.
- **Data:**
  ```json
  {
      "name": "Project Name 2 Updated",
      "description": "Updated Project Description",
      "type": "FE"
  }
  ```

#### Delete Project

- **URL:** `/api/projects/{project_id}/`
- **Method:** DELETE
- **Permissions:** Owner or read-only
- **Description:** Delete a specific project.

### Contributors

#### Get All Contributors

- **URL:** `/api/contributors/`
- **Method:** GET
- **Permissions:** Authenticated users
- **Description:** Retrieve all contributors.

#### Add Contributor

- **URL:** `/api/contributors/`
- **Method:** POST
- **Permissions:** Authenticated users
- **Description:** Add a new contributor to a project.
- **Data:**
  ```json
  {
      "user": 2,
      "project": 1
  }
  ```

#### Get Contributor Details

- **URL:** `/api/contributors/{contributor_id}/`
- **Method:** GET
- **Permissions:** Authenticated users
- **Description:** Retrieve details of a specific contributor.

#### Update Contributor

- **URL:** `/api/contributors/{contributor_id}/`
- **Method:** PUT
- **Permissions:** Owner or read-only
- **Description:** Update details of a specific contributor.
- **Data:**
  ```json
  {
      "user": 2,
      "project": 1
  }
  ```

#### Remove Contributor

- **URL:** `/api/contributors/{contributor_id}/`
- **Method:** DELETE
- **Permissions:** Owner or read-only
- **Description:** Remove a specific contributor from a project.

### Issues

#### Get All Issues

- **URL:** `/api/issues/`
- **Method:** GET
- **Permissions:** Authenticated users
- **Description:** Retrieve all issues visible to the authenticated user.

#### Create Issue

- **URL:** `/api/issues/`
- **Method:** POST
- **Permissions:** Authenticated users
- **Description:** Create a new issue.
- **Data:**
  ```json
  {
      "title": "Issue Title",
      "description": "Issue Description",
      "priority": "LOW",
      "tag": "TASK",
      "status": "TODO",
      "assignee": "1",
      "project": 1
  }
  ```

#### Get Issue Details

- **URL:** `/api/issues/{issue_id}/`
- **Method:** GET
- **Permissions:** Authenticated users
- **Description:** Retrieve details of a specific issue.

#### Update Issue

- **URL:** `/api/issues/{issue_id}/`
- **Method:** PUT
- **Permissions:** Owner or read-only
- **Description:** Update details of a specific issue.
- **Data:**
  ```json
  {
      "title": "Updated Issue Title",
      "description": "Updated Issue Description",
      "priority": "HIGH",
      "tag": "BUG",
      "status": "IN_PROGRESS",
      "assignee": 2,
      "project": 1
  }
  ```

#### Delete Issue

- **URL:** `/api/issues/{issue_id}/`
- **Method:** DELETE
- **Permissions:** Owner or read-only
- **Description:** Delete a specific issue.

### Comments

#### Get All Comments

- **URL:** `/api/comments/`
- **Method:** GET
- **Permissions:** Authenticated users
- **Description:** Retrieve all comments visible to the authenticated user.

#### Create Comment

- **URL:** `/api/comments/`
- **Method:** POST
- **Permissions:** Authenticated users
- **Description:** Create a new comment.
- **Data:**
  ```json
  {
      "description": "Comment text",
      "issue": "1"
  }
  ```

#### Get Comment Details

- **URL:** `/api/comments/{comment_id}/`
- **Method:** GET
- **Permissions:** Authenticated users
- **Description:** Retrieve details of a specific comment.

#### Update Comment

- **URL:** `/api/comments/{comment_id}/`
- **Method:** PUT
- **Permissions:** Owner or read-only
- **Description:** Update details of a specific comment.
- **Data:**
  ```json
  {
      "description": "Updated Comment Description",
      "issue": 19
  }
  ```

#### Delete Comment

- **URL:** `/api/comments/{comment_id}/`
- **Method:** DELETE
- **Permissions:** Owner or read-only
- **Description:** Delete a specific comment.

---

### Clean Code Standards

To ensure clean code, all Python files in this project should follow these guidelines:

1. **PEP8 Compliance**: All Python code should adhere to the PEP8 style guide. Use tools like `flake8` or `black` to check your code.
2. **Docstrings**: Each class and method should have a clear and concise docstring explaining its purpose and behavior.

### Example Docstring Format

```python
class CustomUserCreate(APIView):
    """
    API view for creating a new user.

    Methods:
    -------
    post(request):
        Handles POST requests to create a new user.
    """
    
    permission_classes = [AllowAny]

    def post(self, request):
        """
        Handles the creation of a new user.

        Parameters:
        ----------
        request : Request
            The incoming request containing user data.

        Returns:
        -------
        Response
            A response with a success message and the new user details or an error message.
        """
        reg_serializer = RegisterUserSerializer(data=request.data)
        if reg_serializer.is_valid():
            age = request.data.get('age')
            consent = request.data.get('consent')

            if int(age) < 18 or consent not in ['compactable', 'shareable']:
                return Response({"error": "Invalid age or consent rules."}, status=status.HTTP_400_BAD_REQUEST)

            newuser = reg_serializer.save()
            if newuser:
                return Response({
                    "message": "Account created successfully",
                    "user": {
                        "email": newuser.email,
                        "user_name": newuser.user_name,
                    }
                }, status=status.HTTP_201_CREATED)
        return Response(reg_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
```