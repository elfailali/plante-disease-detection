    # plante-disease-detection

[![Watch the demo video](demo\Recording_demo_app_final.mp4)](demo\Recording_demo_app_final.mp4)


1. Install Python packages
```
pip3 install -r training/requirements.txt
pip3 install -r api/requirements.txt
```

## Setup the frontend app

```bash
cd plant-detection-frontend
npm install --global yarn # if not yet installed
yarn install 
yarn start
```

- Copy `.env.example` as `.env`.
- Change API url in `.env`.

### Using FastAPI

```bash
cd api
```

- Run the FastAPI Server using uvicorn

```bash
uvicorn main:app --reload --host 0.0.0.0
```

- Your API is now running at `0.0.0.0:8000` or localhost:8000

#### hint:  run tf serving image in docker
docker run -t --rm -p 8501:8501 -v C:\Users\Honor\Documents\Projects\Plant-disease-detection:/Plant-disease-detection tensorflow/serving --rest_api_port=8501 --model_config_file=/Plant-disease-detection/models.config



## Run the backend

```bash
cd plants-detection-backend
yarn run nodemon server.js
```

## Contributors

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

- AGDAD Mariam
- DARIF Oussama
- ED-DAOUI Nouha
- EL-AAFANI Hamza
- OUHAMOU Aicha