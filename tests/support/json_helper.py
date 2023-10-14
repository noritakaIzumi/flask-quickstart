import sys
from typing import Any, Mapping

import jsonref
import jsonschema
from jsonschema.exceptions import ValidationError

Schema = Mapping[str, Any]


def load_json_from_file(filepath: str) -> Any:
    return jsonref.load(open(filepath, "r"), base_uri=f"file://{filepath}", jsonschema=True)


def json_is_valid(instance: object, schema_filepath: str) -> bool:
    try:
        schema = load_json_from_file(schema_filepath)
        jsonschema.validate(instance=instance, schema=schema)
        return True
    except ValidationError as e:
        print(e.message, file=sys.stderr)
        return False
