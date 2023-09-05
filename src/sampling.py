from manim import *

class Sampling(Scene):
    def construct(self):
        vgroup = VGroup()
        title = Text("Sampling")
        self.play(Create(title.to_edge(UP)))
        ax = Axes(x_range=(-6,6),y_range=(-1.5,1.5)).scale(0.8)
        curve = ax.plot(lambda x : np.sin(x-0.5),color=YELLOW)
        self.play(Create(ax,run_time=2),Create(curve,run_time=3))
        for i in range(-5,5):
            point = Dot(color=RED).move_to(ax.c2p(i,np.sin(i-0.5)))
            vgroup.add(point)

        #self.wait(3)
        # flush all of tem
        self.play(Create(vgroup),run_time=3)
        self.wait(1)
        self.play(FadeOut(curve, shift=DOWN * 2, scale=1.5))
        self.wait(3)
        self.play(FadeOut(vgroup, shift=DOWN * 2, scale=1.5))
        self.play(FadeOut(title,ax, shift=DOWN * 2, scale=1.5))
        

        # explain the mathematic side

        title = Text("More formally, sampling is \n mathematically defined as ").scale(0.9)
        self.play(Create(title.to_edge(UP)))
        mat = Tex("\( x_s(i) = x(i T)\) for \(1 \leq i \le n\)")
        mat.next_to(title,DOWN*4)
        text_i = Tex("where\n\n\n\n T is the sampling period and\n\n").scale(0.6)
        text_i2 = Tex("n is the number of sample that we take and").scale(0.6)
        text_i3 = Tex("\(x_s(i) \) is the amplitude of the signal at the time i ").scale(0.6)
        text_i.next_to(mat,DOWN*4)
        text_i2.next_to(text_i,DOWN)
        text_i3.next_to(text_i2,DOWN)
        self.play(Create(mat))
        self.play(Create(text_i))
        self.play(Create(text_i2))
        self.play(Create(text_i3))
        self.wait(5)

        self.play(FadeOut(title,mat,text_i,text_i2,text_i3,shift=DOWN * 2, scale=1.5))

        # continue to the nyquuist rate
        title = Text("So, how do we know the exact number that we should use as n?").scale(0.7)
        self.play(Create(title.to_edge(UP)))
        subt = Text("If we under sample the signal").scale(0.6)
        subt.next_to(title,DOWN*2)
        self.wait(2)
        self.play(Create(subt))

        # create the simulation
        ax = Axes(x_range=(-6,6),y_range=(-1.5,1.5)).scale(0.8)
        ax.next_to(subt,DOWN*2)
        curve = ax.plot(lambda x : np.sin(x-0.5),color=YELLOW)
        self.play(Create(ax,run_time=2),Create(curve,run_time=3))
        vgroup = VGroup()
        for i in range(-5,6,5):
            point = Dot(color=RED).move_to(ax.c2p(i,np.sin(i-0.5)))
            vgroup.add(point)

        self.play(Create(vgroup),run_time=3)
        self.play(FadeOut(curve,shift=DOWN * 2, scale=1.5))
        self.wait(1)
        self.play(FadeOut(vgroup, shift=DOWN * 2, scale=1.5))
        self.play(Create(curve))

        # create the 
        newtitle = Text("If we over sample the signal").scale(0.6)
        newtitle.next_to(title,DOWN*2)
        self.play(Transform(subt,newtitle))
        vgroup = VGroup()
        for i in range(-5,5):
            point = Dot(color=RED).move_to(ax.c2p(i,np.sin(i-0.5)))
            vgroup.add(point)

        self.play(Create(vgroup),run_time=3)
        self.play(FadeOut(curve,shift=DOWN * 2, scale=1.5))
        self.wait(1)
        self.play(FadeOut(vgroup, shift=DOWN * 2, scale=1.5))
        self.wait(1)

        # flush the screen

        self.play(FadeOut(title,subt,ax,shift=DOWN * 2, scale=1.5))

        conc = Text("So, what number should we use for the n?").scale(0.6)
        self.play(FadeIn(conc))
        self.wait(1)
        self.play(FadeOut(conc))
        self.wait(1)
        





            
        
        
        
        
        


