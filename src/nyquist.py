from manim import *

class nyquist(Scene):
    def construct(self):
        title = Text("Nyquist Rate")
        self.play(Create(title.to_edge(UP)))
        expl = Paragraph("In signal processing, the Nyquist rate, named after Harry \n\nNyquist, is a value (in units of samples per second or hertz, Hz)\n\n equal to twice the highest frequency (bandwidth) of a given\n\nfunction or signal.",alignment='center').scale(0.5)
        expl.next_to(title,DOWN*6)
        self.play(Create(expl))
        self.wait(2)
        prf = Paragraph("I'm not going too deeply about the math.\n\nI'll prove it to you by an example",alignment='center').scale(0.5)
        prf.next_to(expl,DOWN*3)
        self.play(Create(prf))
        self.wait(3)
        self.play(FadeOut(title,expl,prf,shift=DOWN * 2, scale=1.5))
        self.wait(1)

        title = Text("Consider this signal").scale(0.6)
        self.play(Create(title.to_edge(UP)))
        fn = Tex("\(y = sin(2x)\)")
        fn.next_to(title,DOWN*3)
        self.play(Create(fn))
        ax = Axes(x_range=(-6,6),y_range=(-1.5,1.5)).scale(0.8)
        ax.next_to(fn,DOWN*2)
        curve = ax.plot(lambda x : np.sin(2*x),color=YELLOW)
        self.play(Create(ax,run_time=2),Create(curve,run_time=3))   

        newtitle = Text("According to Nyquist, we should sampled the signal 4 times").scale(0.6)
        newfn = Text("But, let sample it 2 times and 4 times")
        newtitle = newtitle.to_edge(UP)
        newfn.next_to(newtitle,DOWN)
        self.play(Transform(title,newtitle),run_time=1.5)
        self.play(Transform(fn,newfn))

        vgroup2 = VGroup()
        for i in range(int(-3*2),int(-2*2),1):
            ti = i
            point = Dot(color=RED).move_to(ax.c2p(ti,np.sin(2*ti)))
            vgroup2.add(point)

        vgroup4 = VGroup()
        for i in range(int(0),int(4)):
            ti = i
            point = Dot(color=GREEN).move_to(ax.c2p(ti,np.sin(2*ti)))
            vgroup4.add(point)

        self.play(Create(vgroup2))
        self.play(Create(vgroup4))
        self.wait(1)
        self.play(FadeOut(curve,shift=DOWN * 2, scale=1.5))
        self.wait(3)

        # 

        self.play(Indicate(vgroup2))
        self.wait(2)
        self.play(Indicate(vgroup4))
        self.wait(3)

        # flush all of them
        
        self.play(FadeOut(title,fn,vgroup2,vgroup4,ax,shift=DOWN * 2, scale=1.5))





