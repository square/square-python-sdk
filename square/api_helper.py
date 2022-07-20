# -*- coding: utf-8 -*-

import re
import sys
import datetime
import calendar
import email.utils as eut
from time import mktime

import jsonpickle
import dateutil.parser
from requests.utils import quote


class APIHelper(object):

    """A Helper Class for various functions associated with API Calls.

    This class contains static methods for operations that need to be
    performed during API requests. All of the methods inside this class are
    static methods, there is no need to ever initialise an instance of this
    class.

    """

    SKIP = '#$%^S0K1I2P3))*'

    @staticmethod
    def get_request_parameter(value, is_wrapped=False):
        """get the correct serialization method for a oneof/anyof parameter type.

        Args:
            value: the value of the request parameter
            is_wrapped: whether parameter are wrapped in object or not

        Returns:
             A correct serialized value which can be used
             when sending a request.

        """

        if type(value) is str:
            return value
        if is_wrapped:
            return APIHelper.json_serialize_wrapped_params(value)
        return APIHelper.json_serialize(value)

    @staticmethod
    def json_serialize_wrapped_params(obj):
        """JSON Serialization of a given wrapped object.

        Args:
            obj (object): The object to serialize.

        Returns:
            str: The JSON serialized string of the object.

        """
        if obj is None:
            return None
        val = dict()
        for k,v in obj.items():
            val[k] = APIHelper.json_serialize(v, should_encode=False)

        return jsonpickle.encode(val, False)

    @staticmethod
    def json_serialize(obj, should_encode=True):
        """JSON Serialization of a given object.

        Args:
            obj (object): The object to serialize.
            should_encode: whether to encode at end or not

        Returns:
            str: The JSON serialized string of the object.

        """
        if obj is None:
            return None

        # Resolve any Names if it's one of our objects that needs to have this called on
        if isinstance(obj, list):
            value = list()
            for item in obj:
                if hasattr(item, "_names"):
                    value.append(APIHelper.to_dictionary(item))
                else:
                    value.append(item)
            obj = value
        else:
            if hasattr(obj, "_names"):
                obj = APIHelper.to_dictionary(obj)
        if not should_encode:
            return obj
        return jsonpickle.encode(obj, False)

    @staticmethod
    def json_deserialize(json, unboxing_function=None, as_dict=False):
        """JSON Deserialization of a given string.

        Args:
            json (str): The JSON serialized string to deserialize.

        Returns:
            dict: A dictionary representing the data contained in the
                JSON serialized string.

        """
        if json is None:
            return None

        try:
            decoded = jsonpickle.decode(json)
        except ValueError:
            return json

        if unboxing_function is None:
            return decoded

        if as_dict:
            return {k: unboxing_function(v) for k, v in decoded.items()}
        elif isinstance(decoded, list):
            return [unboxing_function(element) for element in decoded]
        else:
            return unboxing_function(decoded)

    @staticmethod
    def get_content_type(value):
        """Get content type header for oneof.

        Args:
            value: The value passed by the user.

        Returns:
            dict: A dictionary representing the data contained in the
                JSON serialized string.

        """
        if value is None:
            return None
        primitive = (int, str, bool, float)

        if type(value) in primitive:
            return 'text/plain; charset=utf-8'

        else:
            return 'application/json; charset=utf-8'

    @staticmethod
    def get_schema_path(path):
        """Return the Schema's path

        Returns:
            string : returns Correct schema path

        """
        path = path.replace('\\models', '\\schemas').replace('/models', '/schemas').replace(".py", ".json")
        return path

    @staticmethod
    def serialize_array(key, array, formatting="indexed", is_query=False):
        """Converts an array parameter to a list of key value tuples.

        Args:
            key (str): The name of the parameter.
            array (list): The value of the parameter.
            formatting (str): The type of key formatting expected.
            is_query (bool): Decides if the parameters are for query or form.

        Returns:
            list: A list with key value tuples for the array elements.

        """
        tuples = []

        if sys.version_info[0] < 3:
            serializable_types = (str, int, long, float, bool, datetime.date, APIHelper.CustomDate)
        else:
            serializable_types = (str, int, float, bool, datetime.date, APIHelper.CustomDate)

        if isinstance(array[0], serializable_types):
            if formatting == "unindexed":
                tuples += [("{0}[]".format(key), element) for element in array]
            elif formatting == "indexed":
                tuples += [("{0}[{1}]".format(key, index), element) for index, element in enumerate(array)]
            elif formatting == "plain":
                tuples += [(key, element) for element in array]
            elif is_query:
                if formatting == "csv":
                    tuples += [(key, ",".join(str(x) for x in array))]

                elif formatting == "psv":
                    tuples += [(key, "|".join(str(x) for x in array))]

                elif formatting == "tsv":
                    tuples += [(key, "\t".join(str(x) for x in array))]

            else:
                raise ValueError("Invalid format provided.")
        else:
            tuples += [("{0}[{1}]".format(key, index), element) for index, element in enumerate(array)]

        return tuples

    @staticmethod
    def append_url_with_template_parameters(url, parameters):
        """Replaces template parameters in the given url.

        Args:
            url (str): The query url string to replace the template parameters.
            parameters (dict): The parameters to replace in the url.

        Returns:
            str: URL with replaced parameters.

        """
        # Parameter validation
        if url is None:
            raise ValueError("URL is None.")
        if parameters is None:
            return url

        # Iterate and replace parameters
        for key in parameters:
            value = parameters[key]['value']
            encode = parameters[key]['encode']
            replace_value = ''

            # Load parameter value
            if value is None:
                replace_value = ''
            elif isinstance(value, list):
                replace_value = "/".join((quote(str(x), safe='') if encode else str(x)) for x in value)
            else:
                replace_value = quote(str(value), safe='') if encode else str(value)

            url = url.replace('{{{0}}}'.format(key), str(replace_value))

        return url

    @staticmethod
    def append_url_with_query_parameters(url,
                                         parameters,
                                         array_serialization="indexed"):
        """Adds query parameters to a URL.

        Args:
            url (str): The URL string.
            parameters (dict): The query parameters to add to the URL.
            array_serialization (str): The format of array parameter serialization.

        Returns:
            str: URL with added query parameters.

        """
        # Parameter validation
        if url is None:
            raise ValueError("URL is None.")
        if parameters is None:
            return url
        parameters = APIHelper.process_complex_types_parameters(parameters, array_serialization)
        for index, value in enumerate(parameters):
            key = value[0]
            val = value[1]
            seperator = '&' if '?' in url else '?'
            if value is not None:
                url += "{0}{1}={2}".format(seperator, key, quote(str(val), safe=''))

        return url

    @staticmethod
    def process_complex_types_parameters(query_parameters, array_serialization):
        processed_params = []
        for key, value in query_parameters.items():
            processed_params.extend(
                APIHelper.form_encode(value, key, array_serialization=array_serialization, is_query=True))
        return processed_params


    @staticmethod
    def clean_url(url):
        """Validates and processes the given query Url to clean empty slashes.

        Args:
            url (str): The given query Url to process.

        Returns:
            str: Clean Url as string.

        """
        # Ensure that the urls are absolute
        regex = "^https?://[^/]+"
        match = re.match(regex, url)
        if match is None:
            raise ValueError('Invalid Url format.')

        protocol = match.group(0)
        index = url.find('?')
        query_url = url[len(protocol): index if index != -1 else None]
        query_url = re.sub("//+", "/", query_url)
        parameters = url[index:] if index != -1 else ""

        return protocol + query_url + parameters

    @staticmethod
    def form_encode_parameters(form_parameters,
                               array_serialization="indexed"):
        """Form encodes a dictionary of form parameters

        Args:
            form_parameters (dictionary): The given dictionary which has
            atleast one model to form encode.
            array_serialization (str): The format of array parameter serialization.

        Returns:
            dict: A dictionary of form encoded properties of the model.

        """
        encoded = []

        for key, value in form_parameters.items():
            encoded += APIHelper.form_encode(value, key, array_serialization)

        return encoded

    @staticmethod
    def form_encode(obj,
                    instance_name,
                    array_serialization="indexed", is_query=False):
        """Encodes a model in a form-encoded manner such as person[Name]

        Args:
            obj (object): The given Object to form encode.
            instance_name (string): The base name to appear before each entry
                for this object.
            array_serialization (string): The format of array parameter serialization.
            is_query (bool): Decides if the parameters are for query or form.

        Returns:
            dict: A dictionary of form encoded properties of the model.

        """
        retval = []

        if obj is None:
            return []
        elif isinstance(obj, list):
            for element in APIHelper.serialize_array(instance_name, obj, array_serialization, is_query):
                retval += APIHelper.form_encode(element[1], element[0], array_serialization, is_query)
        elif isinstance(obj, dict):
            for item in obj:
                retval += APIHelper.form_encode(obj[item], instance_name + "[" + item + "]", array_serialization, is_query)
        else:
            retval.append((instance_name, obj))

        return retval

    @staticmethod
    def to_dictionary(obj):
        """Creates a dictionary representation of a class instance. The
        keys are taken from the API description and may differ from language
        specific variable names of properties.

        Args:
            obj: The object to be converted into a dictionary.

        Returns:
            dictionary: A dictionary form of the model with properties in
            their API formats.

        """
        dictionary = dict()

        optional_fields = obj._optionals if hasattr(obj, "_optionals") else []
        nullable_fields = obj._nullables if hasattr(obj, "_nullables") else []

        # Loop through all properties in this model
        for name in {k: v for k, v in obj.__dict__.items() if v is not None}:
            value = getattr(obj, name, APIHelper.SKIP)

            if value is APIHelper.SKIP:
                continue

            if value is None:
                if name not in optional_fields and not name in nullable_fields:
                    raise ValueError(f"The value for {name} can not be None for {obj}")
                else:
                    dictionary[obj._names[name]] = None
            elif isinstance(value, list):
                # Loop through each item
                dictionary[obj._names[name]] = list()
                for item in value:
                    dictionary[obj._names[name]].append(APIHelper.to_dictionary(item) if hasattr(item, "_names") else item)
            elif isinstance(value, dict):
                # Loop through each item
                dictionary[obj._names[name]] = dict()
                for key in value:
                    dictionary[obj._names[name]][key] = APIHelper.to_dictionary(value[key]) if hasattr(value[key], "_names") else value[key]
            else:
                dictionary[obj._names[name]] = APIHelper.to_dictionary(value) if hasattr(value, "_names") else value

        # Return the result
        return dictionary

    @staticmethod
    def when_defined(func, value):
        return func(value) if value else None

    class CustomDate(object):

        """ A base class for wrapper classes of datetime.

        This class contains methods which help in
        appropriate serialization of datetime objects.

        """

        def __init__(self, dtime, value=None):
            self.datetime = dtime
            if not value:
                self.value = self.from_datetime(dtime)
            else:
                self.value = value

        def __repr__(self):
            return str(self.value)

        def __getstate__(self):
            return self.value

        def __setstate__(self, state):
            pass

    class HttpDateTime(CustomDate):

        """ A wrapper class for datetime to support HTTP date format."""

        @classmethod
        def from_datetime(cls, date_time):
            return eut.formatdate(timeval=mktime(date_time.timetuple()),
                                  localtime=False, usegmt=True)

        @classmethod
        def from_value(cls, value):
            dtime = datetime.datetime.fromtimestamp(eut.mktime_tz(eut.parsedate_tz(value)))
            return cls(dtime, value)

    class UnixDateTime(CustomDate):

        """ A wrapper class for datetime to support Unix date format."""

        @classmethod
        def from_datetime(cls, date_time):
            return calendar.timegm(date_time.utctimetuple())

        @classmethod
        def from_value(cls, value):
            dtime = datetime.datetime.utcfromtimestamp(float(value))
            return cls(dtime, float(value))

    class RFC3339DateTime(CustomDate):

        """ A wrapper class for datetime to support Rfc 3339 format."""

        @classmethod
        def from_datetime(cls, date_time):
            return date_time.isoformat()

        @classmethod
        def from_value(cls, value):
            dtime = dateutil.parser.parse(value)
            return cls(dtime, value)
