import json
from dataclasses import dataclass
from typing import Any

import requests

from wowr.logger import get_logger
from wowr.constants import WLOGS_CLIENT_ID, WLOGS_CLIENT_SECRET, WLOGS_TOKEN_URL, WLOGS_AUTHORIZE_URL, \
    WLOG_AUTH_FLOW_DATA

log = get_logger()


@dataclass
class GraphQLClient:
    client_id = WLOGS_CLIENT_ID
    client_secret = WLOGS_CLIENT_SECRET
    authorize_url = WLOGS_AUTHORIZE_URL
    token_url = WLOGS_TOKEN_URL
    auth_flow_data = WLOG_AUTH_FLOW_DATA
    access_token: str = ""

    def _init_access_token(self):
        log.debug(f"Token request for client {self.client_id} at {self.token_url}.")
        response = requests.post(url=self.token_url,
                                 data=self.auth_flow_data,
                                 auth=(self.client_id, self.client_secret))
        try:
            self.access_token = response.json()['access_token']
        except KeyError:
            log.exception("Access token not retrieved.")
            raise
        else:
            log.info("Access token retrieved.")
        self._headers = {'Authorization': 'Bearer ' + self.access_token}

    def post(self, query: str) -> Any:
        if not self.access_token:
            self._init_access_token()

        log.debug(f"Query request: {query}")
        response = requests.get(self.authorize_url,
                                headers=self._headers,
                                json={'query': query})
        return json.loads(response.text)
    