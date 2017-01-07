import svgwrite as svg

from uuid import uuid4

from .symbols import *
from .colours import *

class FragmentMixin:

        def _add_to_defs(self, object):
            object_id = uuid4()
            object.attribs['id'] = object_id
            self.defs.add(object)
            return object_id
            