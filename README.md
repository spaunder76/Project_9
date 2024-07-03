# Project API

## Overview

This Django REST Framework project provides APIs for managing projects, contributors, issues, and comments.

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
- **Description:** Update details of a specific issue.
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
