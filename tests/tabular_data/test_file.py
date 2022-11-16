import tabular_data
import fixtures.files
from pathlib import Path
import textwrap


def test_csv_file_read_records():
    assert tabular_data.csv_file(fixtures.files.PEOPLE_CSV).read_records() == [
        {
            "First Name": "Juan",
            "Last Name": "Gonzalez",
            "DOB": "01/01/1991",
            "State": "FL",
            "Country": "USA",
        },
        {
            "First Name": "Solomon",
            "Last Name": "Grundy",
            "DOB": "01/07/1991",
            "State": "NY",
            "Country": "USA",
        },
    ]


def test_csv_file_read_lists():
    csv = tabular_data.csv_file(fixtures.files.PEOPLE_CSV)

    assert csv.read_lists() == [
        ["First Name", "Last Name", "DOB", "State", "Country"],
        ["Juan", "Gonzalez", "01/01/1991", "FL", "USA"],
        ["Solomon", "Grundy", "01/07/1991", "NY", "USA"],
    ]

    assert csv.read_lists(skip_header=True) == [
        ["Juan", "Gonzalez", "01/01/1991", "FL", "USA"],
        ["Solomon", "Grundy", "01/07/1991", "NY", "USA"],
    ]


def test_csv_write_records():
    target_file = Path(f"{fixtures.files.PEOPLE_CSV}.ignore")

    # remove file if it exists
    if target_file.exists():
        target_file.unlink()

    tabular_data.csv_file(target_file).write_records(
        [
            {
                "First Name": "Juan",
                "Last Name": "Gonzalez",
                "DOB": "01/01/1991",
                "State": "FL",
                "Country": "USA",
            },
            {
                "First Name": "Solomon",
                "Last Name": "Grundy",
                "DOB": "01/07/1991",
                "State": "NY",
                "Country": "USA",
            },
        ]
    )

    assert target_file.read_text() == textwrap.dedent(
        """\
        First Name,Last Name,DOB,State,Country
        Juan,Gonzalez,01/01/1991,FL,USA
        Solomon,Grundy,01/07/1991,NY,USA
        """
    )


def test_csv_write_records_multiple_calls():
    target_file = Path(f"{fixtures.files.PEOPLE_CSV}.ignore")

    # remove file if it exists
    if target_file.exists():
        target_file.unlink()

    with tabular_data.csv_file(target_file).open() as csv:
        csv.write_records(
            [
                {
                    "First Name": "Juan",
                    "Last Name": "Gonzalez",
                    "DOB": "01/01/1991",
                    "State": "FL",
                    "Country": "USA",
                },
            ]
        )

        csv.write_records(
            [
                {
                    "First Name": "Solomon",
                    "Last Name": "Grundy",
                    "DOB": "01/07/1991",
                    "State": "NY",
                    "Country": "USA",
                }
            ]
        )

    assert target_file.read_text() == textwrap.dedent(
        """\
        First Name,Last Name,DOB,State,Country
        Juan,Gonzalez,01/01/1991,FL,USA
        Solomon,Grundy,01/07/1991,NY,USA
        """
    )
