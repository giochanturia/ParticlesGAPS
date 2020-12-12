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
    }, {
        "symbol": "e^-",
        "name": "ელექტრონი",
        "year": 1897
    }, {
        "symbol": "\\alpha",
        "name": "ალფა გამოსხივება",
        "year": 1899
    }, {
    #     "symbol": "",
    #     "name": "ატომბირთვი",
    #     "year": 1911
    # },{
        "symbol": "p",
        "name": "პროტონი",
        "year": 1919
    }, {
        "symbol": "d",
        "name": "დეიტერიუმი",
        "year": 1931
    }, {
        "symbol": "n",
        "name": "ნეიტრონი",
        "year": 1932
    }, {
        "symbol": "e^+",
        "name": "პოზიტრონი",
        "year": 1932
    }, {
        "symbol": "\\mu^-",
        "name": "მიონი",
        "year": 1937
    }, {
        "symbol": "\\pi",
        "name": "პიონი",
        "year": 1947
    }, {
        "symbol": "K",
        "name": "კაონი",
        "year": 1947
    }, {
        "symbol": "\\Lambda^0",
        "name": "ლამბდა",
        "year": 1950
    }, {
        "symbol": "\\bar{p}",
        "name": "ანტიპროტონი",
        "year": 1955
    }, {
        "symbol": "\\nu_e",
        "name": "ელექტრონული ნეიტრინო",
        "year": 1956
    }, {
        "symbol": "\\nu_\\mu",
        "name": "მიონური ნეიტრინო",
        "year": 1962
    }, {
        "symbol": "\\Xi",
        "name": "ქსი ბარიონი",
        "year": 1964
    }, {
        "symbol": "u ~ d ~ s",
        "name": "მსუბუქი კვარკები",
        "year": 1969
    }, {
        "symbol": "J/\\Psi",
        "name": "ფსი მეზონი",
        "year": 1974
    }, {
        "symbol": "c",
        "name": "კვარკი",
        "year": 1974
    }, {
        "symbol": "\\tau",
        "name": "ტაუ",
        "year": 1975
    }, {
        "symbol": "\\Upsilon",
        "name": "უფსილონი",
        "year": 1977
    }, {
        "symbol": "b",
        "name": "კვარკი",
        "year": 1977
    }, {
        "symbol": "g",
        "name": "გლუონი",
        "year": 1979
    }, {
        "symbol": "Z ~ W^{\\pm}",
        "name": "ბოზონები",
        "year": 1983
    }, {
        "symbol": "t",
        "name": "კვარკი",
        "year": 1995
    }, {
        "symbol": "\\nu_\\tau",
        "name": "ტაუ ნეიტრინო",
        "year": 2000
    }, {
        "symbol": "H",
        "name": "ჰიგსის ბოზონი",
        "year": 2012
    }
]


class TitleScene(Scene):
    def construct(self):
        title_text = TextMobject("ნაწილაკების ფიზიკა")
        subtitle_text = TextMobject("შესავალი")
        subtitle_text.scale(0.75)
        group = VGroup(title_text, subtitle_text)
        group.arrange(DOWN)
        self.play(Write(title_text))
        self.play(Write(subtitle_text))
        self.wait()
        self.play(Uncreate(title_text), Uncreate(subtitle_text))
        self.wait()


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

        def electron(color=WHITE):
            c1 = Circle(color=color, stroke_width=0, fill_color=color, fill_opacity=.2, radius=0.2)
            c2 = Circle(color=color, stroke_width=0, fill_color=color, fill_opacity=.2, radius=0.4)
            c3 = Circle(color=color, stroke_width=0, fill_color=color, fill_opacity=.2, radius=0.6)
            c4 = Circle(color=color, stroke_width=0, fill_color=color, fill_opacity=.2, radius=0.8)
            c5 = Circle(color=color, stroke_width=0, fill_color=color, fill_opacity=.2, radius=1.0)
            return VGroup(c1, c2, c3, c4, c5)

        def proton(color=RED):
            return Circle(color=color, stroke_width=0, fill_color=color, fill_opacity=.5, radius=0.1)

        def neutron(color=BLUE):
            return Circle(color=color, stroke_width=0, fill_color=color, fill_opacity=.5, radius=0.1)


        def year_tick(year):
            tick = -5 + (year - 1800) / 20
            tick_circle = Circle(arc_center=(tick, 0, 0),
                                 color=pcolor, stroke_width=0, fill_color=pcolor, fill_opacity=.75, radius=0.1)
            tick_circle.shift(0.8*BOTTOM)
            return tick_circle
        timeline = NumberLine(**timelineparams)
        timeline.shift(0.8*BOTTOM)
        timelinetick1 = TexMobject("1800")
        timelinetick1.shift((-5, 0, 0))
        timelinetick1.shift(0.9*BOTTOM)
        timelinetick2 = TexMobject("1900")
        # timelinetick2.shift((0,0,0))
        timelinetick2.shift(0.9*BOTTOM)
        timelinetick3 = TexMobject("2020")
        timelinetick3.shift((6, 0, 0))
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
        separator = int(np.ceil(len(groups)/3))
        verticalgroup1 = VGroup(*groups[:separator-1])
        verticalgroup1.arrange(DOWN)
        verticalgroup2 = VGroup(*groups[separator-1:2*separator-1])
        verticalgroup2.arrange(DOWN)
        verticalgroup3 = VGroup(*groups[2*separator-1:])
        verticalgroup3.arrange(DOWN)
        thewholegroup = VGroup(verticalgroup1, verticalgroup2, verticalgroup3)
        thewholegroup.arrange(RIGHT)
        thewholegroup.scale(0.8)
        thewholegroup.shift(1*LEFT)
        thewholegroup.shift(0.5*UP)

        radiations = ["სითბური გამოსხივება (1800)",
                      "ქიმიური გამოსხივება (1801)",
                      "ულტრაიისფერი გამოსხივება (1895)",
                      "რენტგენის გამოსხივება (1895)"]

        radiation_texts = list()
        for radiation in radiations:
            radiation_texts.append(TextMobject(radiation))
            radiation_texts[-1].scale(0.5)
        radiation_group = VGroup(*radiation_texts)
        radiation_group.arrange(DOWN)

        e1 = electron()
        p1 = proton()
        p1.shift(0.1*UR)
        n1 = neutron()
        n1.shift(0.1*DL)
        atom_text = TextMobject("ატომი")
        atom_text.shift(DOWN)

        alpha = [proton(), proton(), neutron(), neutron()]
        alpha[0].shift(0.075*UR)
        alpha[1].shift(0.075*DL)
        alpha[2].shift(0.075*DR)
        alpha[3].shift(0.075*UL)
        alpha_group = VGroup(*alpha)

        deuterium = [proton(), neutron()]
        deuterium[0].shift(0.05*UR)
        deuterium[1].shift(0.05*DL)
        deuterium_group = VGroup(*deuterium)

        positron_discovery = ImageMobject("PositronDiscovery")
        positron_discovery.shift(RIGHT)
        positron_discovery_frame = Square()
        positron_discovery_frame.surround(positron_discovery)
        positron = electron()
        positron.scale(0.5)
        positron.shift(LEFT)

        muon = electron()
        muon.scale(0.5)

        def display_particle(i, j=None):
            animations = list()
            if not j:
                j = i+1
            for k in range(i, j):
                animations.append(Write(symbols[k]))
                animations.append(Write(names[k]))
                animations.append(GrowFromCenter(ticks[k]))
            return animations

        self.play(ShowCreation(timeline))
        self.play(ShowCreation(timelinetick1), ShowCreation(timelinetick2), ShowCreation(timelinetick3))
        self.wait()
        self.play(*display_particle(0))  # Photon
        self.wait()
        for radiation_text in radiation_texts:
            self.play(Write(radiation_text))
        self.wait()
        self.play(*[Uncreate(radiation_text) for radiation_text in radiation_texts])
        self.wait()
        self.play(GrowFromCenter(e1), GrowFromCenter(p1), GrowFromCenter(n1), Write(atom_text))
        self.wait()
        self.play(*display_particle(1),  # Electron
                  ApplyMethod(e1.move_to, names[1].get_right()+0.2*RIGHT),
                  Uncreate(atom_text))
        self.play(*display_particle(2, 4),  # Alpha and Proton
                  ApplyMethod(p1.move_to, names[3].get_right()+0.2*RIGHT))
        self.play(*display_particle(4, 6),  # Deuterium and Neutron
                  ApplyMethod(n1.move_to, names[5].get_right()+0.2*RIGHT))
        self.wait()
        alpha_group.move_to(names[2].get_right() + 0.2*RIGHT)
        deuterium_group.move_to(names[4].get_right() + 0.2*RIGHT)
        self.play(GrowFromCenter(alpha_group), GrowFromCenter(deuterium_group), ApplyMethod(e1.scale, 0.5))
        self.wait()
        self.play(FadeIn(positron_discovery), ShowCreation(positron_discovery_frame))
        self.wait()
        self.play(GrowFromCenter(positron))
        self.wait()
        self.play(FadeToColor(positron, RED))
        self.wait()
        self.play(*display_particle(6),  # Positron
                  ApplyMethod(positron.move_to, names[6].get_right() + 0.2*RIGHT))
        self.wait()
        self.play(Uncreate(positron_discovery_frame), FadeOut(positron_discovery))
        self.wait()
        self.play(GrowFromCenter(muon))
        self.wait()
        self.play(ApplyMethod(muon.scale, 2))
        self.wait()
        self.play(*display_particle(7),  # Muon
                  ApplyMethod(muon.move_to, names[7].get_right() + 0.2*RIGHT))
        self.wait()
        objects_to_remove = [e1, p1, n1, alpha_group, deuterium_group, positron, muon]
        self.play(*[ShrinkToCenter(o) for o in objects_to_remove])
        self.wait()
        self.play(AnimationGroup(*display_particle(8, len(names)), lag_ratio=0.05))  # The rest.
        self.wait()
        self.play(*[Uncreate(names[i]) for i in range(len(names))])
        symbolsgroup = VGroup(*symbols)
        self.play(ApplyMethod(symbolsgroup.scale, 0.8))
        self.play(ApplyMethod(symbolsgroup.arrange, RIGHT))
        timelinegroup = VGroup(timeline, timelinetick1, timelinetick2, timelinetick3, *ticks)
        self.play(ApplyMethod(symbolsgroup.shift, 0.8*BOTTOM), FadeOut(timelinegroup))
        self.wait()
