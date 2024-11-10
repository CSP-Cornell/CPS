import matplotlib.pyplot as plt
import numpy as np

# Define speed range for the motor
speed = np.linspace(0, 100, 100)  # Speed in percentage (0-100)

# Define torque vs speed characteristics
stall_torque = 1.2  # Maximum torque at stall (Nm)
torque = stall_torque * (1 - speed / 100)  # Linear decrease

# Power vs speed characteristics
max_power = 0.6  # Peak power (W) for this motor example
power = max_power * (4 * speed * (100 - speed) / 10000)  # Parabolic curve

# Efficiency vs speed characteristics
max_efficiency = 90  # Maximum efficiency in percentage
efficiency = max_efficiency * (1 - (speed - 50)**2 / 2500)  # Bell curve

# Current vs torque characteristics
max_current = 10  # Maximum current at stall (A)
current = max_current * (torque / stall_torque)  # Linear increase

efficiency_2 = torque * speed / (torque * speed + (.01*current)**2)
# Plotting the curves
'''
# Torque vs Speed
plt.figure(figsize=(8, 6))
plt.plot(speed, torque, label="Torque (Nm)", color="blue")
plt.xlabel("Speed (%)")
plt.ylabel("Torque (Nm)")
plt.title("Torque vs Speed for DC Motor")
plt.legend()
plt.grid(True)
plt.show()

# Power vs Speed
plt.figure(figsize=(8, 6))
plt.plot(speed, power, label="Power (W)", color="green")
plt.xlabel("Speed (%)")
plt.ylabel("Power (W)")
plt.title("Power vs Speed for DC Motor")
plt.legend()
plt.grid(True)
plt.show()

# Efficiency vs Speed
plt.figure(figsize=(8, 6))
plt.plot(speed, efficiency, label="Efficiency (%)", color="orange")
plt.xlabel("Speed (%)")
plt.ylabel("Efficiency (%)")
plt.title("Efficiency vs Speed for DC Motor")
plt.legend()
plt.grid(True)
plt.show()

# Current vs Torque
plt.figure(figsize=(8, 6))
plt.plot(torque, current, label="Current (A)", color="red")
plt.xlabel("Torque (Nm)")
plt.ylabel("Current (A)")
plt.title("Current vs Torque for DC Motor")
plt.legend()
plt.grid(True)
plt.show()
'''
# Current vs Torque
plt.figure(figsize=(8, 6))
plt.plot(torque,efficiency_2, label="effiiency_2(A)", color="red")
plt.xlabel("Torque (Nm)")
plt.ylabel("Current (A)")
plt.title("efficientasfdlsdfasl dfalasdf vs Torque for DC Motor")
plt.legend()
plt.grid(True)
plt.show()