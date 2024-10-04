from typing import Any


class FormHelper:
    def __init__(self, *args: tuple, **kwargs: dict) -> None:
        super().__init__(*args, **kwargs)

        self.validate(self)

    @staticmethod
    def attributes(identifier: str) -> dict:
        if not identifier:
            raise ValueError('The tag identifier can not be empty.')

        return {'id': identifier, 'class': 'form-control'}

    @staticmethod
    def validate(form: Any) -> None:
        for name, field in form.fields.items():
            if not form.errors.get(name):
                continue

            MAPPING = {
                'class': 'class',
                'id': 'aria-describedby',
            }

            for source, target in MAPPING.items():
                attribute = field.widget.attrs.get(source, '')
                field.widget.attrs[target] = attribute + ' is-invalid'
