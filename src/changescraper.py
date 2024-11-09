from ChangeDotOrgScraper import scrape_petitions

url='https://www.change.org/search?q=Climate%20Change%202024&offset=0'

SNAP_petitions_df=scrape_petitions(url)

print(SNAP_petitions_df)