import requests
import validators
from urllib.parse import urlparse


class Client:
    """iScraper HTTP client.

    This is the iScraper HTTP client base class. You should extend this class if you need to write a custom client.

    Attributes:
        base_url (str): The API base endpoint.
        client (object): The HTTP client object.
    """
    base_url: str = 'https://api.iscraper.io/v2'
    client: object = None

    def __init__(self, apikey: str):
        """Instantiate client.

        Args:
            apikey (str): iScraper API key. Get your API key at https://iscraper.io if you don't have one.
        """
        self.client = requests.Session()
        self.client.headers.update({'X-API-KEY': apikey})

    def _send_request(self, path: str, method: str = 'POST', data: object = None):
        """Send an HTTP request to iScraper API.

        Args:
            path (str): The target path to send the HTTP request to.
            method (str, optional): The HTTP request method. Defaults to 'POST'.
            data (object, optional): The JSON post body. Defaults to None.

        Raises:
            Exception: When request doesn't receive a 200 status code.
            Exception: If API request fails for some other reason.

        Returns:
            object: Returns JSON object when request is successful.
        """
        try:
            url = f'{self.base_url}{path}'
            if method == 'POST':
                res = self.client.post(url, json=data)
            elif method == 'GET':
                res = self.client.get(url)
                
            if res.status_code == 200:
                return res.json()
            else:
                raise Exception(
                    f'Request failed with status code {res.status_code}')
        except Exception as e:
            raise Exception(f'Request failed: {str(e)}')

    def _parse_id(self, url: str):
        """Parse profile ID from URL.

        Args:
            url (str): LinkedIn company or personal profile URL.

        Raises:
            Exception: Raised if the provided URL is invalid.

        Returns:
            str: The parsed profile ID.
        """
        if not validators.url(url):
            raise Exception('Profile URL is invalid.')
        parsed = urlparse(url)
        return str(parsed.path.rstrip('/').split('/')[-1]).strip()

    def profile_details(self, url: str, profile_type: str = 'personal', contact_info: bool = False, recommendations: bool = False, related_profiles: bool = False):
        """Get details for personal and company LinkedIn profiles.

        Args:
            url (str): The LinkedIn profile URL.
            profile_type (str, optional): The profile type. Should be personal or company. Defaults to 'personal'.
            contact_info (bool, optional): Either to fetch the available contact info for a user or not.
            recommendations (bool, optional): Either to fetch the available recommendations or not.
            related_profiles (bool, optional): Either to get the available related profiles or not.
            

        Returns:
            object: The JSON object containing profile details.
        """
        profile_id = self._parse_id(url)
        path = '/profile-details'
        data = {
            'profile_id': profile_id,
            'profile_type': profile_type,
            'contact_info': contact_info,
            'recommendations': recommendations,
            'related_profiles': related_profiles
        }
        return self._send_request(path=path, data=data)

    def company_employees(self, url: str, per_page: int = 50, offset: int = 0):
        """Get company employees.

        Args:
            url (str): Company's LinkedIn profile URL.
            per_page (int, optional): Number of employees to get per page. Defaults to 50.
            offset (int, optional): The offset to get paginated results. Defaults to 0.

        Returns:
            object: JSON object of employees list.
        """
        profile_id = self._parse_id(url)
        path = '/company-employees'
        return self._send_request(path=path, data={'profile_id': profile_id, 'per_page': per_page, 'offset': offset})

    def search_results(self, keyword: str, search_type: str = 'people', location: str = None, size: str = None, per_page: int = 50, offset: int = 0):
        """Perform a LinkedIn search.

        Args:
            keyword (str): The keyword to perform a search on LinkedIn.
            search_type (str, optional): The profile type to search for. Can be either people or companies. Defaults to 'people'.
            location (str, optional): The location string. Defaults to None.
            size (str, optional): The company size. Defaults to None.
            per_page (int, optional): The number of results to get per page. Defaults to 50.
            offset (int, optional): The offset to use when get paginated results. Defaults to 0.

        Returns:
            object: The JSON object of results list.
        """
        path = '/linkedin-search'
        data = {
            'keyword': keyword,
            'search_type': search_type,
            'location': location,
            'size': size,
            'per_page': per_page,
            'offset': offset
        }
        return self._send_request(path=path, data=data)
    
    def get_jobs(self, company_id, offset=0, geo_id=0):
        """Get jobs by company id. company id is found in company details.

        Returns:
            object: JSON object of jobs list.
        """
        path = '/get-jobs'
        data = {
            'company_id': company_id,
            'geo_id': geo_id,
            'per_page': 50,
            'offset': offset
        }
        return self._send_request(path=path, data=data)

    def job_details(self, job_id, html_description: bool = False):
        """Get job detail by job id

        text desc is returned anyway, html would be an extra

        Returns:
            object: JSON object of job description.
        """
        path = '/job-details'
        data = {
            'job_id': job_id,
            'html_description': html_description
        }
        return self._send_request(path=path, data=data)
    
    def get_locations(self):
        """Get supported locations to use with search.

        Returns:
            object: JSON object of locations list.
        """
        path = '/supported-locations'
        return self._send_request(path=path, method='GET')
