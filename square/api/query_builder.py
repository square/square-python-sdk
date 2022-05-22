# -*- coding: utf-8 -*-

class QueryBuilder(object):
    """A class used for prepare endpoint url
    """

    # The version number of the square service
    api_version = 'v2'

    def __init__(self,
                 endpoint,
                 config):
        """Constructor for the QueryBuilder class

        Args:
            endpoint (string): The Endpoint URL to be called
            config (Configuration): The SDK Configuration

        Returns:
            String: URL with added query parameters.
        """
        self.endpoint = endpoint
        self.base_uri = config.get_base_uri()

    def prepare(self):
        return '{0}/{1}/{2}'.format(self.base_uri, self.api_version, self.endpoint)