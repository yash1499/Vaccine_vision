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