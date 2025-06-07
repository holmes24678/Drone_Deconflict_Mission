from deconflict import load_missions, check_conflict
from visualize_matplotlib import animate_missions_matplotlib

def main():
    # use missions.json to conflict free visualization
    # use collide.json to test for conflict
    primary, others = load_missions("collide.json") 
    
    conflicts = check_conflict(primary, others)

    if conflicts:
        print("⚠️ Conflict Detected!")
        for c in conflicts:
            print(f"  Time: {c['time']}s | Location: {c['location']} | With: Drone {c['with']} | Distance: {c['distance']:.2f}")
    else:
        print("✅ Mission is clear of conflicts.")

    animate_missions_matplotlib(primary, others, conflicts)


if __name__ == "__main__":
    main()
