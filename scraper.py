from dc_base_scrapers.geojson_scraper import RandomIdGeoJSONScraper


stations_url = "http://maps.scarborough.gov.uk/geoserver/inspire/wms?service=WFS&version=1.3.0&request=GetFeature&typeNames=Polling_Stations_Open&outputFormat=json&srsName=EPSG%3A4326&sortBy=id"
council_id = 'E07000168'


scraper = RandomIdGeoJSONScraper(stations_url, council_id, 'utf-8', 'stations')
scraper.scrape()
