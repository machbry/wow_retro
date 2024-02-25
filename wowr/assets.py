import json

from dagster import asset

from wowr.constants import WOWR_GUILD_ID, WOWR_DATA_DIRECTORY_PATH
from wowr.wlogs.queries import query_reports_on_page


@asset
def get_guild_reports():
    page = 1
    responses = {}
    has_more_pages = True
    while has_more_pages:
        responses[page] = query_reports_on_page(guild_id=WOWR_GUILD_ID, page=page)
        has_more_pages = responses[page]['data']['reportData']['reports']['has_more_pages']
        page +=1

    guild_reports_json = []
    for response in responses.values():
        guild_reports_json = guild_reports_json + response['data']['reportData']['reports']['data']

    with open(WOWR_DATA_DIRECTORY_PATH / "guild_reports.json", "w") as f:
        json.dump(guild_reports_json, f)
