from manim import *



        

class Introduction(Scene):
    def get_sine_wave(self,dx=0):
        return FunctionGraph(
            lambda x: np.sin((x+dx),)
        )
    def construct(self):
        analog_vs_digital = Text("Analog & Digital Signal")
        self.play(Create(analog_vs_digital.to_edge(UP)))
        sin_func = FunctionGraph(lambda x : np.sin(x),color=RED)
        sin_func.next_to(analog_vs_digital,4*DOWN);
        self.play(Create(sin_func,run_time=2))
        binary = Text("\n\n\n010101010101010\n010101010101010\n010101010101010\n010101010101010\n").scale(0.75)
        binary.next_to(sin_func,5*DOWN);
        self.play(Create(binary))
        self.wait(5)
        self.play(Indicate(sin_func),run_time=2)
        self.play(Indicate(binary),run_time=2)
        self.play(FadeOut(sin_func,binary,analog_vs_digital,shift=DOWN * 2, scale=1.5))
        self.wait(3)