import matplotlib.pyplot as plt
measured_data = [10, 24, 51, 68, 99, 128, 190, 255]
plt.plot (measured_data)
plt.show()

measured_data_str = [str(item) for item in measured_data]
print (measured_data, measured_data_str)

with open ("data.txt", "w") as out_file:
	out_file.write ("\n".join(measured_data_str))

