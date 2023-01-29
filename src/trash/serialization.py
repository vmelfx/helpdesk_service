from pydantic import BaseModel
from rest_framework import serializers


class Coordinates(BaseModel):
    longitude: float
    latitude: float


class PhoneNumber(BaseModel):
    country_code: int
    number: int


class ContactInfo(BaseModel):
    mail: str
    phone: PhoneNumber


class AddressInfo(BaseModel):
    country: str
    city: str
    street: str
    building: str
    coordinates: Coordinates


class LuxuryInfo(BaseModel):
    spa_exist: bool
    pool_exist: bool
    rest_exist: bool


class Hotel(BaseModel):
    name: str
    rate: int
    address_info: AddressInfo
    contact_info: ContactInfo
    luxury_info: LuxuryInfo


class CoordinatesSerializer(serializers.Serializer):
    longitude = serializers.FloatField
    latitude = serializers.FloatField


class AddressInfoSerializer(serializers.Serializer):
    country = serializers.CharField()
    city = serializers.CharField()
    street = serializers.CharField()
    building = serializers.IntegerField()
    coordinates: CoordinatesSerializer()


class HotelSerializer(serializers.Serializer):
    name = serializers.CharField()
    rate = serializers.IntegerField
    AddressInfo = AddressInfoSerializer()


def main():
    payload = {
        "name": "Grand Hotel",
        "rate": 4,
        "address_info": {
            "country": "Ukraine",
            "city": "Kyiv",
            "street": "Peremogy avenu",
            "building": "Polytech 3",
            "coordinates": {
                "longitude": 20.12,
                "latitude": 30.9,
            },
        },
    }

    grand_hotel = HotelSerializer(payload)
    print(grand_hotel)


if __name__ == "__main__":
    main()
