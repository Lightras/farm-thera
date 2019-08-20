class Calculator:
    def __init__(self, p, D_v_a, D_v_b, D_n_a, D_n_b, Se, Sp, Cd_to_C, Ct_to_C):
        self.D_a = p * D_v_a + (1 - p) * D_n_a
        self.D_b = p * D_v_b + (1 - p) * D_n_b
        self.D_db = (p * (Se * D_v_b + (1 - Se) * D_v_a) +
                     (1 - p) * (Sp * D_n_a + (1 - Sp) * D_n_b))

        self.cost_criteria_1 = self.D_a - self.D_b
        self.p_boundary = ((D_n_a - D_n_b) / (D_v_b - D_n_b + D_n_a - D_v_a) +
                           (1 / (D_v_b - D_n_b + D_n_a - D_v_a)) * Ct_to_C)

        self.cost_criteria_2 = (self.D_a - self.D_db - Cd_to_C) / (p * Se + (1 - p) * (1 - Sp))
        self.p_a_to_db = (
                ((D_n_a - (1 - Se)*D_v_a - Sp*D_n_a - (1 - Sp)*D_n_b) /
                 (Se * D_v_b - Sp * D_n_a - (1 - Sp) * D_n_b - D_v_a + D_n_a)) -
                ((Cd_to_C + (1 - Sp) * Ct_to_C) /
                 (Se * D_v_b - Sp * D_n_a - (1 - Sp)*D_n_b - D_v_a + D_n_a)))

        self.cost_criteria_3 = ((self.D_db - self.D_b + Cd_to_C) /
                                (1 - (p*Se + (1 - p)*(1 - Sp))))
        self.p_b_to_db = ((Cd_to_C - Sp*Ct_to_C) /
                          (D_v_b - D_n_b - Se*D_v_b -
                           (1 - Se)*D_v_a + Sp*D_n_a + (1 - Sp)*D_n_b)) + \
                         ((Sp*D_n_a + (1 - Sp)*D_n_b - D_n_b) /
                          (D_v_b - D_n_b - Se*D_v_b - (1 - Se)*D_v_a +
                           Sp*D_n_a + (1 - Sp)*D_n_b))

        self.EC_to_C = ((p*D_v_a + (1 - p)*D_n_a) +
                        ((p*D_v_b + (1 - p)*D_n_b) + Ct_to_C) +
                        (self.D_db + Cd_to_C + (p*Se + (1 - p)*(1 - Sp))*Ct_to_C))


