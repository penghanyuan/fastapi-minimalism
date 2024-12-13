# FastAPI project template

Template Structure 
-----------------

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

