# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel

from datetime import datetime
import dateutil.parser  # We might need dateutil if we want flexible parsing, but standard lib is safer for zero-dependency.
                        # I'll stick to strptime with common formats or just basic ISO format for now.
                        # Wait, standard lib only doesn't have dateutil. I'll implement basic robust parsing.

class TimeConverter:
    @staticmethod
    def get_current():
        now = datetime.now()
        return {
            "timestamp": int(now.timestamp()),
            "iso": now.isoformat(),
            "human": now.strftime("%Y-%m-%d %H:%M:%S")
        }

    @staticmethod
    def to_human(timestamp_str):
        try:
            ts = float(timestamp_str)
            # Heuristic to detect milliseconds
            # If ts > 100 billion, it's definitely milliseconds (year 5138)
            # If ts > 253402300799 (year 9999), it's definitely micro or nano
            
            is_millis = False
            if ts > 32503680000: # Year 3000 in seconds
                ts = ts / 1000.0
                is_millis = True
            
            dt = datetime.fromtimestamp(ts)
            result = {
                "original": timestamp_str,
                "assumed_unit": "milliseconds" if is_millis else "seconds",
                "human": dt.strftime("%Y-%m-%d %H:%M:%S"),
                "iso": dt.isoformat(),
                "utc": dt.astimezone().strftime("%Y-%m-%d %H:%M:%S %Z")
            }
            return result
        except ValueError:
            return {"error": "Invalid timestamp format"}

    @staticmethod
    def to_timestamp(date_str):
        # Tries a few common formats
        formats = [
            "%Y-%m-%d %H:%M:%S",
            "%Y-%m-%d %H:%M",
            "%Y-%m-%d",
            "%d-%m-%Y %H:%M:%S",
            "%m/%d/%Y %H:%M:%S"
        ]
        
        for fmt in formats:
            try:
                dt = datetime.strptime(date_str, fmt)
                return {
                    "original": date_str,
                    "timestamp": int(dt.timestamp()),
                    "iso": dt.isoformat()
                }
            except ValueError:
                continue
        
        # If standard parsing fails, check if ISO format works
        try:
            dt = datetime.fromisoformat(date_str)
            return {
                "original": date_str,
                "timestamp": int(dt.timestamp()),
                "iso": dt.isoformat()
            }
        except ValueError:
            pass

        return {"error": "Could not parse date format. Try YYYY-MM-DD HH:MM:SS"}

# Developed for Anunzio International by Anzul Aqeel. Contact +971545822608 or +971585515742. Linkedin Profile: linkedin.com/in/anzulaqeel
