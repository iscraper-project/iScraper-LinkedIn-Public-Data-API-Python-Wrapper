# iScraper Python SDK
This is the official SDK to consume iScraper LinkedIn public data APIs. Don't have an API key yet? Visit [https://iscraper.io](https://iscraper.io) to get an API key now.

## Installation
Install from PyPi:
```bash
pip3 install iscraper-python
```
Or install from source:
```bash
git clone https://github.com/iscraper-project/iscraper-python.git && \
cd iscraper-python && \
python3 setup.py install
```

## Authentication
You need your API key to consume our APIs. Create the client first by providing your API key:
```python
from iscraper.client import Client
client = Client('your-api-key')
```

## Get Profile Details
Personal profile details:
```python
url = 'https://linkedin.com/in/williamhgates'
details = client.profile_details(url, profile_type='personal')
```
Company profile details:
```python
url = 'https://linkedin.com/company/microsoft'
details = client.profile_details(url, profile_type='company')
```

## Company Employees
```python
url = 'https://linkedin.com/company/microsoft'
employees = client.company_employees(url = url, per_page = 50, offset = 0)
```