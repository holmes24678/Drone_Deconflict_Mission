import json
import math

def load_missions(filename):
    with open(filename, 'r') as f:
        data = json.load(f)
    primary = data['primary']  # list of [time,x,y,z]
    others = data['others']    # list of dicts with 'id' and 'waypoints'
    return primary, others

def check_conflict(primary, others, threshold=1.0):
    # Create a dict mapping time -> (x, y, z) for primary waypoints
    primary_dict = {p[0]: (p[1], p[2], p[3]) for p in primary}

    conflicts = []

    for drone in others:
        drone_id = drone['id']
        for wp in drone['waypoints']:
            t = wp[0]
            x, y, z = wp[1], wp[2], wp[3]
            if t in primary_dict:
                px, py, pz = primary_dict[t]
                dist = math.sqrt((x - px)**2 + (y - py)**2 + (z - pz)**2)
                if dist <= threshold:
                    conflicts.append({
                        'time': t,
                        'location': [x, y, z],
                        'with': drone_id,
                        'distance': dist
                    })
    return conflicts
