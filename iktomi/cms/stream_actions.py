# -*- coding: utf-8 -*-
from iktomi import web
from webob.exc import HTTPForbidden


class StreamAction(web.WebHandler):

    item_lock = True
    for_item = True
    action = title = cls = None
    allowed_for_new = False
    display = True

    def is_available(self, env, item=None):
        """ Rewrite this method to add condition when action is avalible
        """
        return True

    def is_visible(self, env, item=None):
        """ Tells if this action button is visible.
        """
        return self.is_available(env, item) and self.display

    def insure_is_available(self, env, item=None):
        """ Shortcut to check is_avalible rule on handle
        """
        if hasattr(self, 'is_available') and not self.is_available(env, item):
            raise HTTPForbidden

    def __init__(self, stream=None, **kw):
        self.init_kwargs = kw
        self.stream = stream
        self.action = kw.get('action', self.action)
        self.title = kw.get('title', self.title)
        self.cls = kw.get('cls', self.cls)
        self.allowed_for_new = kw.get('allowed_for_new', self.allowed_for_new)
        self.display = kw.get('display', self.display)

    def bind(self, stream):
        return self.__class__(stream=stream, **self.init_kwargs)


class PostAction(StreamAction):

    mode = 'post'


class GetAction(StreamAction):

    mode = 'get'


class CustomAction(StreamAction):

    mode = 'custom'


class AfterPostAction(StreamAction):

    mode = 'after-post'


