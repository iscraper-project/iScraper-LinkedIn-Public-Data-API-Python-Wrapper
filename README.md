# iScraper LinkedIn API Python SDK
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
You need your API key to consume our APIs. Create the client first by providing your API key. Don't have an API key yet? [Get it here](https://app.iscraper.io)
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

## LinkedIn Search
Find companies:
```python
params = {
    'keyword': 'data science',
    'location': 'United States',
    'size': '11-50',
    'search_type': 'companies'
}
results = client.search_results(**params)
```
Find personal profiles:
```python
params = {
    'keyword': 'data science',
    'search_type': 'people'
}
results = client.search_results(**params)
```

## Get Locations
Get supported locations list to use with search.
```python
locations = client.get_locations()
```

For support related to this SDK, use the issues section. For sales related enquiries, send an email at sales@iscraper.io.