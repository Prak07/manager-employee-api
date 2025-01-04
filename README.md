# Manager-Employee API

The Manager-Employee API is a RESTful web service designed to manage organizational data, focusing on employees and their managers. This API allows for creating, reading, updating, and deleting (CRUD) operations for both managers and employees. The API includes a feature that allows employees to self-select their managers.

## Features

- **Employee Management**:
  - Add, view, update, and delete employee records.
  - Employees can select their managers.

- **Manager Management**:
  - Add, view, update, and delete manager records.

- **Relational Data**:
  - Establish and manage relationships between managers and employees.

- **Public API**:
  - No authentication required for accessing the API.

- **Documentation**:
  - API documentation is provided using Swagger.

- **Deployment**:
  - Hosted on a public URL for accessibility.

## Prerequisites

Before running the project, ensure the following are installed:

- **Python**: Version 3.8 or above.
- **Django**: Version 3.2 or above.
- **Django REST Framework (DRF)**: For building RESTful APIs.

## Technologies Used

- **Backend**: Django, Django REST Framework (DRF)
- **Database**: SQLite (default) or any other relational database (e.g., PostgreSQL, MySQL)
- **Documentation**: Swagger for API exploration and testing
- **Hosting**: Deployed on a public server (accessible at [http:///swagger/](http://4.188.79.171/swagger/)).

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/manager-employee-api.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd manager-employee-api
   ```

3. **Set up a Virtual Environment**:
   ```bash
   python -m venv env
   source env/bin/activate  # On Windows: .\env\Scripts\activate
   ```

4. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run Database Migrations**:
   ```bash
   python manage.py migrate
   ```

6. **Start the Development Server**:
   ```bash
   python manage.py runserver
   ```

7. **Access API Documentation**:
   Visit `http://127.0.0.1:8000/swagger/` for Swagger documentation.

## API Endpoints

### Managers
- `GET /managers/` - List all managers.
- `POST /managers/` - Add a new manager.
- `GET /managers/{id}/` - Retrieve a specific manager by ID.
- `PUT /managers/{id}/` - Update a specific manager by ID.
- `DELETE /managers/{id}/` - Delete a specific manager by ID.

### Employees
- `GET /employees/` - List all employees.
- `POST /employees/` - Add a new employee.
- `GET /employees/{id}/` - Retrieve a specific employee by ID.
- `PUT /employees/{id}/` - Update a specific employee by ID.
- `DELETE /employees/{id}/` - Delete a specific employee by ID.
- `PATCH /employees/{id}/assign-manager/` - Assign or update a manager for the employee.

## Assumptions

- Each employee must be assigned to exactly one manager.
- Managers can have multiple employees reporting to them.
- No authentication or role-based access control is implemented as this is a public API.

## Contributions

This project was solely developed by **Prakhar Agarwal**, who implemented the API logic, designed the database schema, and documented the endpoints.


