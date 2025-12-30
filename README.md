# Unix Timestamp Converter

A versatile CLI tool for converting between Unix timestamps and human-readable dates. It automatically detects milliseconds and supports various common date formats.

<!-- Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742 -->

## Features

*   **Auto-Detect Units**: Intelligently handles seconds or milliseconds as input.
*   **Flexible Parsing**: Understands typical date strings like `2024-01-01` or `2024-01-01 12:00:00`.
*   **Current Time**: Quickly grab the current epoch time.

## Usage

```bash
python run_converter.py [command] [args]
```

### Commands

*   `now`: Show current timestamp.
*   `decode [timestamp]`: Convert epoch to date.
*   `encode [date_string]`: Convert date to epoch.

### Examples

**1. Get Current Time**
```bash
python run_converter.py now
# Output: Timestamp: 1704067200
```

**2. Decode a Timestamp**
```bash
python run_converter.py decode 1609459200
# Output: Human: 2021-01-01 00:00:00
```

**3. Encode a Date**
```bash
python run_converter.py encode "2023-12-25 08:30:00"
# Output: Timestamp: 1703493000
```

**4. Quick Mode**
You can usually just pass the value directly without the command:
```bash
python run_converter.py 1700000000
```

## Requirements

*   Python 3.x

## Contributing

Developed for Anunzio International by Anzul Aqeel.
Contact: +971545822608 or +971585515742

## License

MIT License. See [LICENSE](LICENSE) for details.


---
### 🔗 Part of the "Ultimate Utility Toolkit"
This tool is part of the **[Anunzio International Utility Toolkit](https://github.com/anzulaqeel-anunzio/ultimate-utility-toolkit)**.
Check out the full collection of **180+ developer tools, scripts, and templates** in the master repository.

Developed for Anunzio International by Anzul Aqeel.
