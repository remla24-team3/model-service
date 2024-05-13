# model-service

This is a project that provides a model service for machine learning models.

## Usage

To use the model service, follow these steps:

1. Pull the latest docker image: `docker pull ghcr.io/remla24-team3/model-service:latest`
2. Run the docker container: `docker run -p 105:105 ghcr.io/remla24-team3/model-service:latest`
3. Send a POST request to `localhost:105/API/v1.0/predict` with the input data to get predictions.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.