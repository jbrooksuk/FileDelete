import sublime, sublime_plugin
import os, functools

class FileDeleteCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        filename = self.view.file_name()

        if not os.access(filename, os.W_OK):
            sublime.error_message("%s is read only" % filename)

        panel = self.view.window().show_input_panel("Delete this file? Y/n", "n", functools.partial(self.on_done, filename), None, None)

        panel.sel().clear()
        panel.sel().add(sublime.Region(0, 1))

    def on_done(self, filename, answer):
        if answer == "n":
            pass
        elif answer == "Y":
            try:
                os.remove(filename)

                sublime.status_message("%s deleted" % filename)
            except Exception as e:
                sublime.status_message("Could not remove file: %s" % str(e))
