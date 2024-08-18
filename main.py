import json
from car.models import Car
from car.serializers import CarSerializer


def serialize_car_object(car: Car) -> str:
    serializer = CarSerializer(car)
    return json.dumps(serializer.data)


def deserialize_car_object(car_json: str) -> Car:
    data = json.loads(car_json)
    serializer = CarSerializer(data=data)
    if serializer.is_valid():
        return serializer.save()
    else:
        raise ValueError("Invalid data for deserialization")
