"""Django Ninja Extra Schema - Build Pydantic Schemas from Django Models"""
from .orm import *

__version__ = "0.10.1"


__all__ = ["SchemaFactory", "Schema", "ModelSchema", "model_validator"]
