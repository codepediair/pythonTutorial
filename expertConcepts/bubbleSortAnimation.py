# Import matplotlib and numpy libraries
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

# Define a function to swap two elements in an array
def swap(array, i, j):
    array[i], array[j] = array[j], array[i]

# Define a function to perform bubble sort on an array
def bubble_sort(array):
    # Get the length of the array
    n = len(array)
    # Loop through the array from the beginning to the end
    for i in range(n):
        # Assume that the array is already sorted
        sorted = True
        # Loop through the array from the beginning to the end - i - 1
        for j in range(n - i - 1):
            # Compare the current element with the next element
            if array[j] > array[j + 1]:
                # Swap them if they are in the wrong order
                swap(array, j, j + 1)
                # Set sorted to False to indicate that a swap occurred
                sorted = False
                # Yield the current state of the array for animation
                yield array
        # If no swap occurred, break out of the loop
        if sorted:
            break

# Create an array of random values between 0 and 100 with size 10
array = np.random.randint(0, 100, 30)

# Create a copy of the array to store the previous values
prev_array = array.copy()

# Create a figure and an axis for plotting
fig, ax = plt.subplots()

# Set the title and the labels of the axis
ax.set_title("Bubble Sort Simulation")
ax.set_xlabel("Index")
ax.set_ylabel("Value")

# Plot the initial state of the array as a bar chart with blue color
bars = ax.bar(range(len(array)), array, color="#3cbcc3")

# Define a function to update the plot for each iteration of bubble sort
def update(array, bars):
    global prev_array # Use the global variable prev_array
    # Loop through each bar and its corresponding value in the array
    for i, (bar, val) in enumerate(zip(bars, array)):
        # Set the height of the bar to the value
        bar.set_height(val)
        # Check if the value has changed from the previous iteration
        if val != prev_array[i]:
            # Change the color of the bar to green to indicate movement
            bar.set_color("#ebab3f")
        else:
            # Keep the color of the bar as blue
            bar.set_color("#3cbcc3")
    # Update prev_array with current values for next iteration
    prev_array = array.copy()

# Create an animation object that calls the update function for each iteration of bubble sort
anim = animation.FuncAnimation(fig, func=update, fargs=(bars,), frames=bubble_sort(array), interval=10, repeat=False)

# Show the plot and the animation with interactivity
plt.show()
