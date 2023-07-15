from rich import print as rprint
from rich.tree import Tree
from rich.columns import Table
from rich.console import Console

tree = Tree("movie tree")

tree.add("Seven")
tree.add("the batman")
tree.add("the lord of the rings").add("two tower").add("ring frinds")


rprint(tree)



table = Table(title="todo list")

table.add_column("task Number", style="cyan", no_wrap=True)
table.add_column("Task", style="magenta", no_wrap=True)
table.add_column("Status", justify="right", style="green" , no_wrap=True)

table.add_row("1", "create a video", "Done")
table.add_row("2", "upload", "in progress")
table.add_row("3", "complete a code", "in progress")

console = Console()

console.print(table)


#new_list = [True,False]
#rprint(new_list)
