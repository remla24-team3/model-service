# model-service

##  Overview

The model-service project is designed for orchestrating prediction requests using a pre-trained model. Leveraging Flask framework, it exposes an API endpoint integrated with Swagger for streamlined documentation. With version control using DVC, automated linting through Pylint, and testing via pytest, the project ensures quality code maintenance. Docker image building and publishing automation through GitHub Actions contribute to a seamless CI/CD pipeline, offering automatic versioning for both packages and releases. 

##  Repository Structure

```sh
└── model-service/
    ├── .github
    │   └── workflows
    ├── LICENSE
    ├── README.md
    ├── dockerfile
    ├── poetry.lock
    ├── pyproject.toml
    └── src
        ├── __init__.py
        └── app.py
```

##  Modules

| File                                                                                        | Summary                                                                                                                                                        |
| ---                                                                                         | ---                                                                                                                                                            |
| [pyproject.toml](https://github.com/remla24-team3/model-service/blob/master/pyproject.toml) | Version control with DVC, API documentation with Flasgger, and quality checks using Pylint and pytest.                                                         |
| [dockerfile](https://github.com/remla24-team3/model-service/blob/master/dockerfile)         | Builds a Python Docker image for the model service. Configures the environment with Poetry package manager. Exposes port 105 and runs the app.py using Poetry. |
| [app.py](https://github.com/remla24-team3/model-service/blob/master/src/app.py) | Orchestrates prediction requests using a pre-trained model.-Utilizes Flask framework to expose API endpoint for predictions.-Integrated with Swagger for API documentation.-Dependencies loaded through `load_model` function. |
| [linting.yml](https://github.com/remla24-team3/model-service/blob/master/.github/workflows/linting.yml)               | Implements automated code linting for the model-service repository. Performs static analysis on codebase to maintain consistent coding standards. Integrated into GitHub Actions workflow for continuous quality checks.                 |
| [docker-publish.yml](https://github.com/remla24-team3/model-service/blob/master/.github/workflows/docker-publish.yml) | Automates Docker image publishing from the model-service repository. Triggers on a merge to the main branch, builds the Docker image, and pushes it to the Docker registry. A critical part of the CI/CD pipeline for the model-service. |

## Usage

To use the model service released package, follow these steps:

(Disclaimer) In order for the commands to work correctly the model should be provided in the app/ folder of the model service. In operation it is added as a volume.

> 1. Pull the latest docker image:
>
> ```console
> $ docker pull ghcr.io/remla24-team3/model-service:latest
> ```
>
> 2. Run the docker container:
> ```console
> $ docker run -p 105:105 ghcr.io/remla24-team3/model-service:latest
> ```
>
> 3. Send a POST request with the input data to:
> ```console
> localhost:105/API/v1.0/predict
> ```
>
> 4. Access Swagger:
> ```console
> localhost:105/apidocs/#/
> ```

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.