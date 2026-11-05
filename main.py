import tkinter as tk


def calculate(first: float, operator: str, second: float) -> float:
    if operator == "+":
        return first + second
    if operator == "-":
        return first - second
    if operator == "*":
        return first * second
    if operator == "/":
        if second == 0:
            raise ZeroDivisionError("делить на ноль нельзя")
        return first / second
    raise ValueError(f"неизвестная операция: {operator}")


class Calculator(tk.Tk):
    def __init__(self) -> None:
        super().__init__()
        self.title("Калькулятор")
        self.resizable(False, False)
        self.configure(bg="#202124")

        self.current = "0"
        self.first_operand: float | None = None
        self.pending_operator: str | None = None
        self.replace_display = True
        self.display = tk.StringVar(value=self.current)
        self.expression = tk.StringVar()
        self._create_widgets()

    def _create_widgets(self) -> None:
        screen = tk.Frame(self, bg="#202124", padx=12, pady=16)
        screen.grid(row=0, column=0, columnspan=4, sticky="nsew")
        tk.Label(
            screen,
            textvariable=self.expression,
            anchor="e",
            bg="#202124",
            fg="#9aa0a6",
            font=("Segoe UI", 12),
        ).pack(fill="x")
        tk.Label(
            screen,
            textvariable=self.display,
            anchor="e",
            bg="#202124",
            fg="white",
            font=("Segoe UI", 32),
            width=12,
        ).pack(fill="x")

        buttons = [
            ("C", self.clear, 1, 0, 1),
            ("±", self.toggle_sign, 1, 1, 1),
            ("÷", lambda: self.set_operator("/"), 1, 2, 1),
            ("×", lambda: self.set_operator("*"), 1, 3, 1),
            ("7", lambda: self.enter_digit("7"), 2, 0, 1),
            ("8", lambda: self.enter_digit("8"), 2, 1, 1),
            ("9", lambda: self.enter_digit("9"), 2, 2, 1),
            ("−", lambda: self.set_operator("-"), 2, 3, 1),
            ("4", lambda: self.enter_digit("4"), 3, 0, 1),
            ("5", lambda: self.enter_digit("5"), 3, 1, 1),
            ("6", lambda: self.enter_digit("6"), 3, 2, 1),
            ("+", lambda: self.set_operator("+"), 3, 3, 1),
            ("1", lambda: self.enter_digit("1"), 4, 0, 1),
            ("2", lambda: self.enter_digit("2"), 4, 1, 1),
            ("3", lambda: self.enter_digit("3"), 4, 2, 1),
            ("=", self.equals, 4, 3, 1),
            ("0", lambda: self.enter_digit("0"), 5, 0, 2),
            (".", lambda: self.enter_digit("."), 5, 2, 1),
        ]

        for label, command, row, column, colspan in buttons:
            is_operator = label in {"÷", "×", "−", "+", "="}
            tk.Button(
                self,
                text=label,
                command=command,
                bg="#3c4043" if is_operator else "#5f6368",
                fg="white",
                activebackground="#80868b",
                activeforeground="white",
                relief="flat",
                font=("Segoe UI", 16),
                width=5,
                height=2,
            ).grid(
                row=row,
                column=column,
                columnspan=colspan,
                padx=4,
                pady=4,
                sticky="nsew",
            )

        for column in range(4):
            self.grid_columnconfigure(column, weight=1)

    def enter_digit(self, digit: str) -> None:
        if self.replace_display:
            self.current = "0" if digit == "." else digit
            self.replace_display = False
        elif digit == ".":
            if "." in self.current:
                return
            self.current += digit
        elif self.current in {"0", "-0"}:
            self.current = digit if self.current == "0" else f"-{digit}"
        else:
            self.current += digit
        self.display.set(self.current)

    def set_operator(self, operator: str) -> None:
        value = float(self.current)
        if self.pending_operator is not None and not self.replace_display:
            value = calculate(self.first_operand or 0, self.pending_operator, value)
            self.current = self._format_number(value)
            self.display.set(self.current)

        self.first_operand = value
        self.pending_operator = operator
        self.expression.set(f"{self.current} {operator}")
        self.replace_display = True

    def equals(self) -> None:
        if self.pending_operator is None or self.first_operand is None:
            return

        second_operand = float(self.current)
        first_operand = self.first_operand
        operator = self.pending_operator
        try:
            result = calculate(first_operand, operator, second_operand)
        except ZeroDivisionError:
            self.current = "0"
            self.display.set("Ошибка")
            self.expression.set("Деление на ноль")
            self._reset_calculation()
            return

        self.current = self._format_number(result)
        self.display.set(self.current)
        self.expression.set(
            f"{self._format_number(first_operand)} {operator} "
            f"{self._format_number(second_operand)} ="
        )
        self._reset_calculation()

    def toggle_sign(self) -> None:
        if self.current == "0":
            return
        self.current = (
            self.current[1:] if self.current.startswith("-") else f"-{self.current}"
        )
        self.display.set(self.current)
        self.replace_display = False

    def clear(self) -> None:
        self.current = "0"
        self.display.set(self.current)
        self.expression.set("")
        self._reset_calculation()

    def _reset_calculation(self) -> None:
        self.first_operand = None
        self.pending_operator = None
        self.replace_display = True

    @staticmethod
    def _format_number(number: float) -> str:
        return format(number, ".12g")


def main() -> None:
    Calculator().mainloop()


if __name__ == "__main__":
    main()
