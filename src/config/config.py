PORT=5000
POLLING_INTERVAL=1200 # Poll every 20 minutes

EU_URL = "https://register.eci.ec.europa.eu/core/api/register/search/ALL/EN/0/20"
EU_PARLIAMENT = "https://www.europarl.europa.eu/petitions/en/show-petitions?keyWords=&years=2024&_years=1&_searchThemes=1&statuses=AVAILABLE&_statuses=1&_countries=1&searchRequest=true&resSize=10&pageSize=10#res"
KANSALAISALOITE_URL = "https://www.kansalaisaloite.fi/fi/hae?searchView=pub&offset=0&limit=500&orderBy=mostTimeLeft&show=running"

GOOGLE_DRIVER_LOC = '/usr/bin/google-chrome-stable'

CONNECTION_CONFIG = {
    'host': "34.67.133.83",
    'user': "root",
    'port': "3308",
    'password': "pass",
    'database': "alrdmc"
}

CHANGE_URLS = [
    "https://www.change.org/t/abortion-access-en-us?source_location=homepage",
    "https://www.change.org/t/health-and-well-being-en-us?source_location=topic_page",
    "https://www.change.org/t/public-health-en-us?source_location=topic_page",
    "https://www.change.org/t/government-and-politics-en-us?source_location=topic_page",
    "https://www.change.org/t/public-safety-2?source_location=topic_page",
    "https://www.change.org/t/criminal-justice-en-US?source_location=topic_page",
    "https://www.change.org/t/student-issues-en-us?source_location=topic_page",
#    "https://www.change.org/t/free-speech-en-us?source_location=homepage",
#    "https://www.change.org/t/entertainment-media-en-us?source_location=topic_page",
#    "https://www.change.org/t/technology-9?source_location=topic_page",
#    "https://www.change.org/t/video-games-online-gaming-en-us?source_location=topic_page",
#    "https://www.change.org/t/consumer-rights-en-us?source_location=topic_page",
#    "https://www.change.org/t/environmental-issues-en-us?source_location=topic_page",
#    "https://www.change.org/t/animal-rights-and-conservation-en-us?source_location=topic_page",
#    "https://www.change.org/t/business-and-economy-en-us?source_location=topic_page",
#    "https://www.change.org/t/corporate-responsibility-en-us?source_location=topic_page",
#    "https://www.change.org/t/free-speech-en-us?source_location=homepage"
#    "https://www.change.org/browse"
#    "https://www.change.org/t/entertainment-11?source_location=homepage"
#    "https://www.change.org/t/sports-12?source_location=topic_page"
#    "https://www.change.org/t/recreational-infrastructure-en-us?source_location=topic_page"
#    "https://www.change.org/browse/recent"

]