import logging
import requests

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
)

def check_website(url):
    try:
        # HEAD request to check server status
        head_response = requests.head(url, timeout=5)
        if head_response.status_code == 200:
            logging.info(f"Server is alive: {url}")
        else:
            logging.warning(f"Server returned status code: {head_response.status_code} for {url}")

        # GET request to fetch the server's technology
        get_response = requests.get(url, timeout=5)
        
        if get_response.status_code == 200:
            server = get_response.headers.get('Server', 'Unknown')
            logging.info(f"Server technology: {server}")
        else:
            logging.warning(f"Server returned status code: {get_response.status_code} for {url}")

        # OPTIONS request to check allowed methods
        options_response = requests.options(url, timeout=5)
        allowed_methods = options_response.headers.get('Allow', 'Not specified')
        logging.info(f"Allowed methods: {allowed_methods} for {url}")

    except requests.exceptions.Timeout:
        logging.error(f"Timeout error while checking website: {url}")
    except requests.exceptions.ConnectionError:
        logging.error(f"Connection error while checking website: {url}")
    except requests.RequestException as e:
        logging.error(f"An error occurred while checking website {url}: {e}")

# Example usage
url = input("Enter the URL: ")
check_website(url)
