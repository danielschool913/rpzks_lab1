import math
from dataclasses import dataclass

@dataclass(frozen=True)
class PolarPoint:
    radius: float
    angle: float

    @staticmethod
    def from_cartesian(p):
        radius = math.sqrt(p.x**2 + p.y**2)
        angle = math.atan2(p.y, p.x)
        return PolarPoint(radius, angle)

@dataclass(frozen=True)
class CartesianPoint2D:
    x: float
    y: float

    @staticmethod
    def from_polar(p):
        x = p.radius * math.cos(p.angle)
        y = p.radius * math.sin(p.angle)
        return CartesianPoint2D(x, y)

@dataclass(frozen=True)
class SphericalPoint:
    radius: float
    azimuth: float
    polar_angle: float

    @staticmethod
    def from_cartesian(p):
        r = math.sqrt(p.x**2 + p.y**2 + p.z**2)
        azimuth = math.atan2(p.y, p.x)
        polar_angle = math.acos(p.z / r) if r != 0 else 0
        return SphericalPoint(r, azimuth, polar_angle)

@dataclass(frozen=True)
class CartesianPoint3D:
    x: float
    y: float
    z: float

    @staticmethod
    def from_spherical(p):
        x = p.radius * math.sin(p.polar_angle) * math.cos(p.azimuth)
        y = p.radius * math.sin(p.polar_angle) * math.sin(p.azimuth)
        z = p.radius * math.cos(p.polar_angle)
        return CartesianPoint3D(x, y, z)
