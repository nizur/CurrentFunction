import sublime, sublime_plugin


class FunctionInStatusListener(sublime_plugin.EventListener):
    def on_close(self, view):
        self.on_deactived(view)

    def on_activated(self, view):
        self.on_selection_modified(view)

    def on_deactived(self, view):
        view.erase_status('function name')

    def on_selection_modified(self, view):
        cf = self.get_current_function(view)
        if cf is None:
            view.erase_status('function name')
        else:
            view.set_status('function name', 'Function: ' + cf)

    def get_current_function(self, view):
        sel = view.sel()[0]
        functionRegs = view.find_by_selector('entity.name.function')
        cf = None

        for r in reversed(functionRegs):
            if r.a < sel.a:
                cf = view.substr(r)
                break

        return cf
