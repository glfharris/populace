import svgwrite as svg

from uuid import uuid4

from .symbols import *
from .colours import *
from .fragment import *
from .utils import *

class Queue(svg.container.Group, FragmentMixin):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.xmax = 0
        self.ymax = 0
        self.defs = svg.container.Defs()

    def symbol(self, symbol):
        self.sym_id = self._add_to_defs(symbol)
        self.sym_x = symbol.dim
        self.sym_y = symbol.dim
        return self

    def create(self, fraction, length=10, q_orient='h', **kwargs):

        highlight = kwargs.pop('highlight', TABLEAU['red'])
        base = kwargs.pop('highlight', TABLEAU['light red'])
        orient = kwargs.pop('orient', 'v')

        offset = 1 - ((length * fraction) % 1)
        grad_id = self._add_to_defs(create_gradient(fraction, highlight, base, orient))

        self.attribs['fill'] = base

        for i in range(length):
            tmp = svg.container.Use("#" + str(self.sym_id))

            if i <= (fraction * length) - 1:
                tmp.fill(color=highlight)
            if 0 < (fraction * length) - i < 1:
                tmp.fill(color="#" + str(grad_id))
            
            if q_orient == 'h':
                tmp.translate(i * (self.sym_x / 2))
            if q_orient == 'v':
                tmp.translate(0, (length - i) * self.sym_y)
            self.add(tmp)
        if q_orient == 'h':
            self.ymax = self.sym_y
            self.xmax = (length + 1) * 0.5 * self.sym_x
        if q_orient == 'v':
            self.ymax = length * self.sym_y
            self.xmax = self.sym_x

        return self

