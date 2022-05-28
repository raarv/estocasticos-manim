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
        d = MathTex(
            r"\text{Asumimos que el factor de descuento es }",
            r"\alpha"
        )

        self.add(VGroup(a, b, c, d).arrange(DOWN, buff=1, aligned_edge=LEFT))

        self.wait(5)
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
            r"X(t) - K, \quad &\text{if } X(t) \ge K"
        )
        k = MathTex(
            r"0,  \quad &\text{if } X(t) \ge K"
        )
        eq1 = VGroup(j, k).arrange(DOWN, buff=1, aligned_edge=LEFT)
        br = Brace(eq1, direction=[-1,0])
        text1 = Text("el valor de la opción a tiempo t: ").next_to(br, LEFT)

        self.add(Group(eq1, br, text1).arrange(LEFT).scale(0.8))
        # self.add(eq1)
        # self.add(br)
        # self.add(text1)
        self.wait(5)

        # l = MathTex(
        #     r"\mathbb{E}_{\textbf{P}[e^{-\alpha t}\left( X(t) - K)^{+}] = c"
        # )
