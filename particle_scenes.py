#!/usr/bin/python
# -*- coding: UTF-8 -*-

from manimlib.imports import *

# To watch one of these scenes, run the following:
# python -m manim example_scenes.py SquareToCircle -pl
#
# Use the flag -l for a faster rendering at a lower
# quality.
# Use -s to skip to the end and just save the final frame
# Use the -p to have the animation (or image, if -s was
# used) pop up once done.
# Use -n <number> to skip ahead to the n'th animation of a scene.
# Use -r <number> to specify a resolution (for example, -r 1080
# for a 1920x1080 video)

particles_ch = [
    {
        "symbol": "\\gamma",
        "name": "ფოტონი",
        "year": 1800
    },{
        "symbol": "e^-",
        "name": "ელექტრონი",
        "year": 1897
    },{
        "symbol": "\\alpha",
        "name": "ალფა გამოსხივება",
        "year": 1899
    },{
    #     "symbol": "",
    #     "name": "ატომბირთვი",
    #     "year": 1911
    # },{
        "symbol": "p",
        "name": "პროტონი",
        "year": 1919
    },{
        "symbol": "d",
        "name": "დეიტერიუმი",
        "year": 1931
    },{
        "symbol": "n",
        "name": "ნეიტრონი",
        "year": 1932
    },{
        "symbol": "e^+",
        "name": "პოზიტრონი",
        "year": 1932
    },{
        "symbol": "\\mu^-",
        "name": "მიონი",
        "year": 1937
    },{
        "symbol": "\pi",
        "name": "პიონი",
        "year": 1947
    },{
        "symbol": "K",
        "name": "კაონი",
        "year": 1947
    },{
        "symbol": "\\Lambda^0",
        "name": "ლამბდა",
        "year": 1950
    },{
        "symbol": "\\bar{p}",
        "name": "ანტიპროტონი",
        "year": 1955
    },{
        "symbol": "\\nu_e",
        "name": "ელექტრონული ნეიტრინო",
        "year": 1956
    },{
        "symbol": "\\nu_\\mu",
        "name": "მიონური ნეიტრინო",
        "year": 1962
    },{
        "symbol": "\\Xi",
        "name": "ქსი ბარიონი",
        "year": 1964
    },{
        "symbol": "u ~ d ~ s",
        "name": "მსუბუქი კვარკები",
        "year": 1969
    },{
        "symbol": "J/\\Psi",
        "name": "ფსი მეზონი",
        "year": 1974
    },{
        "symbol": "c",
        "name": "კვარკი",
        "year": 1974
    },{
        "symbol": "\\tau",
        "name": "ტაუ",
        "year": 1975
    },{
        "symbol": "\\Upsilon",
        "name": "უფსილონი",
        "year": 1977
    },{
        "symbol": "b",
        "name": "კვარკი",
        "year": 1977
    },{
        "symbol": "g",
        "name": "გლუონი",
        "year": 1979
    },{
        "symbol": "Z ~ W^{\\pm}",
        "name": "ბოზონები",
        "year": 1983
    },{
        "symbol": "t",
        "name": "კვარკი",
        "year": 1995
    },{
        "symbol": "\\nu_\\tau",
        "name": "ტაუ ნეიტრინო",
        "year": 2000
    },{
        "symbol": "H",
        "name": "ჰიგსის ბოზონი",
        "year": 2012
    }
]

class EnterPhoton(Scene):
    def construct(self):
        photon_symbol = TexMobject("\\gamma", color=ORANGE)
        photon_text = TextMobject("ფოტონი (1800)")
        photon_text.scale(0.5)
        group = VGroup(photon_symbol, photon_text)
        group.arrange(RIGHT)
        self.play(Write(photon_symbol))
        self.play(Write(photon_text))
        self.wait()


class ParticlesCh(Scene):
    def construct(self):
        pcolor = RED
        symbols = list()
        names = list()
        ticks = list()
        groups = list()
        timelineparams = {
            "x_min": -5,
            "x_max": 6,
            "unit_size": 1,
            "include_ticks": True,
            "tick_size": 0.1,
            "tick_frequency": 1,
            "numbers_with_elongated_ticks": [],
            # "stroke_opacity": 0.5
        }
        def year_tick(year):
            tick = -5 + (year - 1800) / 20
            tick_circle = Circle(arc_center=(tick,0,0), color=pcolor, stroke_width=0, fill_color=pcolor, fill_opacity=.75, radius=0.1)
            tick_circle.shift(0.8*BOTTOM)
            return tick_circle
        timeline = NumberLine(**timelineparams)
        timeline.shift(0.8*BOTTOM)
        timelinetick1 = TexMobject("1800")
        timelinetick1.shift((-5,0,0))
        timelinetick1.shift(0.9*BOTTOM)
        timelinetick2 = TexMobject("1900")
        # timelinetick2.shift((0,0,0))
        timelinetick2.shift(0.9*BOTTOM)
        timelinetick3 = TexMobject("2020")
        timelinetick3.shift((6,0,0))
        timelinetick3.shift(0.9*BOTTOM)

        for particle in particles_ch:
            particle_symbol = TexMobject(particle["symbol"], color=pcolor)
            particle_name = TextMobject(particle["name"] + " (" + str(particle["year"]) + ")")
            particle_name.scale(0.5)
            ticks.append(year_tick(particle["year"]))
            group = VGroup(particle_symbol, particle_name)
            group.arrange(RIGHT)
            symbols.append(particle_symbol)
            names.append(particle_name)
            groups.append(group)
        separator = int(np.ceil(len(groups)/2))+1
        verticalgroup1 = VGroup(*groups[:separator])
        verticalgroup1.arrange(DOWN)
        verticalgroup2 = VGroup(*groups[separator:])
        verticalgroup2.arrange(DOWN)
        thewholegroup = VGroup(verticalgroup1, verticalgroup2)
        thewholegroup.arrange(RIGHT)
        thewholegroup.scale(0.8)
        thewholegroup.shift(0.5*UP)
        self.play(ShowCreation(timeline))
        self.play(ShowCreation(timelinetick1), ShowCreation(timelinetick2), ShowCreation(timelinetick3))
        self.wait()
        for i in range(len(names)):
            self.play(Write(symbols[i]),Write(names[i]),GrowFromCenter(ticks[i]))
        self.wait()
        self.play(*[Uncreate(names[i]) for i in range(len(names))])
        symbolsgroup = VGroup(*symbols)
        self.play(ApplyMethod(symbolsgroup.scale, 0.8))
        self.play(ApplyMethod(symbolsgroup.arrange, RIGHT))
        timelinegroup = VGroup(timeline, timelinetick1, timelinetick2, timelinetick3, *ticks)
        self.play(ApplyMethod(symbolsgroup.shift, 0.8*BOTTOM), FadeOut(timelinegroup))
        self.wait()