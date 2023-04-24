# Introduction

In the wake of the COVID-19 pandemic, tracking the progress of vaccination campaigns has become crucial in understanding our collective journey towards a safer, healthier world. The Global Vaccination Tracker is a web-based application designed to provide an intuitive visualization of worldwide vaccination coverage. By leveraging the power of geolocation maps and data from the World Health Organization (WHO), our platform presents a comprehensive and accessible snapshot of vaccination distribution across the globe.

Built using cutting-edge technologies such as Django, SQLite, HTML, CSS, and ArcGIS, the Global Vaccination Tracker aims to make complex data more understandable and engaging for users. The project's integration with the WHO's vaccination dataset ensures that the information presented is both accurate and up-to-date, allowing individuals, organizations, and governments to make well-informed decisions based on the latest trends.

Our interactive geolocation map enables users to explore vaccination data on a global scale, as well as to zoom in on specific countries. This level of granularity provides valuable insights into the successes and challenges faced by different communities, fostering greater awareness and collaboration in the ongoing effort to protect the world's population against infectious diseases.

The Global Vaccination Tracker not only serves as an informative tool for policymakers, healthcare professionals, and the general public, but also stands as a testament to human resilience and ingenuity in the face of adversity. By harnessing the power of data visualization, we hope to inspire collective action and contribute to a brighter, healthier future for all.

# Installation Instructions
## Using Docker

1. Build the docker image
```bash
cd /path/to/this/folder
docker build -t immunization .
```
2. Run the image
```bash
docker run -it --rm --name immunization -p 8000:8000 immunization:latest
```
> NOTE: On windows, it might not work in Powershell, try it using cmd instead

---
## Using local python3

You can also run it locally, but might need to install additional system dependencies `build-deps gcc python3-dev musl-dev libxlt-dev postgresql-dev` - which may or may not exist on Windows.

1. This step is only required to be run once
```bash
pip3 install -r req.txt
```
2. Run the server
```bash
python3 manage.py runserver 0.0.0.0:8000
```
3. Use the following to check all available Django based sub-commands
```bash
python3 manage.py
```
> NOTE: Depending upon your python installation, you might need to replace `python3` with `python` and `pip3` with `pip`.

---
