# Employee Management System (Streamlit and MySQL)

Welcome to the Employee Management System, a web-based application built with Streamlit and MySQL for managing employee records. This README provides information on how to set up and run the system.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

Before getting started, make sure you have the following installed on your system:

- Python (3.6 or later)
- MySQL server
- pip (Python package manager)

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/employee-management-system.git
cd employee-management-system
```

2. Create a virtual environment (optional but recommended):

```bash
python -m venv venv
```

3. Activate the virtual environment:

   - On Windows:

   ```bash
   venv\Scripts\activate
   ```

   - On macOS and Linux:

   ```bash
   source venv/bin/activate
   ```

4. Install the required Python packages:

```bash
pip install -r requirements.txt
```

## Configuration

1. Create a MySQL database for the Employee Management System.

2. Update the database connection details in the `config.py` file.

```python
# config.py
DB_HOST = "localhost"
DB_USER = "your_db_user"
DB_PASSWORD = "your_db_password"
DB_NAME = "employee_management"
```

3. Initialize the database tables by running the following command:

```bash
python init_db.py
```

## Usage

To run the Employee Management System, use the following command:

```bash
python -m streamlit run home.py
```

This will start the Streamlit web application, and you can access it in your web browser by visiting `http://localhost:8501`.

## Contributing

We welcome contributions to this project. If you would like to contribute, please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Feel free to customize this README to include more specific information about your project, its features, and any other relevant details.
