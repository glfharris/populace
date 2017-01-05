import svgwrite as svg

import symbols
from colours import TABLEAU

def generate(fraction, length=10, base=TABLEAU["light red"], highlight=TABLEAU["red"],
             filename="noname.svg", symbol=symbols.HOLLOW_MAN):
    width = 489.3 # hard coded for now
    height = 489.3

    figure = svg.Drawing(filename=filename, fill=base)
    figure.viewbox(width=((length + 1) * 0.5 * width), height=height)
    definitions = figure.add(svg.container.Defs())
    definitions.add(symbol)

    #gradient
    offset = 1 - ((length * fraction) % 1)
    lin_grad = svg.gradients.LinearGradient(start=(0, 0), end=(0, 1), id="lin_grad")
    lin_grad.add_stop_color(offset=offset, color=base, opacity=255)
    lin_grad.add_stop_color(offset=offset, color=highlight, opacity=255)
    definitions.add(lin_grad)

    group = svg.container.Group()
    for i in range(length):
        tmp = svg.container.Use("#symbol")
        if i <= (fraction * length) - 1:
            tmp.fill(color=highlight)
        if 0 < (fraction * length) - i < 1:
            tmp.fill(color="url(#lin_grad)")
        tmp.translate(i * (width / 2))
        group.add(tmp)
    
    figure.add(group)
    return figure

