import json

import apache_beam as beam
import urllib.request as request

from bulq.core.plugin import BulqInputPlugin


class BulqInputExchangeRatesApi(BulqInputPlugin):
    URL = 'https://api.exchangeratesapi.io/history?start_at={}&end_at={}&base={}'
    def __init__(self, conf):
        self.date_ranges = [(conf['start_at'], conf['end_at'])]
        self.base = conf['base']

    def setup(self):
        pass

    def request_data(self, date_range):
        url = BulqInputExchangeRatesApi.URL.format(date_range[0], date_range[1], self.base)
        connection = request.urlopen(url)
        res = connection.read().decode('utf-8')
        rates = json.loads(res)['rates']
        for k, v in rates.items():
            v['date'] = k
            yield v

    def build(self, p):
        api_read = (
            p
            | 'Create date range' >> beam.Create(self.date_ranges)
            | 'Get exchange rates' >> beam.FlatMap(self.request_data)
        )
        return api_read

