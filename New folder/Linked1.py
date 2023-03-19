import requests
import pandas as pd
from pandas.io.json import json_normalize
url="apiadapter.ad5track.com/v3/ads/americanas?size=10&uid=va_1645631511155.0.5938751290497459&context=search&term=maos&placements=%7B%22search.1%22%3A%7B%22size%22%3A2%7D%2C%22search.2%22%3A%7B%7D%2C%22keyword.search.1%22%3A%7B%22size%22%3A4%7D%7D&referrer=https%3A%2F%2Fwww.americanas.com.br%2Fbusca%2Fmaos%3F"
response  = requests.get(url)
data = response.json()
data = json_normalize(data)
df = pd.DataFrame(data)
print(df)
