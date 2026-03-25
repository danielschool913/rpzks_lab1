import math

def distance_2d_cartesian(p1, p2):
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2)

def distance_2d_polar(p1, p2):
    return math.sqrt(p1.radius**2 + p2.radius**2 - 2 * p1.radius * p2.radius * math.cos(p2.angle - p1.angle))

def distance_3d_cartesian(p1, p2):
    return math.sqrt((p2.x - p1.x)**2 + (p2.y - p1.y)**2 + (p2.z - p1.z)**2)

def distance_3d_spherical_chord(p1, p2):
    cos_theta_diff = math.cos(p1.azimuth - p2.azimuth)
    central_angle_cos = math.sin(p1.polar_angle) * math.sin(p2.polar_angle) * cos_theta_diff + math.cos(p1.polar_angle) * math.cos(p2.polar_angle)
    return math.sqrt(p1.radius**2 + p2.radius**2 - 2 * p1.radius * p2.radius * central_angle_cos)

def distance_3d_spherical_arc(p1, p2):
    cos_theta_diff = math.cos(p1.azimuth - p2.azimuth)
    central_angle_cos = math.sin(p1.polar_angle) * math.sin(p2.polar_angle) * cos_theta_diff + math.cos(p1.polar_angle) * math.cos(p2.polar_angle)
    central_angle_cos = max(-1.0, min(1.0, central_angle_cos))
    return p1.radius * math.acos(central_angle_cos)
