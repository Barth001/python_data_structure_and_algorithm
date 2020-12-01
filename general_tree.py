class Management:
    def __init__(self, name, designation):
        self.name = name
        self.designation = designation
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level

    def print_tree(self, property_name):
        if property_name == 'both':
            value = self.name + " (" + self.designation + ")"
        elif property_name == 'name':
            value = self.name
        else:
            value = self.designation

        spaces = ' ' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""
        print(prefix + value)
        if self.children:
            for child in self.children:
                child.print_tree(property_name)


def build_management_tree():
    # CTO Hierarchy
    infra_head = Management("Vishwa", "Infrastructure Head")
    infra_head.add_child(Management("Dhaval", "Cloud Manager"))
    infra_head.add_child(Management("Abhijit", "App Manager"))

    cto = Management("Chinmay", "CTO")
    cto.add_child(infra_head)
    cto.add_child(Management("Aamir", "Application Head"))

    # HR hierarchy
    hr_head = Management("Gels", "HR Head")

    hr_head.add_child(Management("Peter", "Recruitment Manager"))
    hr_head.add_child(Management("Waqas", "Policy Manager"))

    ceo = Management("Nilupul", "CEO")
    ceo.add_child(cto)
    ceo.add_child(hr_head)

    return ceo


if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_tree("both")
