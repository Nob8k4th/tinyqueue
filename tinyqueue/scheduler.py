class Scheduler:
    def parse_cron(self, expr: str) -> int:
        parts = expr.split()
        if len(parts) != 5:
            raise ValueError("invalid cron")
        if not parts[0].startswith("*/"):
            raise ValueError("only */n supported")
        return int(parts[0][2:])
