# Flask CRUD API for Managing People

  This is a simple Flask application for performing CRUD (Create, Read, Update, Delete) operations on a database of people. The application uses SQLite as its database, and it provides a RESTful API to interact with the data.

## Setup

  Before running the application, make sure you have Python and Flask installed on your system. You can install Flask using pip:

  ```bash
  pip install Flask
  ```

## Database Configuration

  The application uses an SQLite database named `people.db`. You can configure the database URI in the following line of code in the `app.py` file:

  ```python
  app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///people.db'  # SQLite database file
  ```

  To create the database and tables, you can uncomment the following lines in the `app.py` file:

  ```python
  # Create the database and tables
  # with app.app_context():
  #     db.create_all()
  ```

  This will create the necessary tables for storing person data.

## Running the Application

  You can run the Flask application by executing the `app.py` file:

  ```bash
  python app.py
  ```

  By default, the application runs in debug mode, which is suitable for development. You can access the API at `http://localhost:5000`.

## Endpoints
  
### Create a New Person
  - **Endpoint**: `/person` (POST)
  - **Description**: Add a new person to the database.
  - **Example Request Body**:
  ```json
  {
    "full_name": "John Doe",
    "age": 30,
    "address": "123 Main St"
  }
  ```

### Read All People
  - **Endpoint**: `/people` (GET)
  - **Description**: Retrieve a list of all people in the database.

### Read a Single Person by ID
  - **Endpoint**: `/person/<int:id>` (GET)
  - **Description**: Retrieve a person's details by their unique ID.

### Update a Person by ID
  - **Endpoint**: `/person/<int:id>` (PUT)
  - **Description**: Update a person's information by their ID.
  - **Example Request Body**:
    ```json
    {
      "full_name": "Updated Name",
      "age": 35,
      "address": "456 Elm St"
    }
    ```

### Delete a Person by ID
  - **Endpoint**: `/person/<int:id>` (DELETE)
  - **Description**: Delete a person from the database by their ID.

## Testing

  You can use tools like Thunder Client to test the API endpoints. Make sure to set the appropriate HTTP method and request body for each endpoint you want to test.

## Note

  This application is intended for educational purposes and may require additional security measures if used in a production environment. Consider adding authentication and authorization mechanisms to protect the API endpoints in a real-world scenario.
