import hashlib
import hmac
import json
import time
import urllib

from hqlib.hyperquant.api import Platform, Sorting, Direction
from hqlib.hyperquant.clients import WSClient, Trade, Error,  WSConverter, RESTConverter, PlatformRESTClient, PrivatePlatformRESTClient, ItemObject
from hqlib.hyperquant.api import ErrorCode, Endpoint, ParamName
# REST


# TODO check getting trades history from_id=1

