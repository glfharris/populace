import svgwrite as svg

def create_gradient(fraction, highlight, base, orientation):

    if orientation == 'h':
        orient = {'start': (1,0), 'end':(0,0)}
    if orientation == 'v':
        orient = {'start': (0,0), 'end':(0,1)}
    lin_grad = svg.gradients.LinearGradient(**orient)
    lin_grad.add_stop_color(offset=fraction, color=base, opacity=255)
    lin_grad.add_stop_color(offset=fraction, color=highlight, opacity=255)

    return lin_grad