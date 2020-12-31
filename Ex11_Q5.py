from typing import List


class Agent:
    def __init__(self, name, pref: List):
        self.name = name
        # the preferences will be givan as a list s.t lower index in the list
        # indicates higher priority for the current agent
        self.pref = pref


def find_match(set1: List[Agent], set2: List[Agent]) -> dict:
    """

    :param set1:
    :param set2:
    :return:
    >>> s1 = Agent("Rafi", ["Aviva", "Gila", "Batya"])
    >>> s2 = Agent("Shlomo", ["Aviva", "Batya", "Gila"])
    >>> s3 = Agent("Tomer", ["Batya", "Gila", "Aviva"])
    >>> d1 = Agent("Gila", ["Shlomo", "Tomer", "Rafi"])
    >>> d2 = Agent("Batya", ["Shlomo", "Rafi", "Tomer"])
    >>> d3 = Agent("Aviva", ["Rafi", "Shlomo", "Tomer"])
    >>> res = find_match([s1, s2, s3], [d1, d2, d3])
    >>> print(res)
    {'Batya': 'Shlomo', 'Aviva': 'Rafi', 'Gila': 'Tomer'}
    """
    matched_pairs = {}
    need_match = set(set1)
    temp_need_match = set()
    while len(need_match) > 0:
        for dep in set2:
            interested_students = set()
            cont = True
            for student in need_match:
                if student.pref[0] == dep.name:
                    interested_students.add(student)
            for student_name in dep.pref: # will itarate from high priority to low priority
                if not cont:
                    break
                for student in interested_students:
                    if not cont:
                        break
                    if student_name == student.name and matched_pairs.get(dep.name) is None:
                        for s in interested_students:
                            s.pref.pop(0)
                        matched_pairs.update({dep.name: student})
                        # interested_students.remove(student)
                        # temp_need_match.update(interested_students)
                        for s in interested_students:
                            if not s == student:
                                temp_need_match.add(s)
                        cont = False
                    elif student_name == student.name:
                        if get_index(dep.pref, student.name) < get_index(dep.pref, matched_pairs.get(dep.name).name):
                            for s in interested_students:
                                s.pref.pop(0)
                            old_s = matched_pairs.get(dep.name)
                            matched_pairs.update({dep.name: student})
                            # interested_students.remove(student)
                            # temp_need_match.update(interested_students)
                            for s in interested_students:
                                if not s == student:
                                    temp_need_match.add(s)
                            temp_need_match.add(old_s)
                            cont = False
        need_match.clear()
        need_match.update(temp_need_match)
        temp_need_match.clear()
    fixed_dict = {}
    for k,v in matched_pairs.items():
        fixed_dict.update({k: v.name})
    return fixed_dict


def get_index(l , _val):
    for idx, val in enumerate(l):
        if val == _val:
            return idx


if __name__ == "__main__":
    import doctest
    doctest.testmod()

    # >>> s11 = Agent("Rafi", ["Batya", "Aviva", "Gila"])
    # >>> s22 = Agent("Shlomo", ["Aviva", "Batya", "Gila"])
    # >>> s33 = Agent("Tomer", ["Batya", "Aviva", "Gila"])
    # >>> d11 = Agent("Gila", ["Shlomo", "Rafi", "Tomer"])
    # >>> d22 = Agent("Batya", ["Shlomo", "Rafi", "Tomer"])
    # >>> d33 = Agent("Aviva", ["Rafi", "Shlomo", "Tomer"])
    # >>> res2 = find_match([s11, s22, s33], [d11, d22, d33])
    # >>> print(res2)
# s11 = Agent("Rafi", ["Batya", "Aviva", "Gila"])
# s22 = Agent("Shlomo", ["Aviva", "Batya", "Gila"])
# s33 = Agent("Tomer", ["Batya", "Aviva", "Gila"])
# d11 = Agent("Gila", ["Shlomo", "Rafi", "Tomer"])
# d22 = Agent("Batya", ["Shlomo", "Rafi", "Tomer"])
# d33 = Agent("Aviva", ["Rafi", "Shlomo", "Tomer"])
# res2 = find_match([s11, s22, s33], [d11, d22, d33])
# print(res2)