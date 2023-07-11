import requests


def get_v1_account():
    """
    Get current user
    :return:
    """
    url = "http://localhost:5051/v1/account"

    payload = {}
    headers = {
        'X-Dm-Auth-Token': 'IQJh+zgzF5ApLc2HuKVvD280AJa+svT3T8bZdE3e81TwBuSGSSl6TOHopbn4heMzsEpWx3SXbBZ15F2/ynMClqzh6DbalZCK3asu48xMTZMg8zOjZzfiTAEdIIgzKT2F2p2V9dpKEh8= ',
        'X-Dm-Bb-Render-Mode': '',
        'Accept': 'text/plain'
    }

    response = requests.request(
        method="GET",
        url=url,
        headers=headers,
        json=payload
    )
    return response
