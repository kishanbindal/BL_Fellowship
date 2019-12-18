class Doctor:

    def __init__(self, name=None, i_d=None, spec=None, avail=None):
        self._name = name
        self._i_d = i_d
        self._spec = spec
        self._avail = avail
        self.number_of_appointments_shift1 = 0
        self.number_of_appointments_shift2 = 0
        self.total_appointments = self.number_of_appointments_shift1 + self.number_of_appointments_shift2
        self.list_of_appointments = []
