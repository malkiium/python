from manim import *  # type: ignore

class imager(Scene):
    def construct(self):
        m = SVGMobject("images/file.svg").shift(UP)
        t = Text("Nebula").next_to(m, DOWN)

        self.play(DrawBorderThenFill(m, run_time=2))  # animate the SVG
        self.play(Write(t))  # animate the text
        self.wait(2)