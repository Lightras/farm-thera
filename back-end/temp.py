from calculator import Calculator


class Temp:
    def __init__(self):
        self.p = 0.527975584944049
        self.D_v_a = 4
        self.D_v_b = 2
        self.D_n_a = 3
        self.D_n_b = 8
        self.Se = 0.8
        self.Sp = 0.9
        self.Cd_to_C = 0.77
        self.Ct_to_C = 0.86

        data_item = Calculator(
            self.p, self.D_v_a, self.D_v_b, self.D_n_a, self.D_n_b, self.Se, self.Sp, self.Cd_to_C, self.Ct_to_C
        )

        a = data_item.__dict__.keys()

        print([data_item[key] for key in a])


Temp()

print('me')
