import argparse
import json
import jsonschema

def ParseJSON(jsonstr, schemastr):
    try:
        to_validate = json.loads(jsonstr)
        to_validate_against = json.loads(schemastr)
        jsonschema.validate(to_validate, to_validate_against)
    except Exception as e:
        print("Exception encountered: %s" % (e, ))
        print("Invalid JSON data")
        return None

    return to_validate

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process file data")
    parser.add_argument("JSON_data", metavar="J", type=open)
    parser.add_argument("JSON_schema", metavar="S", type=open)

    args = parser.parse_args()
    json_file = args.JSON_data
    json_schema = args.JSON_schema

    valid_JSON_obj = ParseJSON(json_file.read(), json_schema.read())
    if (valid_JSON_obj):
        print(valid_JSON_obj)

    json_file.close()
    json_schema.close()
