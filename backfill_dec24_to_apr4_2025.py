import os
import sys
from datetime import datetime, timedelta
from random import randint

import contribute


def main(def_args=sys.argv[1:]):
    """Backfill contributions from 2024-12-01 to 2025-04-04.

    This script reuses contribute.py's logic but targets a fixed
    date range instead of using the current date.
    """
    args = contribute.arguments(def_args)

    # Ensure we are operating inside the existing "contribution" repo
    repo_root = os.path.join(os.path.dirname(os.path.abspath(__file__)), "contribution")
    os.chdir(repo_root)

    start_date = datetime(2024, 12, 1, 20, 0)
    end_date = datetime(2025, 4, 4, 20, 0)

    total_days = (end_date.date() - start_date.date()).days + 1

    for offset in range(total_days):
        day = start_date + timedelta(days=offset)
        if (not args.no_weekends or day.weekday() < 5) and randint(0, 100) < args.frequency:
            for commit_time in (day + timedelta(minutes=m)
                                for m in range(contribute.contributions_per_day(args))):
                contribute.contribute(commit_time)

    print("Backfill from 2024-12-01 to 2025-04-04 completed.")


if __name__ == "__main__":
    main()
