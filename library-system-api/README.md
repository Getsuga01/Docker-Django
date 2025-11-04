# Library System API

This project is a Django REST API for managing a library system. It provides CRUD operations for resources such as Books, Authors, and Loans.

## Features

- Manage Books: Create, Read, Update, and Delete book records.
- Manage Authors: Create, Read, Update, and Delete author records.
- Manage Loans: Create, Read, Update, and Delete loan records.

## Technologies Used

- Django
- Django REST Framework
- Docker

## Getting Started

### Prerequisites

- Docker
- Docker Compose

### Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd library-system-api
   ```

2. Build and run the Docker containers:
   ```
   docker-compose up --build
   ```

3. Access the API at `http://localhost:8000/api/`.

### Running Tests

To run the tests, execute the following command inside the Docker container:
```
docker-compose exec web python manage.py test
```

## API Endpoints

- **Books**
  - `GET /api/books/` - List all books
  - `POST /api/books/` - Create a new book
  - `GET /api/books/{id}/` - Retrieve a specific book
  - `PUT /api/books/{id}/` - Update a specific book
  - `DELETE /api/books/{id}/` - Delete a specific book

- **Authors**
  - `GET /api/authors/` - List all authors
  - `POST /api/authors/` - Create a new author
  - `GET /api/authors/{id}/` - Retrieve a specific author
  - `PUT /api/authors/{id}/` - Update a specific author
  - `DELETE /api/authors/{id}/` - Delete a specific author

- **Loans**
  - `GET /api/loans/` - List all loans
  - `POST /api/loans/` - Create a new loan
  - `GET /api/loans/{id}/` - Retrieve a specific loan
  - `PUT /api/loans/{id}/` - Update a specific loan
  - `DELETE /api/loans/{id}/` - Delete a specific loan

## License

This project is licensed under the MIT License.