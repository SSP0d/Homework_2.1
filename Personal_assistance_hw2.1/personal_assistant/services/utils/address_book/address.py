from re import search

from personal_assistant.services.utils.field import Field


class Address(Field):
    @Field.value.setter
    def value(self, value):
        self._value: str = self.check_address(value)

    @staticmethod
    def check_address(value: str) -> str:
        clean_value = value.strip()
        pattern = r'(?!^\d+$)^.+$'

        if not search(pattern, clean_value) or len(clean_value) < 3 or len(clean_value) > 30:
            raise ValueError(f"Address '{clean_value}' is not valid")

        return clean_value
