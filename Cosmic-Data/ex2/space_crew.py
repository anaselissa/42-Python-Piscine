from datetime import datetime
from enum import Enum
from typing import Self

from pydantic import BaseModel, Field, ValidationError, model_validator


class Rank(Enum):
    cadet = "cadet"
    officer = "officer"
    lieutenant = "lieutenant"
    commander = "commander"
    captain = "captain"


class CrewMember(BaseModel):
    member_id: str = Field(min_length=3, max_length=10)
    name: str = Field(min_length=2, max_length=50)
    rank: Rank = Field(...)
    age: int = Field(ge=18, le=80)
    specialization: str = Field(min_length=3, max_length=30)
    years_experience: int = Field(ge=0, le=50)
    is_active: bool = Field(default=True)


class SpaceMission(BaseModel):
    mission_id: str = Field(min_length=5, max_length=15)
    mission_name: str = Field(min_length=3, max_length=100)
    destination: str = Field(min_length=3, max_length=50)
    mission_status: str = Field(min_length=2, max_length=50, default="planned")
    duration_days: int = Field(ge=1, le=3650)
    launch_date: datetime = Field(...)
    crew: list[CrewMember] = Field(min_length=1, max_length=12)
    budget_millions: float = Field(ge=1.0, le=10000.0)

    @model_validator(mode="after")
    def MissionValidation(self) -> Self:
        if not self.mission_id.startswith("M"):
            raise ValueError("mission id shold be starat with 'M' ")

        has_leadership = False
        for crew_member in self.crew:
            if crew_member.rank in (Rank.commander, Rank.captain):
                has_leadership = True
                break

        if not has_leadership:
            raise ValueError(
                " mission must have at least one Commander or Captain"
            )

        count = 0
        if self.duration_days > 365:
            for i in self.crew:
                if i.years_experience >= 5:
                    count += 1
            if (len(self.crew) / 2) > count:
                raise ValueError(
                    "Long missions (> 365 days) need 50% experienced crew "
                    "(5+ years)"
                )

        for i in self.crew:
            if not i.is_active:
                raise ValueError("All crew members must be active")

        return self


def main() -> None:
    print("Space Mission Crew Validation")
    print("=========================================")

    try:
        print("Valid mission created:")
        crew1 = CrewMember(
            name="Sarah Connor",
            rank=Rank.cadet,
            specialization="Mission Command",
            member_id="123",
            age=22,
            years_experience=15,
            is_active=True,
        )
        crew2 = CrewMember(
            name="John Smith",
            rank=Rank.lieutenant,
            specialization="Navigation",
            member_id="124",
            age=22,
            years_experience=15,
            is_active=True,
        )
        crew3 = CrewMember(
            name="Alice Johnson",
            rank=Rank.commander,
            specialization="Engineering",
            member_id="125",
            age=22,
            years_experience=15,
            is_active=True,
        )
        crews = [crew1, crew2, crew3]
        mission1 = SpaceMission(
            mission_id="M2024_MARS",
            destination="Mars",
            duration_days=900,
            mission_name="mmm",
            launch_date=datetime.now(),
            budget_millions=900,
            crew=crews,
        )

        print(f"Mission: {mission1.mission_name}")
        print(f"ID: {mission1.mission_id}")
        print(f"Destination: {mission1.destination}")
        print(f"Duration: {mission1.duration_days} days")
        print(f"Budget: ${mission1.budget_millions}M")
        print(f"Crew size: {len(mission1.crew)}")
        print("Crew members:")

        for member in mission1.crew:
            print(
                f"- {member.name} ({member.rank.value}) - "
                f"{member.specialization}"
            )
    except ValidationError as e:
        for error in e.errors():
            print(f"- {error['msg']}")
            # print(f"- IN  :{error['loc']}")

    print("=========================================")

    try:
        print("Expected validation error:")
        crew1 = CrewMember(
            name="Sarah Connor",
            rank=Rank.cadet,
            specialization="Mission Command",
            member_id="123",
            age=22,
            years_experience=15,
            is_active=True,
        )
        crew2 = CrewMember(
            name="John Smith",
            rank=Rank.lieutenant,
            specialization="Navigation",
            member_id="124",
            age=22,
            years_experience=15,
            is_active=True,
        )
        crew3 = CrewMember(
            name="Alice Johnson",
            rank=Rank.officer,
            specialization="Engineering",
            member_id="125",
            age=22,
            years_experience=15,
            is_active=True,
        )
        crews = [crew1, crew2, crew3]
        mission2 = SpaceMission(
            mission_id="M2024_MARS",
            destination="Mars",
            duration_days=900,
            mission_name="mmm",
            launch_date=datetime.now(),
            budget_millions=900,
            crew=crews,
        )

        print(f"Mission: {mission2.mission_name}")
        print(f"ID: {mission2.mission_id}")
        print(f"Destination: {mission2.destination}")
        print(f"Duration: {mission2.duration_days} days")
        print(f"Budget: ${mission2.budget_millions}M")
        print(f"Crew size: {len(mission2.crew)}")
        print("Crew members:")

        for member in mission2.crew:
            print(
                f"- {member.name} ({member.rank.value}) - "
                f"{member.specialization}"
            )

    except ValidationError as e:
        for error in e.errors():
            print(f"- {error['msg']}")


if __name__ == "__main__":
    main()
