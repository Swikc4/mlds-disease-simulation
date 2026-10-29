# This saves the town results from our Week 2 simulation.
# It does not create a new town.

import json


def save_town_results(town_snapshots, town_meetings):
    data = {
        "town_snapshots": town_snapshots,
        "town_meetings": town_meetings
    }

    with open("town_data.json", "w") as file:
        json.dump(data, file)

    print("Town data saved!")


# After my teammates run their simulation, I can use:
# save_town_results(town_snapshots, town_meetings)
#
# Keep town_data.json in the visualizations folder
# so my notebook can read it.
