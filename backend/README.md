# Containerized Selenium API

The main objective of this repository was to deploy a Docker container with
both, FastAPI and Selenium, to check the possibilities when we try to use
FastAPI to receive parameters, and run a selenium process in the background
to gather and parse data. But some issues occured in the google cloud run about permissions. So beautiful soup is used insted.

- functions can be triggered with [fast api  running in gcp](https://sociality4-sl6b2mo6eq-uc.a.run.app/docs).