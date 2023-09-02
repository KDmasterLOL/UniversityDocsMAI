from manim import *


class CreateCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency
        self.play(Create(circle))  # show the circle on screen


class SquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set color and transparency

        square = Square()  # create a square
        square.rotate(PI / 4)  # rotate a certain amount

        self.play(Create(square))  # animate the creation of the square
        self.play(Transform(square, circle))  # interpolate the square into the circle
        self.play(FadeOut(square))  # fade out animation


class SquareAndCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        circle.set_fill(PINK, opacity=0.5)  # set the color and transparency

        square = Square()  # create a square
        square.set_fill(BLUE, opacity=0.5)  # set the color and transparency

        square.next_to(circle, RIGHT, buff=0.5)  # set the position
        self.play(Create(circle), Create(square))  # show the shapes on screen


class AnimatedSquareToCircle(Scene):
    def construct(self):
        circle = Circle()  # create a circle
        square = Square()  # create a square

        self.play(Create(square))  # show the square on screen
        self.play(square.animate.rotate(PI / 4))  # rotate the square
        self.play(
            ReplacementTransform(square, circle)
        )  # transform the square into a circle
        self.play(
            circle.animate.set_fill(PINK, opacity=0.5)
        )  # color the circle on screen


class DifferentRotations(Scene):
    def construct(self):
        left_square = Square(color=BLUE, fill_opacity=0.7).shift(2 * LEFT)
        right_square = Square(color=GREEN, fill_opacity=0.7).shift(2 * RIGHT)
        self.play(
            left_square.animate.rotate(PI), Rotate(right_square, angle=PI), run_time=2
        )
        self.wait()


from manim import *


class CoordSysExample(Scene):
    def construct(self):
        # the location of the ticks depends on the x_range and y_range.
        grid = Axes(
            x_range=[0, 1, 0.05],  # step size determines num_decimal_places.
            y_range=[0, 1, 0.05],
            x_length=9,
            y_length=5.5,
            axis_config={
                "numbers_to_include": np.arange(0, 1 + 0.1, 0.1),
                "font_size": 24,
            },
            tips=False,
        )

        # Labels for the x-axis and y-axis.
        y_label = grid.get_y_axis_label("y", edge=LEFT, direction=LEFT, buff=0.4)
        x_label = grid.get_x_axis_label("x")
        grid_labels = VGroup(x_label, y_label)

        graphs = VGroup()
        for n in np.arange(1, 20 + 0.5, 0.5):
            graphs += grid.plot(lambda x: x**n, color=WHITE)
            graphs += grid.plot(
                lambda x: x ** (1 / n), color=WHITE, use_smoothing=False
            )

        # Extra lines and labels for point (1,1)
        graphs += grid.get_horizontal_line(grid.c2p(1, 1, 0), color=BLUE)
        graphs += grid.get_vertical_line(grid.c2p(1, 1, 0), color=BLUE)
        graphs += Dot(point=grid.c2p(1, 1, 0), color=YELLOW)
        graphs += Tex("(1,1)").scale(0.75).next_to(grid.c2p(1, 1, 0))
        title = Title(
            # spaces between braces to prevent SyntaxError
            r"Graphs of $y=x^{ {1}\over{n} }$ and $y=x^n (n=1,2,3,...,20)$",
            include_underline=False,
            font_size=40,
        )

        self.add(title, graphs, grid, grid_labels)


class PolygonOnAxes(Scene):
    def get_rectangle_corners(self, bottom_left, top_right):
        return [
            (top_right[0], top_right[1]),
            (bottom_left[0], top_right[1]),
            (bottom_left[0], bottom_left[1]),
            (top_right[0], bottom_left[1]),
        ]

    def construct(self):
        ax = Axes(
            x_range=[0, 10],
            y_range=[0, 10],
            x_length=6,
            y_length=6,
            axis_config={"include_tip": False},
        )

        t = ValueTracker(5)
        k = 25

        graph = ax.plot(
            lambda x: k / x,
            color=YELLOW_D,
            x_range=[k / 10, 10.0, 0.01],
            use_smoothing=False,
        )

        def get_rectangle():
            polygon = Polygon(
                *[
                    ax.c2p(*i)
                    for i in self.get_rectangle_corners(
                        (0, 0), (t.get_value(), k / t.get_value())
                    )
                ]
            )
            polygon.stroke_width = 1
            polygon.set_fill(BLUE, opacity=0.5)
            polygon.set_stroke(YELLOW_B)
            return polygon

        polygon = always_redraw(get_rectangle)

        dot = Dot()
        dot.add_updater(lambda x: x.move_to(ax.c2p(t.get_value(), k / t.get_value())))
        dot.set_z_index(10)

        self.add(ax, graph, dot)
        self.play(Create(polygon))
        self.play(t.animate.set_value(10))
        self.play(t.animate.set_value(k / 10))
        self.play(t.animate.set_value(5))


class MyGraph(Scene):
    def construct(self):
        ax = Axes(x_range=[0, 10], y_range=[0, 10], x_length=10, y_length=6)
        s_1 = ValueTracker(0)
        s_2 = ValueTracker(0)
        get_func_1 = lambda: ax.plot(
            lambda x: 2 - x - s_1.get_value(),
            x_range=[0, 30, 1],
            color=WHITE,
            use_smoothing=False,
        )
        get_func_2 = lambda: ax.plot(
            lambda x: 3 - x * 3 - s_2.get_value(),
            x_range=[0, 30, 1],
            color=YELLOW,
            use_smoothing=False,
        )
        func_1 = get_func_1().add_updater(lambda mob: mob.become(get_func_1()))
        func_2 = get_func_2().add_updater(lambda mob: mob.become(get_func_2()))

        # labels = [MathTex("y+x+s_1=2"), MathTex("2y+x+s_2=2")]

        labels = (
            Group(MathTex("y+x+s_1=2"), MathTex("y+3x+s_2=3"))
            .arrange(DOWN)
            .move_to([4, 2.5, 0])
        )

        vars = (
            Group(
                Variable(
                    s_1.get_value(), MathTex("s_1"), num_decimal_places=3
                ).add_updater(lambda v: v.tracker.set_value(s_1.get_value())),
                Variable(
                    s_2.get_value(), MathTex("s_2"), num_decimal_places=3
                ).add_updater(lambda v: v.tracker.set_value(s_2.get_value())),
            )
            .arrange(LEFT)
            .next_to(labels, DOWN)
        )

        lines = [
            Line([0, 0, 0], [0.2, 0, 0], color=YELLOW).next_to(labels[0], LEFT),
            Line([0, 0, 0], [0.2, 0, 0]).next_to(labels[1], LEFT),
        ]
        self.add(ax, func_1, func_2, labels, vars, *lines)
        self.play(s_1.animate.set_value(2))
        self.play(s_2.animate.set_value(2))
        self.play(Wait(1))


if __name__ == "__main__":
    with tempconfig({"quality": "low_quality", "preview": True}):
        scene = MyGraph()
        scene.render()
