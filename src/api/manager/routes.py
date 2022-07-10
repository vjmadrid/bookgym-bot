import logging

from flask import Blueprint, jsonify

from . import constants

# Logging Configuration
logger = logging.getLogger(__name__)

# Blueprint Configuration
manager_bp = Blueprint("api", __name__, url_prefix=constants.ROOT_ENDPOINT)


@manager_bp.route(constants.HEALTH_ENDPOINT, endpoint="health")
@manager_bp.route(constants.IS_ALIVE_ENDPOINT, endpoint="is_alive")
def health_manager():
    """Handles HTTP requests to URL:
    * /api/v1/manager/health
    * /api/v1/manager/isalive
    """

    return jsonify(success=True)
