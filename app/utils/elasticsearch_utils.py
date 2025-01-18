# app/utils/elasticsearch_utils.py
import time
import requests

def wait_for_elasticsearch(url: str, timeout: int = 60):
    """Esperar a que Elasticsearch esté listo."""
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            response = requests.get(url)
            if response.status_code == 200:
                return True
        except requests.exceptions.ConnectionError:
            pass
        time.sleep(1)
    raise Exception("Elasticsearch no está listo")