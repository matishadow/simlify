import sublime
import sublime_plugin
import random


def simlify(string):
    if not isinstance(string, str):
        raise ValueError("Argument must be of type string")

    string_as_list = list(string)

    for i in range(len(string_as_list)):
        char = string_as_list[i]
        if char == 'O':
            string_as_list[i] = 'Ö'
        elif char == 'o':
            string_as_list[i] = 'ö'
        elif char == 'A':
            string_as_list[i] = random.choice(['Å', 'Ä'])
        elif char == 'a':
            string_as_list[i] = random.choice(['å', 'ä'])

    return "".join(string_as_list)


class SimlifyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        contents = self.view.substr(sublime.Region(0, self.view.size()))

        simlified = simlify(contents)

        self.view.erase(edit, sublime.Region(0, self.view.size()))
        self.view.insert(edit, 0, simlified)
