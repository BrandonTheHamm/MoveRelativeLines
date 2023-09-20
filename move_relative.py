import sublime, sublime_plugin

#------------------------------------------------------------------------------
class LineCountInputHandler(sublime_plugin.TextInputHandler):
	def placeholder(self):
		return "# of lines"


#------------------------------------------------------------------------------
class MoveRelativeCommand(sublime_plugin.TextCommand):
	def run(self, edit, line_count):
		num_lines = int(line_count)
		move_down = num_lines > 0
		for _ in range(abs(num_lines)):
			self.view.run_command("move", {
				"by": "lines",
				"forward": move_down
				})

	def input(self, args):
		if "line_count" not in args:
			return LineCountInputHandler()