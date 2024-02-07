import re
from scrapingbee import ScrapingBeeClient

client = ScrapingBeeClient(api_key='NDCTIM3L1DHXSM9KSBUGE60B9VKXTBAJOUAJR1QWB7FH0ITUN40EL58ZHZI7JECYEQZ9QLEDLQLP11EN')

url = "https://www.amazon.in/Fire-Boltt-Bluetooth-Calling-Assistance-Resolution/dp/B0BF57RN3K/ref=sr_1_1?crid=3RWAAT7GD8AER&keywords=smartwatch&qid=1707317738&sprefix=smartwatch%2Caps%2C1570&sr=8-1-spons&sp_csd=d2lkZ2V0TmFtZT1zcF9hdGY&psc=1"

response = client.get(
    url,
    params={
        'extract_rules': {
            "name": {
                "selector": "span[id='productTitle']",
                "output": "text",
            },
            "price": {
                "selector": "span[class='a-price a-text-price a-size-medium apexPriceToPay'] > span",
                "output": "text",
            },
          "Manufacturer": {
            "selector": "div[id='Manufacturer']",
              "output": "text",
          },
            "rating": {
                "selector": "i[class='a-icon a-icon-star a-star-4-5'] > span",
                "output": "text",
            },
            "description": {
                "selector": "div[id='productDescription']",
                "output": "text",
            },
            "full_html": {
                "selector": "html",
                "output": "html",
            },
        }
    }
)

if response.ok:
    scraped_data = response.json()
    images = re.findall('"hiRes":"(.+?)"', response.json()['full_html'])

    print(scraped_data['name'])
    print(scraped_data['price'])
    print(scraped_data['rating'])
    print(scraped_data['Manufacturer'])
    print(scraped_data['description'])
    print(images)