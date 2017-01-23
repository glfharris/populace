import svgwrite as svg

from uuid import uuid4

from .symbols import *
from .colours import *
from .fragment import *
from .queue import *

class Graphic(svg.Drawing, FragmentMixin):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.xmax = 0
        self.ymax = 0

    def _update_viewbox(self):
        self.viewbox(width=self.xmax, height=self.ymax)

    def add_obj(self, obj, place='below'):
        tmp = obj
        self.defs.elements += obj.defs.elements
        if place == 'below':
            tmp.translate(0, self.ymax)
            self.add(tmp)
            self.ymax += obj.ymax
            if self.xmax < obj.xmax:
                self.xmax = obj.xmax
        if place == 'right':
            tmp.translate(self.xmax)
            self.add(tmp)
            self.xmax += obj.xmax
            if self.ymax < obj.ymax:
                self.ymax = obj.ymax
        self._update_viewbox()


