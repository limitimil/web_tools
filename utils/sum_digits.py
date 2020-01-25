import re


class SumDigits:
    # this module only support nature number.
    text_content = ''

    def __init__(self, text_content):
        self.text_content = text_content

    @property
    def digits(self):
        temp = re.findall(r'\d+', self.text_content)
        return list(map(int, temp))

    def get_sum(self):
        return sum(self.digits)
