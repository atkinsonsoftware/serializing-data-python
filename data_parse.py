import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Process file data")
    parser.add_argument("JSON_data", metavar="J", type=open)
    parser.add_argument("JSON_schema", metavar="S", type=open)

    args = parser.parse_args()
    json_file = args.JSON_data
    json_schema = args.JSON_schema
    json_file.close()
    json_schema.close()
