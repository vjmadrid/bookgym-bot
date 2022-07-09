# -*- coding: utf-8 -*-

from http import HTTPStatus
from flask import Blueprint, jsonify


from . import constants


manager_bp = Blueprint("api", __name__, url_prefix="/manager")


@manager_bp.route(constants.HEALTH_ENDPOINT, endpoint="health")
@manager_bp.route(constants.IS_ALIVE_ENDPOINT, endpoint="is_alive")
def HealthManager():
    """Handles HTTP requests to URL:
    * /api/v1/manager/health
    * /api/v1/manager/isalive
    """

    return jsonify(success=True)
