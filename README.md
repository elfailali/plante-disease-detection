    # plante-disease-detection

[![Watch the demo video](\demo\Recording_demo_app_final.mp4)](\demo\Recording_demo_app_final.mp4)


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