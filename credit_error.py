class CreditError(ArithmeticError):
    def __init__(self, *args):
        super().__init__(args)

    def __str__(self):
        return 'El dinero es insuficiente para esta compra'
