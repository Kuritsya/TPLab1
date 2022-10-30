import pytest
import yaml
from src.DataReaderChild import DataReaderChild
from src.Types import DataType


class TestDataReaderChild:
    @pytest.fixture()
    def file_and_data_content(self) -> tuple[str, DataType]:
        text = "- Александров Александр Александрович:\n" + \
               "    русский язык: 100\n" + \
               "    литература: 99\n" + \
               "- Иванов Иван Иванович:\n" + \
               "    обществознание: 66\n" + \
               "    история: 77\n"

        data = {
            "Александров Александр Александрович": [
                ("русский язык", 100),
                ("литература", 99)
            ],
            "Иванов Иван Иванович": [
                ("обществознание", 66),
                ("история", 77)
            ]
        }
        return text, data

    @pytest.fixture()
    def filepath_and_data(self,
                          file_and_data_content: tuple[str, DataType],
                          tmpdir) -> tuple[str, DataType]:
        p = tmpdir.mkdir("datadir").join("TestYaml.yaml")
        p.write_text(file_and_data_content[0], encoding='utf-8')
        return str(p), file_and_data_content[1]

    def test_read(self, filepath_and_data: tuple[str, DataType]) -> None:
        file_content = DataReaderChild().read(filepath_and_data[0])
        assert file_content == filepath_and_data[1]
