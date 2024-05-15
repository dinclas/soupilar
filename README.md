## Running the project
* Install dependencies with `pip install -r requirements.txt`
* Start with `uvicorn src.main:app --port 8080`

## Endpoints
After running the project, Swagger will be available on http://localhost:8080/docs
### GET /healthcheck
This endpoint doesn't take any queries/payload and is only useful for automated checks to know if the service is alive.

### POST /vowel_count
#### Payload
The payload must be a json object with a list of words for the vowels to be counted.

* The `words` value must be a list of valid strings
  *  At least one string is required
  *  Strings cannot contain characters with an ASCII code below 0 or above 255
  *  Null values are not permitted 

```json
{
  "words": ["batman", "robin", "coringa"]
}
```
#### Response
The response is a json object in the structure `word: vowels_count`.
```json
{
  "batman": 2,
  "robin": 2,
  "coringa": 3
}
```

### POST /sort
#### Payload
The payload must be a json object with a list of words to be sorted, and the sort orientation.

* The `words` value must be a list of valid strings
  *  At least one string is required
  *  Strings cannot contain characters with an ASCII code below 0 or above 255
  *  Null values are not permitted
* The `order` value must be either "asc" or "desc"
```json
{
  "words": ["batman", "robin", "coringa"],
  "order": "asc"
}
```
#### Response
The response is a json array with the sorted values.
```json
["batman", "coringa", "robin"]
```

# Testing
After installing dependencies, run `pytest`.

# Linter
The linter will run automatically in a pre-commit hook.

# Deployment
Deployment is done using [Kamal](https://kamal-deploy.org).
The process works by building a Docker image(see [Dockerfile](https://github.com/dinclas/soupilar/blob/main/Dockerfile)) and publishing it to Dockerhub. Kamal then accesses the host using SSH, pulls the image and does a zero-downtime deployment.

This repository is configured to deploy whenever a commit is pushed to the main branch and that's done using a GitHub actions workflow that runs the linter([Ruff](https://github.com/astral-sh/ruff)) and tests([Pytest](https://docs.pytest.org/en/8.2.x/)) before deploying.

Deploying requires two credentials: Dockerhub token and the private key to access the host machine. Both are securely stored in this repository secrets.
