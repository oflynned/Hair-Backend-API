from bson import json_util
from flask import Blueprint, Response, request

from app.use_cases.common.distance import Distance
from app.use_cases.common.exception_payload import ExceptionPayload
from app.use_cases.vendor_data.retrieve_vendor_meta_data import RetrieveVendorMetaData
from app.use_cases.vendor_filters.filter_exceptions import AttributeNotPresent, InvalidAttributeRange
from app.use_cases.vendor_filters.filter_vendors_by_attribute import DistanceFilter

vendor_endpoint = Blueprint("vendor", __name__)


@vendor_endpoint.route("/", methods=["GET"])
def get_vendor_data():
    vendor_data = RetrieveVendorMetaData.get_vendor_data()

    return Response(json_util.dumps(vendor_data), status=200, mimetype="application/json")


@vendor_endpoint.route("/distance", methods=["GET"])
def get_distance_to_vendor():
    user_lat = request.args.get("user_lat")
    user_lng = request.args.get("user_lng")
    vendor_lat = request.args.get("vendor_lat")
    vendor_lng = request.args.get("vendor_lng")

    distance = Distance.get_distance_between_points_in_km(user_lat, user_lng, vendor_lat, vendor_lng)
    payload = {
        "distance": distance
    }

    return Response(json_util.dumps(payload), status=200, mimetype="application/json")


@vendor_endpoint.route("/filter", methods=["GET"])
def get_vendors_nearby():
    lat = request.args.get("lat")
    lng = request.args.get("lng")
    radius = request.args.get("radius")

    vendors = DistanceFilter.get_vendors_within_distance(lat, lng, radius)
    return Response(vendors, status=200, mimetype="text/plain")


@vendor_endpoint.errorhandler(InvalidAttributeRange)
@vendor_endpoint.errorhandler(AttributeNotPresent)
def handle_invalid_client_usage(error):
    return ExceptionPayload.generate_payload_res(error)
