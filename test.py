import populace

a = populace.queue.Queue()
a.symbol(populace.symbols.small_man)
a.create(0.6)

b = populace.queue.Queue()
b.symbol(populace.symbols.HOLLOW_WOMAN)
b.create(0.3)
b.translate(0, 10)

fig = populace.graphic.Graphic()
fig.add_obj(a)
fig.add_obj(b)

fig.save()