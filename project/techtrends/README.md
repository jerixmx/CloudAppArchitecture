# TechTrends Web Application

TechTrends is a news sharing platform where users can access, create, and share news within the cloud-native ecosystem.


https://user-images.githubusercontent.com/78225194/132833632-584c18ac-1b01-4a53-a041-0b4f4564f992.mp4



## Project Specifications
1. Health checking via the `/healthz` endpoint
2. Metrics access via the `/metrics` endpoint which returns the number of posts and database connections
3. DEBUG level logging in STDOUT & STDERR of the following events:
    1. Accessing an article
    2. Accessing the About page
    3. Creation of a new article
    4. Errors from accessing non-existing article
4. Docker created container images pushed to [Docker Hub](https://hub.docker.com/repository/docker/jerixmx/techtrends)
5. Continuous Integration (CI) by GitHub Actions that constructs a new image with every new commit to specified project branches
6. Declarative Kubernetes deployment
7. Continuous Delivery by ArgoCD and Helm to staging and production environments

## Tech Used
1. Flask
2. Docker
3. GitHub Actions
4. Helm
5. Kubernetes
6. ArgoCD

## Run 
1. Run `python init_db.py` to initialize the posts database.
    - This will create or overwrite the `database.db` file that is used by the web application.
2.  Run `python app.py` to launch the TechTrends application.
    - The application runs on port `3111` and can be accessed by querying the `http://127.0.0.1:3111/` endpoint.
