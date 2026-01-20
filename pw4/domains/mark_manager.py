import math
import numpy as np

class MarkManager:
    def __init__(self):
        self.students = []
        self.courses = []
        self.marks = {}

    def input_marks(self):
        for c in self.courses:
            for s in self.students:
                m = float(input(f"{s.get_name()} - {c}: "))
                self.marks[(c.get_id(), s.get_id())] = math.floor(m * 10) / 10

    def average_GPA(self):
        gpas = []
        for s in self.students:
            scores, credits = [], []
            for c in self.courses:
                k = (c.get_id(), s.get_id())
                if k in self.marks:
                    scores.append(self.marks[k])
                    credits.append(c.get_credits())
            gpa = np.average(scores, weights=credits) if scores else 0
            gpas.append((gpa, s))

        gpas.sort(key=lambda x: x[0], reverse=True)
        for g, s in gpas:
            print(s.get_name(), f"{g:.2f}")
