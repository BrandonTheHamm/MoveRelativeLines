import sublime, sublime_plugin

#------------------------------------------------------------------------------
class LineCountInputHandler(sublime_plugin.TextInputHandler):
	def placeholder(self):
		return "# of lines"


#------------------------------------------------------------------------------
class MoveRelativeCommand(sublime_plugin.TextCommand):
	def run(self, edit, line_count):
		num_lines = int(line_count)
		current_position = self.view.sel()[0]
		current_rowcol = self.view.rowcol(current_position.begin())
		current_line = current_rowcol[0]
		target_row = current_line + num_lines
		target_position = self.view.text_point(target_row, 0)
		self.view.sel().clear()
		self.view.sel().add(target_position)
		self.view.show_at_center(target_position)

	def input(self, args):
		if "line_count" not in args:
			return LineCountInputHandler()