from models import CartesianPoint2D, PolarPoint, CartesianPoint3D, SphericalPoint
import benchmarking
import math


def verify_conversions():
    p2d = CartesianPoint2D(10.0, 10.0)
    polar = PolarPoint.from_cartesian(p2d)
    back_to_2d = CartesianPoint2D.from_polar(polar)

    p3d = CartesianPoint3D(10.0, 20.0, 30.0)
    spherical = SphericalPoint.from_cartesian(p3d)
    back_to_3d = CartesianPoint3D.from_spherical(spherical)

    print("Verification Results:")
    print(f"2D: Start{p2d} -> End({round(back_to_2d.x, 2)}, {round(back_to_2d.y, 2)})")
    print(f"3D: Start{p3d} -> End({round(back_to_3d.x, 2)}, {round(back_to_3d.y, 2)}, {round(back_to_3d.z, 2)})")


if __name__ == "__main__":
    verify_conversions()
    print("\nRunning Benchmarks (100,000 points)...")
    results = benchmarking.run_benchmarks()
    for method, duration in results.items():
        print(f"{method}: {duration:.5f} seconds")
