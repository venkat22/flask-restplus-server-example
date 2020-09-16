# encoding: utf-8
"""
Teams module
============
"""

from app.extensions.api import api_v1


def init_app(app, **kwargs):
    # pylint: disable=unused-argument,unused-import
    """
    Init teams module.
    """
    api_v1.add_oauth_scope('hello:read', "Provide access to team details")
    api_v1.add_oauth_scope('hello:write', "Provide write access to team details")

    # Touch underlying modules
    from . import helloworld

    api_v1.add_namespace(helloworld.api)
