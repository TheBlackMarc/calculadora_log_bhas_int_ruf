#calculadora 3.5

import tkinter as tk
from tkinter import messagebox
import math
import sympy as sp

# ============================================================
# BlackCalculator Neon Glass 3.5
# ============================================================

APP_TITLE = "BlackCalculator 3.5"
WIDTH = 1920
HEIGHT = 1080

# =========================
# PALETA DE COLORES
# =========================
BG = "#0a0f1f"         # fondo general
BG_2 = "#0f172a"       # fondo secundario
CARD = "#111827"       # panel principal
CARD_2 = "#0b1220"     # panel interno
TEXT = "#e5f3ff"       # texto principal
MUTED = "#94a3b8"      # texto secundario
NEON = "#00e5ff"       # cian neón
NEON_2 = "#7c3aed"     # violeta neón
SUCCESS = "#22c55e"    # verde
ERROR = "#ef4444"      # rojo
WARNING = "#f59e0b"

FONT = "Segoe UI"

# Variable simbólica para integrales
x = sp.symbols("x")


# ============================================================
# COMPONENTES VISUALES
# ============================================================

class NeonEntry(tk.Frame):
    """
    Entry con borde neón.
    """
    def __init__(self, master, width=260):
        super().__init__(master, bg=NEON, bd=0, highlightthickness=0)
        self.inner = tk.Frame(self, bg=CARD_2, bd=0)
        self.inner.pack(fill="both", expand=True, padx=1, pady=1)

        self.entry = tk.Entry(
            self.inner,
            bg=CARD_2,
            fg=TEXT,
            insertbackground=NEON,
            relief="flat",
            bd=0,
            font=(FONT, 12),
            width=max(10, width // 10)
        )
        self.entry.pack(fill="both", expand=True, padx=12, pady=10)

    def get(self):
        return self.entry.get()

    def clear(self):
        self.entry.delete(0, tk.END)


class NeonButton(tk.Button):
    """
    Botón con hover tipo neon.
    """
    def __init__(self, master, text, command, big=False):
        super().__init__(
            master,
            text=text,
            command=command,
            bg=CARD,
            fg=TEXT,
            activebackground=NEON_2,
            activeforeground="white",
            relief="flat",
            bd=0,
            cursor="hand2",
            font=(FONT, 12, "bold" if big else "normal"),
            padx=18,
            pady=12 if big else 10,
        )

        self.default_bg = CARD
        self.hover_bg = "#172554"

        self.bind("<Enter>", lambda e: self.config(bg=self.hover_bg))
        self.bind("<Leave>", lambda e: self.config(bg=self.default_bg))


class GlassCard(tk.Frame):
    """
    Panel con borde neón simulando tarjeta glass.
    """
    def __init__(self, master, glow_color=NEON, inner_bg=CARD, **kwargs):
        super().__init__(master, bg=glow_color, bd=0, highlightthickness=0, **kwargs)
        self.inner = tk.Frame(self, bg=inner_bg, bd=0)
        self.inner.pack(fill="both", expand=True, padx=1, pady=1)


# ============================================================
# APP PRINCIPAL
# ============================================================

class CalculadoraApp:
    def __init__(self, root):
        self.root = root
        self.root.title(APP_TITLE)
        self.root.geometry(f"{WIDTH}x{HEIGHT}")
        self.root.minsize(1100, 700)
        self.root.configure(bg=BG)

        # Transparencia ligera general
        try:
            self.root.attributes("-alpha", 0.98)
        except Exception:
            pass

        # Intento de blur/acrylic en Windows (si está pywinstyles)
        self.try_windows_blur()

        self.result_label = None

        self.build_background()
        self.build_layout()
        self.show_home()

    # ========================================================
    # EFECTO GLASS / BLUR EN WINDOWS
    # ========================================================
    def try_windows_blur(self):
        """
        Intenta aplicar estilo acrylic/blur si pywinstyles está instalado.
        Si no lo está, la app igual funciona con el estilo neon.
        """
        try:
            import pywinstyles
            pywinstyles.apply_style(self.root, "acrylic")
        except Exception:
            pass

    # ========================================================
    # FONDO DECORATIVO
    # ========================================================
    def build_background(self):
        self.bg_canvas = tk.Canvas(
            self.root,
            bg=BG,
            highlightthickness=0,
            bd=0
        )
        self.bg_canvas.place(relx=0, rely=0, relwidth=1, relheight=1)

        # Manchas/glow decorativas
        self.bg_canvas.create_oval(-120, -100, 380, 340, fill="#0b2d5c", outline="")
        self.bg_canvas.create_oval(780, -120, 1240, 280, fill="#24114f", outline="")
        self.bg_canvas.create_oval(820, 480, 1280, 980, fill="#082f49", outline="")
        self.bg_canvas.create_oval(-160, 500, 300, 980, fill="#102a43", outline="")

    # ========================================================
    # ESTRUCTURA GENERAL
    # ========================================================
    def build_layout(self):
        self.main = tk.Frame(self.root, bg=BG)
        self.main.place(relx=0.03, rely=0.04, relwidth=0.94, relheight=0.92)

        # ================= Barra superior =================
        top = GlassCard(self.main, glow_color=NEON, inner_bg="#0b1220")
        top.place(relx=0, rely=0, relwidth=1, relheight=0.11)

        top_inner = top.inner

        tk.Label(
            top_inner,
            text="⚡ BlackCalculator 3.5",
            bg="#0b1220",
            fg=TEXT,
            font=(FONT, 22, "bold")
        ).pack(side="left", padx=24, pady=18)

        tk.Label(
            top_inner,
            text="Calculadora de funciones avanzadas",
            bg="#0b1220",
            fg=MUTED,
            font=(FONT, 11)
        ).pack(side="left", pady=18)

        # ================= Sidebar =================
        sidebar = GlassCard(self.main, glow_color=NEON, inner_bg="#0b1220")
        sidebar.place(relx=0, rely=0.14, relwidth=0.26, relheight=0.86)
        self.sidebar = sidebar.inner

        tk.Label(
            self.sidebar,
            text="MÓDULOS",
            bg="#0b1220",
            fg=NEON,
            font=(FONT, 12, "bold")
        ).pack(anchor="w", padx=22, pady=(24, 10))

        menu = [
            ("🏠 Inicio", self.show_home),
            ("📘 Logaritmos", self.show_logaritmos),
            ("📐 Bhaskara", self.show_bhaskara),
            ("🧮 Ruffini", self.show_ruffini),
            ("∫ Integrales", self.show_integrales),
        ]

        for text, cmd in menu:
            NeonButton(self.sidebar, text=text, command=cmd, big=True).pack(
                fill="x", padx=18, pady=8
            )

        tk.Label(
            self.sidebar,
            text=(
                
                "• Para potencias usa x**2\n"
                "• Para multiplicar usa 2*x"
            ),
            bg="#0b1220",
            fg=MUTED,
            justify="left",
            font=(FONT, 10)
        ).pack(anchor="w", padx=22, pady=(24, 10))

        # ================= Contenido principal =================
        content = GlassCard(self.main, glow_color=NEON, inner_bg=CARD)
        content.place(relx=0.29, rely=0.14, relwidth=0.71, relheight=0.86)
        self.content = content.inner

    # ========================================================
    # UTILIDADES UI
    # ========================================================
    def clear_content(self):
        for widget in self.content.winfo_children():
            widget.destroy()

    def section_title(self, parent, title, subtitle):
        tk.Label(
            parent,
            text=title,
            bg=CARD,
            fg=TEXT,
            font=(FONT, 24, "bold")
        ).pack(anchor="w", padx=26, pady=(26, 4))

        tk.Label(
            parent,#f
            text=subtitle,#a
            bg=CARD,#p
            fg=MUTED,#e
            font=(FONT, 11)#r
        ).pack(anchor="w", padx=26, pady=(0, 18))#e

    def create_input(self, parent, label):#z
        tk.Label(
            parent,
            text=label,
            bg=CARD,
            fg=TEXT,
            font=(FONT, 11, "bold")
        ).pack(anchor="w", pady=(8, 6))

        entry = NeonEntry(parent)
        entry.pack(anchor="w", fill="x")
        return entry

    def result_box(self, parent):
        frame = tk.Frame(parent, bg=NEON, bd=0)
        inner = tk.Frame(frame, bg="#08111f")
        inner.pack(fill="both", expand=True, padx=1, pady=1)

        tk.Label(
            inner,
            text="RESULTADO",
            bg="#08111f",
            fg=NEON,
            font=(FONT, 11, "bold")
        ).pack(anchor="w", padx=18, pady=(14, 4))

        self.result_label = tk.Label(
            inner,
            text="Aquí aparecerá el resultado...",
            bg="#08111f",
            fg=TEXT,
            justify="left",
            wraplength=640,
            font=(FONT, 14)
        )
        self.result_label.pack(anchor="w", padx=18, pady=(0, 16))
        return frame

    def set_result(self, text, ok=True):
        if self.result_label:
            self.result_label.config(text=text, fg=SUCCESS if ok else ERROR)

    # ========================================================
    # PANTALLA INICIO
    # ========================================================
    def show_home(self):
        self.clear_content()

        self.section_title(
            self.content,
            "Panel principal",
            "Selecciona un módulo desde la izquierda."
        )

        cards = tk.Frame(self.content, bg=CARD)
        cards.pack(fill="x", padx=24, pady=8)

        items = [
            ("📘 Logaritmos", "Calcula logaritmos usando número y base."),
            ("📐 Bhaskara", "Resuelve ecuaciones cuadráticas con discriminante."),
            ("🧮 Ruffini", "Opera con coeficientes usando el esquema de Ruffini."),
            ("∫ Integrales", "Calcula integrales indefinidas y definidas con SymPy."),
        ]

        for i, (title, desc) in enumerate(items):
            card = tk.Frame(cards, bg=NEON, bd=0)
            inner = tk.Frame(card, bg="#0c1527")
            inner.pack(fill="both", expand=True, padx=1, pady=1)

            tk.Label(
                inner,
                text=title,
                bg="#0c1527",
                fg=TEXT,
                font=(FONT, 14, "bold")
            ).pack(anchor="w", padx=18, pady=(18, 6))

            tk.Label(
                inner,
                text=desc,
                bg="#0c1527",
                fg=MUTED,
                justify="left",
                wraplength=220,
                font=(FONT, 10)
            ).pack(anchor="w", padx=18, pady=(0, 18))

            card.grid(
                row=i // 2,
                column=i % 2,
                sticky="nsew",
                padx=10,
                pady=10,
                ipadx=4,
                ipady=4
            )

        cards.grid_columnconfigure(0, weight=1)
        cards.grid_columnconfigure(1, weight=1)

        rb = self.result_box(self.content)
        rb.pack(fill="x", padx=24, pady=18)
        self.set_result("Interfaz cargada correctamente. Elige un módulo para empezar.", True)

    # ========================================================
    # LOGARITMOS
    # ========================================================
    def show_logaritmos(self):
        self.clear_content()

        self.section_title(
            self.content,
            "Logaritmos",
            "Introduce el número y la base del logaritmo."
        )

        form = tk.Frame(self.content, bg=CARD)
        form.pack(fill="x", padx=24)

        entry_num = self.create_input(form, "Número")
        entry_base = self.create_input(form, "Base")

        def calcular():
            try:
                d = float(entry_num.get())
                e = float(entry_base.get())

                if d <= 0:
                    self.set_result("Error: el número debe ser mayor que 0.", False)
                    return

                if e <= 0 or e == 1:
                    self.set_result("Error: la base es inválida.", False)
                    return

                res = math.log(d, e)
                self.set_result(f"Resultado: log base {e} de {d} = {res}", True)

            except ValueError:
                self.set_result("Error: introduce valores numéricos válidos.", False)
            except Exception as ex:
                self.set_result(f"Error inesperado: {ex}", False)

        NeonButton(form, "Calcular logaritmo", calcular, big=True).pack(anchor="w", pady=18)

        rb = self.result_box(self.content)
        rb.pack(fill="x", padx=24, pady=10)

    # ========================================================
    # BHASKARA
    # ========================================================
    def show_bhaskara(self):
        self.clear_content()

        self.section_title(
            self.content,
            "Bhaskara",
            "Resuelve una ecuación cuadrática ax² + bx + c = 0."
        )

        form = tk.Frame(self.content, bg=CARD)
        form.pack(fill="x", padx=24)

        entry_a = self.create_input(form, "Coeficiente A")
        entry_b = self.create_input(form, "Coeficiente B")
        entry_c = self.create_input(form, "Coeficiente C")

        def calcular():
            try:
                a = float(entry_a.get())
                b = float(entry_b.get())
                c = float(entry_c.get())

                if a == 0:
                    self.set_result("Error: A no puede ser 0 en una ecuación cuadrática.", False)
                    return

                discriminante = b**2 - 4*a*c

                if discriminante < 0:
                    self.set_result("No hay soluciones reales.", False)
                else:
                    x1 = (-b + math.sqrt(discriminante)) / (2*a)
                    x2 = (-b - math.sqrt(discriminante)) / (2*a)
                    self.set_result(f"x1 = {x1}\nx2 = {x2}", True)

            except ValueError:
                self.set_result("Error: introduce valores numéricos válidos.", False)
            except Exception as ex:
                self.set_result(f"Error inesperado: {ex}", False)

        NeonButton(form, "Resolver ecuación", calcular, big=True).pack(anchor="w", pady=18)

        rb = self.result_box(self.content)
        rb.pack(fill="x", padx=24, pady=10)

    # ========================================================
    # RUFFINI
    # ========================================================
    def show_ruffini(self):
        self.clear_content()

        self.section_title(
            self.content,
            "Ruffini",
            "Introduce los coeficientes del polinomio y el coeficiente de Ruffini."
        )

        form = tk.Frame(self.content, bg=CARD)
        form.pack(fill="x", padx=24)

        entry_a = self.create_input(form, "A")
        entry_b = self.create_input(form, "B")
        entry_c = self.create_input(form, "C")
        entry_d = self.create_input(form, "D")
        entry_e = self.create_input(form, "Coeficiente")

        def calcular():
            try:
                a = float(entry_a.get())
                b = float(entry_b.get())
                c = float(entry_c.get())
                d = float(entry_d.get())
                e = float(entry_e.get())

                f = e * a + b
                g = e * f + c
                h = e * g + d

                self.set_result(
                    f"Resultado:\n{a}x³ + {f}x² + {g}x + resto {h}",
                    True
                )

            except ValueError:
                self.set_result("Error: introduce valores numéricos válidos.", False)
            except Exception as ex:
                self.set_result(f"Error inesperado: {ex}", False)

        NeonButton(form, "Calcular Ruffini", calcular, big=True).pack(anchor="w", pady=18)

        rb = self.result_box(self.content)
        rb.pack(fill="x", padx=24, pady=10)

    # ========================================================
    # INTEGRALES
    # ========================================================
    def show_integrales(self):
        self.clear_content()

        self.section_title(
            self.content,
            "Integrales",
            "Usa formato SymPy. Ejemplo: x**2 + 2*x"
        )

        form = tk.Frame(self.content, bg=CARD)
        form.pack(fill="x", padx=24)

        entry_funcion = self.create_input(form, "Función")
        entry_a = self.create_input(form, "Límite inferior (para definida)")
        entry_b = self.create_input(form, "Límite superior (para definida)")

        btns = tk.Frame(form, bg=CARD)
        btns.pack(anchor="w", pady=18)

        def calcular_integral():
            try:
                funcion_texto = entry_funcion.get().strip()
                if not funcion_texto:
                    self.set_result("Error: introduce una función.", False)
                    return

                funcion = sp.sympify(funcion_texto)
                integral = sp.integrate(funcion, x)

                self.set_result(f"∫ {funcion} dx = {integral} + C", True)

            except Exception:
                self.set_result("Error en la función.", False)

        def calcular_definida():
            try:
                funcion_texto = entry_funcion.get().strip()
                if not funcion_texto:
                    self.set_result("Error: introduce una función.", False)
                    return

                funcion = sp.sympify(funcion_texto)
                a = float(entry_a.get())
                b = float(entry_b.get())

                resultado = sp.integrate(funcion, (x, a, b))
                self.set_result(f"Integral definida = {resultado}", True)

            except ValueError:
                self.set_result("Error: los límites deben ser numéricos.", False)
            except Exception:
                self.set_result("Error en los datos de la integral definida.", False)

        NeonButton(btns, "Integral indefinida", calcular_integral, big=True).pack(side="left", padx=(0, 12))
        NeonButton(btns, "Integral definida", calcular_definida, big=True).pack(side="left")

        rb = self.result_box(self.content)
        rb.pack(fill="x", padx=24, pady=10)


# ============================================================
# EJECUCIÓN
# ============================================================
if __name__ == "__main__":
    root = tk.Tk()
    app = CalculadoraApp(root)
    root.mainloop()
