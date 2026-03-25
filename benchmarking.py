import time
import random
import math
from models import PolarPoint, CartesianPoint2D, SphericalPoint, CartesianPoint3D
import distances


def run_benchmarks():
    n = 100000

    polar_pairs = [(PolarPoint(random.uniform(1, 100), random.uniform(0, 2 * math.pi)),
                    PolarPoint(random.uniform(1, 100), random.uniform(0, 2 * math.pi))) for _ in range(n)]
    cartesian_2d_pairs = [(CartesianPoint2D.from_polar(p1), CartesianPoint2D.from_polar(p2)) for p1, p2 in polar_pairs]

    start = time.perf_counter()
    for p1, p2 in polar_pairs:
        distances.distance_2d_polar(p1, p2)
    polar_2d_time = time.perf_counter() - start

    start = time.perf_counter()
    for p1, p2 in cartesian_2d_pairs:
        distances.distance_2d_cartesian(p1, p2)
    cartesian_2d_time = time.perf_counter() - start

    spherical_pairs = []
    for _ in range(n):
        r = random.uniform(1, 100)
        p1 = SphericalPoint(r, random.uniform(0, 2 * math.pi), random.uniform(0, math.pi))
        p2 = SphericalPoint(r, random.uniform(0, 2 * math.pi), random.uniform(0, math.pi))
        spherical_pairs.append((p1, p2))

    cartesian_3d_pairs = [(CartesianPoint3D.from_spherical(p1), CartesianPoint3D.from_spherical(p2)) for p1, p2 in
                          spherical_pairs]

    start = time.perf_counter()
    for p1, p2 in spherical_pairs:
        distances.distance_3d_spherical_chord(p1, p2)
    spherical_chord_time = time.perf_counter() - start

    start = time.perf_counter()
    for p1, p2 in spherical_pairs:
        distances.distance_3d_spherical_arc(p1, p2)
    spherical_arc_time = time.perf_counter() - start

    start = time.perf_counter()
    for p1, p2 in cartesian_3d_pairs:
        distances.distance_3d_cartesian(p1, p2)
    cartesian_3d_time = time.perf_counter() - start

    return {
        "2D Polar": polar_2d_time,
        "2D Cartesian": cartesian_2d_time,
        "3D Spherical Chord": spherical_chord_time,
        "3D Spherical Arc": spherical_arc_time,
        "3D Cartesian": cartesian_3d_time
    }
