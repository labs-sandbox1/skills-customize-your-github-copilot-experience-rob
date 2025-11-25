# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objective

Learn how to build and deploy RESTful APIs using the FastAPI framework in Python. Students will create a simple API for managing resources, practice CRUD operations, and understand API documentation and testing.

## 📝 Tasks

### 🛠️ Task 1: Set Up FastAPI Project

#### Description
Initialize a new FastAPI project and create a basic API endpoint that returns a welcome message.

#### Requirements
Completed program should:
- Use FastAPI to create a web server
- Provide a root endpoint (`/`) that returns a JSON welcome message
- Run locally on port 8000

### 🛠️ Task 2: Implement CRUD Endpoints

#### Description
Create RESTful endpoints to manage a collection of items (e.g., books, tasks, or users). Implement Create, Read, Update, and Delete operations.

#### Requirements
Completed program should:
- Define a data model using Pydantic
- Implement endpoints for:
  - Creating a new item
  - Retrieving all items
  - Retrieving a single item by ID
  - Updating an item by ID
  - Deleting an item by ID
- Return appropriate HTTP status codes and error messages

### 🛠️ Task 3: API Documentation and Testing

#### Description
Explore FastAPI's automatic documentation and test your endpoints using Swagger UI.

#### Requirements
Completed program should:
- Provide interactive API docs at `/docs`
- Include example requests and responses in the documentation
- Test all endpoints using Swagger UI

---

**Tip:** Use clear variable names and comments to make your code easy to understand. Refer to the FastAPI documentation for help: https://fastapi.tiangolo.com/
