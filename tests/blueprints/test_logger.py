from logging import Logger
from unittest import mock
from unittest.mock import MagicMock

from flask.testing import FlaskClient


class TestLogger:
    @mock.patch.object(Logger, Logger.error.__name__)
    @mock.patch.object(Logger, Logger.warning.__name__)
    @mock.patch.object(Logger, Logger.debug.__name__)
    def test_logger(
        self, m_logger_debug: MagicMock, m_logger_warning: MagicMock, m_logger_error: MagicMock, client: FlaskClient
    ) -> None:
        client.get("/logger")
        m_logger_debug.assert_called_once_with("A value for debugging")
        m_logger_warning.assert_called_once_with("A warning occurred (42 apples)")
        m_logger_error.assert_called_once_with("An error occurred")
