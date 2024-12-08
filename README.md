# Library Management System

## How to run the project

1. Clone the repository.
2. Install dependencies: `pip install -r requirements.txt`.
3. Run the Flask app: `python run.py`.
4. Access the API at `http://127.0.0.1:5000`.

## Design Choices

- Used Python classes to represent books and members.
- The application uses a simple in-memory list to store books and members. No database was used for this submission.
- The application provides basic CRUD functionality for both books and members.

## Assumptions and Limitations

- This implementation does not persist data between server restarts.
- Authentication and advanced features like pagination are optional and could be added later.
