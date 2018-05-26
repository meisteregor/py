from test_cases import *


class Network(object):
    """Network checks to ensure an app could run correctly"""
    logger = logging.getLogger(__name__)

    @staticmethod
    def check_local_internet():
        Network.logger.debug(cons.DEBUG_CONNECTION_STAGE)
        Network.logger.info(cons.INFO_CHECKING_LOCAL_WEB_AVAILABILITY)
        response = UnixCommands.ping(cons.OUTER_SOURCE)
        Inspection.is_pinging_local(response, Network)

    @staticmethod
    def check_host_availability():
        Network.logger.info(cons.INFO_CHECKING_HOST_AVAILABILITY)
        response = UnixCommands.ping(var.SERVER_IP)
        Inspection.is_pinging_local(response, Network)

    @staticmethod
    def check_remote_internet():
        Network.logger.info(cons.INFO_CHECKING_REMOTE_WEB_AVAILABILITY)
        response = UnixCommands.remote_ping_web(var.SERVER_NAME, var.SERVER_IP, cons.PING_OUTER_SOURCE)
        Inspection.is_pinging_remote(response, Network)
