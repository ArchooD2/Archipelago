from typing import Callable, Dict, NamedTuple, Optional

from BaseClasses import Location
from .Options import CliqueOptions



class CliqueLocation(Location):
    game = "Clique"


class CliqueLocationData(NamedTuple):
    region: str
    address: Optional[int] = None
    can_create: Callable[[CliqueOptions], bool] = lambda options: True
    locked_item: Optional[str] = None


location_data_table: Dict[str, CliqueLocationData] = {
    "The Big Red Button": CliqueLocationData(
        region="The Button Realm",
        address=69696969,
    ),
    "The Item on the Desk": CliqueLocationData(
        region="The Button Realm",
        address=69696968,
        can_create=lambda options: bool(getattr(options, "hard_mode")),
    ),
    "In the Player's Mind": CliqueLocationData(
        region="The Button Realm",
        locked_item="The Urge to Push",
    ),
}

location_table = {name: data.address for name, data in location_data_table.items() if data.address is not None}
locked_locations = {name: data for name, data in location_data_table.items() if data.locked_item}
