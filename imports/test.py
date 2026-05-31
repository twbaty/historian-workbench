from pathlib import Path

ged_file = Path(r"C:\Users\Tom Baty\code\historian_workbench\docs\imports\Batie.GED")

with open(ged_file, "rb") as f:
    data = f.read(200)

print(data)
