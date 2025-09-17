from manim import *
import numpy as np

class Waves(Scene):
    def construct(self):
        a = Axes(x_range=[-1, 10], y_range=[-1, 10])

        graph = a.plot(lambda x: np.sin(x), color=BLUE)

        self.add(graph, a)