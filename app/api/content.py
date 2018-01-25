from bson import json_util
from flask import Blueprint, Response

from app.use_cases.vendor_content_feed.remote_fetch_exception import RemoteFetchException
from app.use_cases.vendor_content_feed.retrieve_ig_content import VendorContentFeed
from app.use_cases.common.exception_payload import ExceptionPayload

content_endpoint = Blueprint("content", __name__)


@content_endpoint.route("/", methods=["GET"])
def get_barber_feed():
    raw_data = VendorContentFeed.get_raw_feed_data()
    output = VendorContentFeed.groom_ig_input_data(raw_data)

    return Response(json_util.dumps(output), status=200, mimetype="application/json")


@content_endpoint.route("/raw", methods=["GET"])
def get_raw_feed():
    raw_data = VendorContentFeed.get_raw_feed_data()

    return Response(json_util.dumps(raw_data), status=200, mimetype="application/json")


@content_endpoint.errorhandler(RemoteFetchException)
def handle_server_side_errors(error):
    return ExceptionPayload.generate_payload_res(error)
