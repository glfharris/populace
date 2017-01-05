# Populace

A small little package for generating quick and easy visualizations of population statistics, such as:

![](examples/basic.svg)

As it's in a very early state almost all functionality is the `generate` function, and I've tried to include sane defaults.

#### Fraction

Specifying the fraction is as simple as calling `generate(0.5)`, which will highlight exactly half.

#### Length

Length is simply expressed as a whole integer of the number of people you want in your graphic, such as `generate(0.5, length=7)`.

#### Colours

So far I've imported all of the Tableau 20 set, styled as `TABLEAU['red']` and `TABLEAU['light red']` and so on. At the moment each graphic has a `base` colour and a `highlight` colour, again specified in `generate`.

So putting it all together the most complicated variant it's currently capable of is something like:
```
generate((1/3), length=8, base=TABLEAU['blue'], highlight=TABLEAU['light orange'], filename='fancy.svg').save()
```
![](examples/fancy.svg)
I told you it was still early days!
