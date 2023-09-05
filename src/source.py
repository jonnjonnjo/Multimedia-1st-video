from manim import *

class Source(Scene):
    def construct(self):
        title = Paragraph("List of source : ",alignment='center').to_edge(UP)
        self.play(Create(title))
        listofit = Paragraph("- Multimedia Systems Algorithms, Standards, and Industry Practices (Parag Havaldar and Gerard Medioni)\n-	Nyquist Theorem – Tech Target\n-	What is convolution? This is the easiest way to understand – Discretised\n-	But what is a convolution? – 3Blue1Brown",alignment='center').scale(0.5)
        listofit.next_to(title,DOWN*2)
        self.play(Create(listofit))
        self.wait(3)



