"""Save the Week 2 team's town results for the visualization notebook.

This file does not build the town or simulate disease spread.
Teammate 3 creates town_snapshots and town_meetings in the original
assignment; the visualization reads the JSON file exported here.
"""

import json
from pathlib import Path


def save_town_results(town_snapshots, town_meetings, output_path=None):
    """Export actual simulation results, preserving resident ID order.

    town_snapshots[day][resident_id] is one of S, E, I, R.
    town_meetings[day] contains pairs of resident IDs.
    """
    if len(town_snapshots) != 61 or len(town_meetings) != 61:
        raise ValueError("Expected 61 entries (Day 0 through Day 60).")
    if any(len(snapshot) != 100 for snapshot in town_snapshots):
        raise ValueError("Every town snapshot must have 100 residents.")
    if any(state not in {"S", "E", "I", "R"}
           for snapshot in town_snapshots for state in snapshot):
        raise ValueError("Resident states must be S, E, I, or R.")

    if output_path is None:
        output_path = Path(__file__).with_name("town_data.json")
    path = Path(output_path)
    path.parent.mkdir(parents=True, exist_ok=True)
    data = {
        "town_snapshots": town_snapshots,
        "town_meetings": town_meetings,
    }
    path.write_text(json.dumps(data, indent=2), encoding="utf-8")
    return path


# Once Teammate 3's code has run in Week_02_Assignment.ipynb, use:
#
# from pathlib import Path
# import sys
# sys.path.insert(0, str(Path.cwd().parent / "simulations"))
# from town_simulation import save_town_results
# save_town_results(town_snapshots, town_meetings)
#
# If notebook working directory is the repository root, use:
# from simulations.town_simulation import save_town_results
