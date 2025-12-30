# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

import argparse
import sys
import os

# Add current dir to path
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from converter.core import TimeConverter

def main():
    parser = argparse.ArgumentParser(description="Unix Timestamp Converter")
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # Current time
    subparsers.add_parser("now", help="Get current timestamp")

    # Convert FROM timestamp
    from_parser = subparsers.add_parser("decode", help="Convert timestamp to human date")
    from_parser.add_argument("timestamp", help="Unix timestamp (seconds or millis)")

    # Convert TO timestamp
    to_parser = subparsers.add_parser("encode", help="Convert date string to timestamp")
    to_parser.add_argument("date_string", help="Date string (e.g., '2023-12-31 23:59:59')")

    args = parser.parse_args()

    if args.command == "now":
        res = TimeConverter.get_current()
        print(f"Timestamp: {res['timestamp']}")
        print(f"Human:     {res['human']}")
        print(f"ISO:       {res['iso']}")

    elif args.command == "decode":
        res = TimeConverter.to_human(args.timestamp)
        if "error" in res:
            print(f"Error: {res['error']}")
        else:
            print(f"Unit:      {res['assumed_unit']}")
            print(f"Human:     {res['human']}")
            print(f"UTC:       {res['utc']}")
            print(f"ISO:       {res['iso']}")

    elif args.command == "encode":
        res = TimeConverter.to_timestamp(args.date_string)
        if "error" in res:
            print(f"Error: {res['error']}")
        else:
            print(f"Timestamp: {res['timestamp']}")
            print(f"ISO:       {res['iso']}")

    else:
        # Default behavior: Print current time if no args, or try to guess
        if len(sys.argv) > 1:
            # Try to guess if arg is timestamp or date
            arg = sys.argv[1]
            if arg.replace('.', '', 1).isdigit():
                # Probable timestamp
                res = TimeConverter.to_human(arg)
                print("Decoding (Auto-detected):")
                print(f"Human:     {res.get('human', res)}")
            else:
                # Probable date
                res = TimeConverter.to_timestamp(arg)
                print("Encoding (Auto-detected):")
                print(f"Timestamp: {res.get('timestamp', res)}")
        else:
            parser.print_help()

if __name__ == "__main__":
    main()

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
