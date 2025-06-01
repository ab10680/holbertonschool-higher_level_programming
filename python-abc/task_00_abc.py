#!/usr/bin/python3
"""
Defines an abstract Animal class with a sound method.
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class representing an animal."""

    @abstractmethod
    def sound(self):
        """Abstract method to be implemented by subclasses."""
        pass


class Dog(Animal):
    """Dog class inheriting from Animal."""

    def sound(self):
        return "Bark"


class Cat(Animal):
    """Cat class inheriting from Animal."""

    def sound(self):
        return "Meow"
