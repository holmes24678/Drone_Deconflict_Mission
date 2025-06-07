import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.animation import FuncAnimation

def animate_missions_matplotlib(primary, others, conflicts):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    # Extract primary mission coordinates
    x_p = [p[1] for p in primary]
    y_p = [p[2] for p in primary]
    z_p = [p[3] for p in primary]

    # Plot other drones statically
    other_colors = ['green', 'orange', 'purple', 'cyan', 'magenta']
    for idx, drone in enumerate(others):
        waypoints = drone['waypoints']
        x_o = [wp[1] for wp in waypoints]
        y_o = [wp[2] for wp in waypoints]
        z_o = [wp[3] for wp in waypoints]
        color = other_colors[idx % len(other_colors)]
        ax.plot(x_o, y_o, z_o, color=color, marker='^', label=f"Drone {drone['id']}")

    # Plot conflicts
    if conflicts:
        cx = [c['location'][0] for c in conflicts]
        cy = [c['location'][1] for c in conflicts]
        cz = [c['location'][2] for c in conflicts]
        ax.scatter(cx, cy, cz, color='red', marker='x', s=100, label='Conflicts')

    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('Z')
    ax.set_title('Drone Missions with Conflicts')

    # Initialize primary path line for animation
    line, = ax.plot([], [], [], color='blue', marker='o', label='Primary Mission')

    ax.legend()

    ax.set_xlim(min(x_p) - 1, max(x_p) + 1)
    ax.set_ylim(min(y_p) - 1, max(y_p) + 1)
    ax.set_zlim(min(z_p) - 1, max(z_p) + 1)

    # Animation update function
    def update(frame):
        line.set_data(x_p[:frame], y_p[:frame])
        line.set_3d_properties(z_p[:frame])
        return line,

    # Animate with 100-300ms delay between frames, adjust as needed
    ani = FuncAnimation(fig, update, frames=len(primary) + 1, interval=300, blit=True, repeat=False)

    plt.tight_layout()
    plt.show()
