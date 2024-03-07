from .base_model import BaseModel
from .engine import FileStorage

storage = FileStorage()  # Create a FileStorage instance
storage.reload()  # Reload objects from file if it exists

