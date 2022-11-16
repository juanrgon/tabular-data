# tabular-data

The sensible way to work with tabular data

## Read CSV files with ease

Go from this 😡

```python
import csv

with open('names.csv', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        print(row)
```

to this 😎

```python
from tabular_data import csv_file

for row in csv_file('names.csv').read():
    print(row)
```

## Write CSV files with no effort

Go from this 🤮

```python
import csv

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['first_name', 'last_name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Lovely', 'last_name': 'Spam'})
    writer.writerow({'first_name': 'Wonderful', 'last_name': 'Spam'})
```

to this 🤩

```python
from tabular_data import csv_file

csv_file('names.csv').write(
    [
        {'first_name': 'Baked', 'last_name': 'Beans'},
        {'first_name': 'Lovely', 'last_name': 'Spam'},
        {'first_name': 'Wonderful', 'last_name': 'Spam'}
    ]
)
```
