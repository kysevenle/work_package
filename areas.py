import work_package

class Areas:
    def __init__(self, regex = None, lines = None):
        self.regex = regex
        self.lines = lines

north_c = Areas()
north_c.regex = "((10.2.(4[89]|5[0-9]|6[0-3]).(\d|\d\d|\d\d\d))|(64.72.211.(3[4-9]|4[0-6])))"
north_c.lines = ['NorthC_F3_N', 'NorthC_F3_S']

central_h = Areas()
central_h.regex = "((10.3.1(2[89]|3[0-9]|4[0-3]).(\d|\d\d|\d\d\d))|(64.72.212.1(1[4-9]|2[0-6]))|(64.72.212.(19[4-9]|20[0-6])))"

print(north_c.lines)
