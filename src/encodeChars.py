from typing import List
import json


class EncodeChars:
    def __init__(self, char_dict_path='charDict.json'):
        self.__raw_dict: dict = self.__load_json(f"resources/{char_dict_path}")
        self.code_to_char: dict = self.__raw_dict.get("chars")
        self.char_to_code: dict = {v: k for k, v in self.code_to_char.items()}
        self.name: str = self.__raw_dict.get('custom')

    def __repr__(self) -> str:
        return f"Character encoding {self.name}"

    def __len__(self) -> int:
        return len(self.__raw_dict.get('chars'))

    def __load_json(self, path: str) -> dict:
        with open(path, "r", encoding='utf-8') as json_file:
            return json.load(json_file)

    def char_to_bits(self, char) -> str:
        result: str = str(bin(int(self.char_to_code.get(char, 127)))).replace("0b", "")
        padding: int = 8 - len(result)
        return "0" * padding + result

    def string_to_bits(self, text: str) -> List[int]:
        for char in text:
            print(self.char_to_bits(char))


if __name__ == "__main__":
    encoder = EncodeChars()
    encoder.string_to_bits("Co tam u ciebie adaś!")
