import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Boundaries
temp_min, temp_max = 0, 90
time_min, time_max = 0, 10

# Thresholds
min_temp_threshold = 20   # vertical line
min_time_threshold = 2.0  # horizontal line

# Samples
N = 1000

# Generate realistic distributions
temps = np.random.normal(loc=60, scale=15, size=N)
times = np.random.normal(loc=6, scale=2, size=N)

# Clip to valid ranges
temps = np.clip(temps, temp_min, temp_max)
times = np.clip(times, time_min, time_max)

# Decision boundaries (scaled to 0–90 range)
upper_line = -0.1 * temps + 10
lower_line = -0.1 * temps + 6

# Labeling
labels = []
for t, d in zip(temps, times):
    if (d > min_time_threshold and t > min_temp_threshold and 
        d < (-0.1*t + 10) and d > (-0.1*t + 6)):
        labels.append(1)  # good coffee
    else:
        labels.append(0)  # bad coffee

labels = np.array(labels)

# Save to CSV
df = pd.DataFrame({
    "temperature": temps,
    "duration": times,
    "label": labels
})
df.to_csv("coffee_roasting.csv", index=False)
print("Dataset saved as coffee_roasting.csv")

# Plot for visualization
plt.figure(figsize=(8,6))
plt.scatter(temps[labels==1], times[labels==1], c='red', marker='x', label="Good (1)")
plt.scatter(temps[labels==0], times[labels==0], c='blue', marker='o', label="Bad (0)")

x = np.linspace(temp_min, temp_max, 200)
plt.plot(x, -0.1*x + 10, 'k--', label="Upper boundary")
plt.plot(x, -0.1*x + 6, 'k--', label="Lower boundary")
plt.axhline(y=min_time_threshold, color='purple', linestyle='-', label="Min duration")
plt.axvline(x=min_temp_threshold, color='purple', linestyle='-', label="Min temp")

plt.xlabel("Temperature (Celsius)")
plt.ylabel("Duration (minutes)")
plt.legend()
plt.title("Synthetic Coffee Roasting Dataset")
plt.ylim(time_min, time_max)
plt.xlim(temp_min, temp_max)
plt.show()
