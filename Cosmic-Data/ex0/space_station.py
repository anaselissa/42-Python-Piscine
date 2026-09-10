from pydantic import BaseModel, ConfigDict, Field, ValidationError
from datetime import datetime


class SpaceStation(BaseModel):
    model_config = ConfigDict(validate_assignment=True)
    station_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=1, max_length=50)
    crew_size: int = Field(ge=1, le=20)
    power_level: float = Field(ge=0.0, le=100.0)
    oxygen_level: float = Field(ge=0.0, le=100.0)
    last_maintenance: datetime = Field()
    is_operational: bool = Field(default=True)
    notes: str | None = Field(default=None, max_length=200)


def main() -> None:
    print("Space Station Data Validation")
    print("========================================")

    try:
        station = SpaceStation(
            station_id="ISS001",
            name="International Space Station",
            crew_size=6,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime(2026, 2, 2, 12, 4, 5),
            notes="All Done"
        )

        print("Valid station created:")
        print(f"ID: {station.station_id}")
        print(f"Name: {station.name}")
        print(f"Crew: {station.crew_size} people")
        print(f"Power: {station.power_level}%")
        print(f"Oxygen: {station.oxygen_level}%")
        if station.is_operational:
            print("Status: Operational")
        else:
            print("Status:  NOT Operational")
    except ValidationError as e:
        print(e.errors()[0]["msg"])

    try:
        print("========================================")
        print("Expected validation error:")
        station2 = SpaceStation(
            station_id="ISS002",
            name="International Space Station",
            crew_size=39,
            power_level=85.5,
            oxygen_level=92.3,
            last_maintenance=datetime.now(),
            notes="All Done"
        )

        print(f"ID: {station2.station_id}")
        print(f"Name: {station2.name}")
        print(f"Crew: {station2.crew_size} people")
        print(f"Power: {station2.power_level}%")
        print(f"Oxygen: {station2.oxygen_level}%")
        if station2.is_operational:
            print("Status: Operational")
        else:
            print("Status:  NOT Operational")
    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
