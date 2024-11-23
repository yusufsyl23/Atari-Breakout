import tkinter as tk

class Zorluk:
    def __init__(self, zorluk_derecesi):
        self.zorluk_derecesi = zorluk_derecesi

        if self.zorluk_derecesi == "kolay":
            self._can = 5
            self._dx = -3
            self._dy = -3
            self._uzunluk = 9
            self._boyut = 2
            self._artis = 5
            self._tugla_boyut = (2, 4)

        elif self.zorluk_derecesi == "orta":
            self._can = 3
            self._dx = -5
            self._dy = -5
            self._uzunluk = 7
            self._boyut = 1
            self._artis = 10
            self._tugla_boyut = (1.5, 3)

        elif self.zorluk_derecesi == "zor":
            self._can = 1
            self._dx = -7
            self._dy = -7
            self._uzunluk = 5
            self._boyut = 0.5
            self._artis = 15
            self._tugla_boyut = (1, 2)

    def get_params(self):
        return {
            "can": self._can,
            "dx": self._dx,
            "dy": self._dy,
            "uzunluk": self._uzunluk,
            "boyut": self._boyut,
            "artis": self._artis,
            "tugla_boyut": self._tugla_boyut
        }

def show_difficulty_selection():
    def set_difficulty_and_start(zorluk_derecesi):
        nonlocal selected_difficulty
        selected_difficulty = zorluk_derecesi
        root.destroy()

    root = tk.Tk()
    root.title("Zorluk Seçimi")
    root.geometry("300x200")

    selected_difficulty = None

    kolay_button = tk.Button(root, text="Kolay", width=15, height=2, command=lambda: set_difficulty_and_start("kolay"))
    orta_button = tk.Button(root, text="Orta", width=15, height=2, command=lambda: set_difficulty_and_start("orta"))
    zor_button = tk.Button(root, text="Zor", width=15, height=2, command=lambda: set_difficulty_and_start("zor"))

    kolay_button.pack(pady=10)
    orta_button.pack(pady=10)
    zor_button.pack(pady=10)

    root.mainloop()

    return selected_difficulty
