from datetime import datetime
from enum import Enum
from typing import Self
from pydantic import BaseModel, Field, ValidationError, model_validator


class ContactType(Enum):
    radio = "radio"
    visual = "visual"
    physical = "physical"
    telepathic = "telepathic"


class AlienContact(BaseModel):
    contact_id: str = Field(min_length=5, max_length=15)
    timestamp: datetime = Field()
    location: str = Field(min_length=3, max_length=100)
    contact_type: ContactType = Field()
    signal_strength: float = Field(ge=0.0, le=10.0)
    duration_minutes: int = Field(ge=1, le=1440)
    witness_count: int = Field(ge=1, le=100)
    message_received: str | None = Field(max_length=500, default=None)
    is_verified: bool = Field(default=False)

    @model_validator(mode="after")
    def customValidation(self) -> Self:
        if not self.contact_id.startswith("AC"):
            raise ValueError("id should be start with 'AC'")

        if (
            self.contact_type == ContactType.telepathic
            and self.witness_count < 3
        ):
            raise ValueError("should be at least 3 witness")

        if self.signal_strength > 7 and not self.message_received:
            raise ValueError("strong single shold be greater than 7 ")

        if self.contact_type == ContactType.physical and not self.is_verified:
            raise ValueError("Physical contact reports must be verified")

        return self


def main() -> None:
    print("Alien Contact Log Validation")
    print("======================================")

    try:
        print("Valid contact report:")
        contact1 = AlienContact(
            contact_id="AC_2024_001",
            contact_type=ContactType.radio,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=5,
            message_received="Greetings from Zeta Reticuli",
            timestamp=datetime.now(),
            # is_verified= True
        )
        print(f"ID: {contact1.contact_id}")
        print(f"Type: {contact1.contact_type.value}")
        print(f"Location: {contact1.location}")
        print(f"Signal: {contact1.signal_strength} /10")
        print(f"Duration: {contact1.duration_minutes} minutes")
        print(f"Witnesses: {contact1.witness_count}")
        print(f"Message: {contact1.message_received}")

    except ValidationError as e:
        print(e.errors()[0]["msg"])

    try:
        print("======================================")
        print("Expected validation error:")
        contact2 = AlienContact(
            contact_id="AC_2024_001",
            contact_type=ContactType.telepathic,
            location="Area 51, Nevada",
            signal_strength=8.5,
            duration_minutes=45,
            witness_count=2,
            message_received="Greetings from Zeta Reticuli",
            timestamp=datetime.now(),
            is_verified=True
        )
        print(f"ID: {contact2.contact_id}")
        print(f"Type: {contact2.contact_type}")
        print(f"Location: {contact2.location}")
        print(f"Signal: {contact2.signal_strength} /10")
        print(f"Duration: {contact2.duration_minutes} minutes")
        print(f"Witnesses: {contact2.witness_count}")
        print(f"Message: '{contact2.message_received}'")

    except ValidationError as e:
        print(e.errors()[0]["msg"])


if __name__ == "__main__":
    main()
