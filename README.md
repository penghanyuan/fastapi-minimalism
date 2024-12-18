# FastAPI project template

## Getting Started

### Prerequisites

- Python 3.8 or higher
- [Poetry](https://python-poetry.org/) for dependency management (optional)

### Installation

1. **Clone the repository:**

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Create a virtual environment:**

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

   Alternatively, if using Poetry:

   ```bash
   poetry install
   ```

### Running the Application

To start the FastAPI application, run:

```bash
uvicorn src.main:app --reload
```


The application will be available at `http://localhost:8000`.

### Project Configuration

The project uses a `pyproject.toml` file for configuration, which includes dependencies and project metadata. You can modify this file to add or update dependencies.

### Testing

To run the tests, use:

```bash
pytest
```


### Code Style

The project uses `black`, `flake8`, and `isort` for code styling. You can run these tools using the Makefile:

```bash
make style
```

### Directory Structure

- **`src/app/api`**: Contains the API endpoints, including the main API and health check endpoints.
- **`src/app/core`**: Core components of the application, such as configuration and event handlers.
- **`src/app/services`**: Service layer that interfaces between the API and processing logic.
- **`src/main.py`**: The entry point of the application.
- **`tests`**: Contains test configurations and test cases for the API.

### License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

### Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

### Acknowledgments

This template is inspired by best practices for structuring FastAPI projects and aims to provide a solid foundation for building scalable applications.


### Project Structure

```
.
├── Makefile                                                <- contains commands for clean and style
├── README.md                                               <- project overview, including what it does, how to set up and use it
├── cli                                                     <- command-line interface scripts or tools (for production)
├── install                                                 <- installation scripts or instructions (for production)
├── data
│   ├── 01_raw                                              <- original unmodified data acting as source of truth and provenance
│   ├── 02_interim                                          <- data in intermediate processing stage
│   └── 03_processed                                        <- data after all preprocessing has been done
├── notebooks                                               <- Jupyter notebooks for exploratory analysis and explanation
├── pyproject.toml                                          <- project configuration file, including dependencies and project metadata
├── requirements.txt                                        <- list of Python dependencies required for the project
├── src
│   ├── app                                                 <- FastAPI application code
│   │   ├── api                                                 <- API-related code
│   │   │   ├── api.py                                              <- main API endpoints
│   │   │   └── heartbeat.py                                        <- API health check endpoints
│   │   ├── core                                                <- core application components
│   │   │   ├── config.py                                           <- application configuration
│   │   │   └── event_handler.py                                    <- event handling logic
│   │   └── services                                            <- service layer code
│   │       └── {{cookiecutter.project_slug}}_services.py           <- interface layer between api and processing logic
│   ├── main.py                                             <- entry point of the application
│   ├── ui                                                  <- user interface code (python)
│   └── {{cookiecutter.project_slug}}                       <- application functionalities
│       └── utils.py                                                <- utility functions
└── tests                                                   <- test suite
    ├── conftest.py                                             <- configuration for tests
    └── test_api.py                                             <- tests for the API

```

