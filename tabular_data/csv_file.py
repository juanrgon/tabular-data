import csv
from io import TextIOWrapper
import attrs
from contextlib import contextmanager
from pathlib import Path


@attrs.define
class TabularDataFile:
    path: str


@attrs.define
class CSVFile(TabularDataFile):
    headers: list[str]
    separator: str
    header_written: bool

    def read(self) -> list[dict[str, str]]:
        with open(self.path) as f:
            return list(csv.DictReader(f, delimiter=self.separator))

    def read_lists(self, skip_header: bool = False) -> list[list[str]]:
        with open(self.path) as f:
            reader = csv.reader(f, delimiter=self.separator)
            start = 1 if skip_header else 0
            return list(reader)[start:]

    def write(self, rows: list[dict[str, str]], write_header=True):
        with open(self.path, "w") as f:
            if not rows:
                return

            headers = self.headers if self.headers else rows[0].keys()
            writer = csv.DictWriter(f, fieldnames=headers, delimiter=self.separator)

            if write_header:
                writer.writeheader()

            writer.writerows(rows)

    @contextmanager
    def open(self):
        with open(self.path, "w") as f:
            yield SmartCSVWriter(headers=self.headers, separator=self.separator, file=f)


@attrs.define
class SmartCSVWriter:
    file: TextIOWrapper
    headers: list[str]
    separator: str
    header_written: bool = False
    writer: csv.DictWriter | None = None

    def write(self, rows: list[dict[str, str]]):
        if not rows:
            return

        if self.writer is None:
            headers = self.headers if self.headers else rows[0].keys()
            self.writer = csv.DictWriter(
                self.file, fieldnames=headers, delimiter=self.separator
            )
            self.writer.writeheader()

        self.writer.writerows(rows)


def csv_file(
    path: str | Path, headers: list[str] | bool = True, separator=","
) -> CSVFile:
    path = str(path)
    headers = headers if isinstance(headers, list) else []
    headers = headers or []
    return CSVFile(
        path=path, headers=headers, separator=separator, header_written=False
    )
