from manim import *


class convolution(Scene):
    def construct(self):
        title = Text("Convolution")
        self.play(Create(title.to_edge(UP)))
        definition = Tex("According to Wolfram Mathworld,\nA convolution is an integral that expresses the amount of overlap\nof one function \(g\) as it is shifted over another function \(f\)").scale(0.5)
        definition.next_to(title,DOWN*2)
        equation = Tex("\( f * g = \int_{0}^{t} f(x)g(t-x)dx \)")
        equation.next_to(definition,DOWN*2)
        self.play(Create(definition))
        self.play(Create(equation))
        self.wait(7)

        waittext = Paragraph("I'm not going to prove the math.\nI'll just give you the \nintuition about what is actually a convolution",alignment='center').scale(0.6)
        waittext.next_to(equation,DOWN*4)
        self.play(Create(waittext))
        self.wait(7)

        # flush the screen
        self.play(FadeOut(title,definition,waittext,equation,shift=DOWN * 2, scale=1.5))

        self.wait(1)

        oil = Paragraph("Let assume that we are an oil company and we have function\nf(x) as the number of new well that we opened at time -x and\ng(x) as the number of oil that a well produce\n at x-th time since it's been built ",alignment='center').scale(0.4)
        self.play(Create(oil))
        self.wait(12)
        oiltransform = Paragraph("f(x) as the number of new oil well that opened at time -x\n g(x) as the number of oil-well that an oil-well produce at time - x since it's been built\n and also assuming that the g(x) is same for all well",alignment='center').scale(0.4)
        self.play(Transform(oil,oiltransform.to_edge(UP)))
        self.wait(7)

        # do some simulation at 0, 1, and 2
        t1 = Tex("At time 0").scale(0.6)
        t1.next_to(oiltransform,DOWN*3)
        t1exp = MathTex(r"total \ oil = f(0) \cdot  g(0)").scale(0.6)
        t1exp.next_to(t1,DOWN)

        self.play(Create(t1))
        self.play(Create(t1exp))
        

        t2 = Tex("At time 1").scale(0.6)
        t2.next_to(t1exp,DOWN)
        t2exp = MathTex(r"total \ oil = f(1) \cdot g(0) + f(0) \cdot g(1)").scale(0.6)
        t2exp.next_to(t2,DOWN)

        self.play(Create(t2))
        self.play(Create(t2exp))


        t3 = Tex("At time 3").scale(0.6)
        t3.next_to(t2exp,DOWN)
        t3exp = MathTex(r"total \ oil = f(2) \cdot g(0) + f(1) \cdot g(1) + f(0) \cdot g(2)").scale(0.6)
        t3exp.next_to(t3,DOWN) 
        self.play(Create(t3))

        t4 = Text("Let visualize it so you can see the whole picture").scale(0.8)
        t4.next_to(t3,DOWN*4)
        self.play(Create(t4))
        self.wait(3)

        # flush the character or 
        self.play(FadeOut(oil,oiltransform,t1,t1exp,t2,t2exp,t3,t3exp,t4,shift=DOWN * 2, scale=1.5))

        fchart = BarChart(
            values = [1,2,3],
            y_range = [0,10,5],
            bar_names=[0,1,2],
            bar_colors=[WHITE]
        ).scale(0.5).to_edge(RIGHT,buff=0.5)

        fchartname = Text("The number of new well that\nwe opened at time -x").next_to(fchart,UP).scale(0.4).to_edge(RIGHT,buff=0.5)

        gchart = BarChart(
            values = [10, 3,2],
            y_range= [0,15,5],
            bar_names=[0,1,2],
            bar_colors=[WHITE]
        ).scale(0.5).to_edge(LEFT,buff=0.5)

        gchartname = Text("The number of oil that a well produce\nat time - x since it's been built").next_to(fchart,UP).scale(0.4).to_edge(LEFT,buff=0.5)
        
        totchart = BarChart(
            values = [10,23,38],
            y_range = [0,40,10],
            bar_names=[0,1,2],
            bar_colors=[WHITE]
        ).to_edge(UP).scale(0.5)
        totchartname = Text("Total of oil production at i-th day").next_to(totchart,UP).scale(0.4)

       # gchart.next_to(totchart,DOWN*2)
      #  fchart.next_to(totchart,DOWN*2)

        
        self.play(Create(totchart),Create(totchartname))
        self.play(Create(gchart),Create(gchartname))
        self.play(Create(fchart),Create(fchartname))



        self.play(Indicate(gchart.submobjects[0][0],color=RED),Indicate(fchart.submobjects[0][0],color=RED),Indicate(totchart.submobjects[0][0],color=GREEN),run_time=12)
        self.play(Indicate(gchart.submobjects[0][0],color=RED),Indicate(fchart.submobjects[0][1],color=RED),Indicate(gchart.submobjects[0][1],color=ORANGE),Indicate(fchart.submobjects[0][0],color=ORANGE),Indicate(totchart.submobjects[0][1],color=GREEN),run_time=12)
        self.play(Indicate(gchart.submobjects[0][0],color=RED),Indicate(fchart.submobjects[0][2],color=RED),
                  Indicate(gchart.submobjects[0][1],color=ORANGE),Indicate(fchart.submobjects[0][1],color=ORANGE),
                  Indicate(gchart.submobjects[0][2],color=YELLOW),Indicate(fchart.submobjects[0][0],color=YELLOW),Indicate(totchart.submobjects[0][2],color=GREEN),run_time=12)
        self.wait(10)

        self.play(FadeOut(gchart,gchartname,fchart,fchartname,totchart,totchartname),shift=DOWN * 2, scale=1.5)
        self.wait(1)
        ## start to indicate each







        



