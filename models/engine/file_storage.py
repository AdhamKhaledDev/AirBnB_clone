#!/bin/usr/python3

import json
from models.base_model import BaseModel

from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State


class FileStorage:
    """
    Serializes and deserializes data to and from a JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        Returns the dictionary of all instantiated objects.

        Returns:
            dict: A dictionary containing all instantiated objects.
        """
        return self.__objects

    def new(self, obj):
        """
        Adds a new object to the dictionary of instantiated objects.

        Args:
            obj: The object to be added.
        """
        if isinstance(obj, (State, City, Amenity, Place, Review)):
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects[key] = obj
        else:
            # Handle non-supported objects (optional, based on your needs)
            pass

    def save(self):
        """
        Serializes the dictionary of objects to a JSON file.

        Modifies serialization based on object type.
        """
        data = {
            k: v.dict() if isinstance(v, BaseModel) else v for k, v in self.__objects.items()
        }
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    def reload(self):
        """
        Deserializes the JSON file back to the dictionary of objects.

        Modifies deserialization based on object type.
        """
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for key, value in data.items():
                    class_name, _ = key.split(".")
                    # Use appropriate class for deserialization
                    if class_name == "State":
                        self.new(State(**value))
                    elif class_name == "City":
                        self.new(City(**value))
                    elif class_name == "Amenity":
                        self.new(Amenity(**value))
                    elif class_name == "Place":
                        self.new(Place(**value))
                    elif class_name == "Review":
                        self.new(Review(**value))
                    else:
                        # Handle unexpected class names (optional)
                        pass
        except FileNotFoundError:
            pass
