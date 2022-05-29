from manim import *


class Presentation(Scene):
    def construct(self):
        title = Text("Black & Scholes", color=PURPLE)
        # title.scale(0.75)
        self.add(title.to_edge(UP))

        a = MathTex(
            r"\text{Valor presente de la acción: }",
            r"X(0) = x_{0}"
        )
        b = MathTex(
            r"\text{Precio de la acción a tiempo t: }",
            r"X(t)"
        )
        c = MathTex(
            r"\text{Estamos interesados en la acción en el intervalo }",
            r"[0, T]"
        )
        e = MathTex(
            r"\text{El valor presente de la acción a tiempo t: }",
            r"e^{-\alpha t}",
            r"X(t)"
        )
        e[1].set_color(YELLOW)


        self.add(VGroup(a, b, c, e).arrange(DOWN, buff=1, aligned_edge=LEFT))

        self.wait(22)
        self.clear()

        e = MathTex(
            r"\text{El valor presente de la acción a tiempo t: }",
            r"e^{-\alpha t}",
            r"X(t)"
        )
        e[1].set_color(YELLOW)

        self.play(Write(e))
        self.wait(5)
        self.clear()

        f = MathTex(
            r"X(t),\ ",
            "0 \leq t \leq T",
        )
        f[0].set_color(YELLOW)
        self.add(f)
        self.wait(5)
        self.clear()

        g = Tex(
            r"\justifying{Queremos encontrar los valores de} ",
            r"$c_{i}$",
            r" \justifying{tales que no exista una estrategia que garantice una ganancia}",
        )

        h = Tex(
            r"\justifying{De esto se sigue que no habrá tal estrategia si y solo si existe una medida de probabilidad sobre el conjunto de posibilidades tal que el total de las apuestas tenga esperanza de retorno 0}",
        )


        self.add(VGroup(g, h).arrange(DOWN, buff=1, aligned_edge=LEFT))
        self.wait(5)
        self.clear()

        i = MathTex(
            r"\mathbb{E}_{\textbf{P}}[e^{-\alpha t} X(t) | X(u), 0 \leq u \leq s] = e^{-\alpha s} X(s)"
        )


        j = MathTex(
            r"X(t) - K, \quad &\text{si } X(t) \ge K"
        )
        k = MathTex(
            r"0,  \quad &\text{si } X(t) \ge K"
        )
        eq1 = VGroup(j, k).arrange(DOWN, buff=1, aligned_edge=LEFT)
        br = Brace(eq1, direction=[-1,0])
        text1 = Text("el valor de la opción a tiempo t: ").next_to(br, LEFT)

        self.add(Group(eq1, br, text1).arrange(LEFT).scale(0.8))
        # self.add(eq1)
        # self.add(br)
        # self.add(text1)
        self.wait(5)

        l = MathTex(
            r"\mathbb{E}_{\textbf{P}}[e^{-\alpha t}\left( X(t) - K \right)^{+}] = c"
        )
        self.add(l)
        self.wait(5)

        m = MathTex(
            r"c_{i} = \mathbb{E}_{\textbf{P}}[e^{-\alpha t_{i}}\left( X(t_{i}) - K_{i} \right)^{+}], \quad i = 1, \dots, N"
        )
        self.add(m)
        self.wait(5)


class Test(Scene):
    def construct(self):
        n = MathTex(
            r""
        )
        self.add(n)
        self.wait(5)

class diapositiva2(Scene):
    def construct(self):
        a = Tex(r"\justifying{Suponiendo que tenemos opciones compradas a tiempo 0, la opción tiene costo }",
                 r"\justifying{c}",
                 r"\justifying{ por acción, lo que nos dará la opción de comprar acciones a tiempo }",
                 r"\justifying{t}",
                 r"\justifying{, por el precio fijo }",
                 r"\justifying{K}",
                 r"\justifying{ por cada una de las acciones.}"
        ).scale(0.8)
        a[1].set_color(YELLOW)
        a[3].set_color(BLUE)
        a[5].set_color(PURPLE)
        self.play(Write(a))
        self.wait(15)

class diapositiva3(Scene):
    def construct(self):
        a = Tex(r"\justifying{De esto se sigue que no habrá una estrategia financiera que garantice un retorno positivo si y solo si existe una medida de probabilidad P sobre el conjunto de posibilidades tal que el total de las apuestas tenga esperanza de retorno 0}").scale(0.8)
        b = MathTex(
                r"\mathbb{E}_{\textbf{P}}[e^{-\alpha t} X(t) | X(u), 0 \leq u \leq s] = e^{-\alpha s} X(s) \quad (1)"
            )

        self.play(Write(VGroup(a, b).arrange(DOWN, buff=1)))
        self.wait(15)

class diapositiva4(Scene):
    def construct(self):
        eq1 = MathTex(r"X(t) - K, \quad &\text{si } X(t) \ge K\\ 0,  \quad &\text{si } X(t) < K")
        br = Brace(eq1, direction=[-1,0])
        text1 = Tex(r"\justifying{Dado que tenemos un call a tiempo t por un precio K, el valor de la opción al tiempo t está dado por: }").next_to(br, LEFT)
        e = Group(eq1, br).arrange(LEFT).scale(0.8)
        f = Group(text1, e).arrange(DOWN, buff = 2).scale(0.8)
        self.add(f)
        self.wait(15)
        self.play(FadeOut(f))

        a = MathTex(r"\left( X(t) - K \right)^{+}")
        b = Text("Por lo tanto, el valor presente de la opción es: ")
        c = MathTex(r"e^{-\alpha t}\left( X(t) - K \right)^{+}")
        self.play(Write(VGroup(a, b, c).arrange(DOWN, buff=1)))

        self.wait(13)

class diapositiva5(Scene):
    def construct(self):

        a = Tex(r"\justifying{Si c es el costo de la opción a tiempo 0, y queremos tener un retorno de la opción esperado igual a 0, necesitamos que:}").scale(0.8)

        b = MathTex(r"\mathbb{E}_{\textbf{P}}[e^{-\alpha t}\left( X(t) - K \right)^{+}] = c \quad (2)")
        c = Group(a, b).arrange(DOWN, buff=2)
        self.add(c)

        self.wait(13)

class diapositiva6(Scene):
    def construct(self):
        a = Tex(r"\justifying{Por el teorema de arbitraje, si podemos encontrar una medida de probabilidad $\textbf{P}$ en el conjunto de resultados que satisfaga la ecuación}").scale(0.8)
        b = MathTex(r"\mathbb{E}_{\textbf{P}}[e^{-\alpha t} X(t) | X(u), 0 \leq u \leq s] = e^{-\alpha s} X(s) \quad (1)")
        c = Tex(r"\justifying{y si c está dado como en la ecuación}")
        d = MathTex(r"\mathbb{E}_{\textbf{P}}[e^{-\alpha t}\left( X(t) - K \right)^{+}] = c \quad (2)")
        e = Tex(r"\justifying{entonces no es posible que haya arbitraje.}")
        f = Group(a, b, c, d, e).arrange(DOWN, buff=1)
        self.add(f)
        self.wait(16)

class diapositiva7(Scene):
    def construct(self):

        a = Tex(r"\justifying{A continuación presentamos una medida de probabilidad $\textbf{P}$ en el resultado $X(t),\quad 0 \leq t \leq T$ que satisface la ecuación (1)}").scale(0.8)
        b = Tex(r"Supongamos que")
        c = MathTex(r"X(t) = x_{0}e^{Y(t)}")
        d = Tex(r"Donde $\{Y(t),\ t\geq 0\}$ es un proceso de movimiento Browniano con coeficiente de deriva $\mu$ y varianza $\sigma^2$. Por lo que $\{X(t),\ t\geq 0\}$ es un proceso Browniano geométrico.").scale(0.8)
        e = Group(a, b, c, d).arrange(DOWN, buff=1)
        self.add(e)
        self.wait(26)
