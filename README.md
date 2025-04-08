# 🗺️ Swiggy Map Plotter

## ✨ Description

Swiggy Map Plotter is a Python program that allows users to visualize geographic coordinates on an interactive map using Plotly. The project includes two main scripts: `main.py` for plotting geographic data and `temp.py` for retrieving and processing order tracking data from Swiggy.

## 🚀 Features

- **Interactive Scatter Plot:** Generates a scatter plot of geographic coordinates.
- **Order Tracking Data Retrieval:** Fetches and processes order tracking data from Swiggy.
- **Randomized Marker Sizes:** Assigns random sizes to valid locations on the map.

## 🛠️ Installation

To use this project, you need to have Python installed along with the required dependencies. Follow these steps to install the dependencies:

```bash
pip install pandas plotly.express requests
```

## 📦 Usage

### main.py

Here’s how you can use `main.py` to generate and display a scatter map:

```python
# Import the necessary module
from main import get_cords, px

# Fetch 50 sets of geographic coordinates
coordinates = get_cords(50)

# Convert the coordinates into a Pandas DataFrame
df = pd.DataFrame(coordinates, columns=["Lat", "Lon"])

# Create an interactive scatter map with Plotly Express
fig = px.scatter_mapbox(df, lat="Lat", lon="Lon", hover_name="Lat",
                        color_discrete_sequence=["fuchsia"], zoom=4,
                        height=600)

# Update the layout of the plot
fig.update_layout(mapbox_style="open-street-map")
fig.show()
```

### temp.py

Here’s how you can use `temp.py` to retrieve and process order tracking data:

```python
# Import the necessary module
from temp import get_cords

# Retrieve tracking data for 10 orders
get_cords(10)
```

## 🔧 Configuration (if applicable)

No additional configuration is required. The script uses default settings.

## 🧪 Tests (if available)

This project does not include tests at the moment, but you can add your own unit tests to ensure the functionality remains intact.

## 📁 Project Structure

```
swiggy_map_plotter/
├── main.py
├── temp.py
└── README.md
```

- `main.py`: Contains the script for generating and displaying a scatter map.
- `temp.py`: Contains the script for retrieving and processing order tracking data.
- `README.md`: This file.

## 👩‍💻 Contributing

Contributions are welcome! Feel free to open issues or submit pull requests. For major changes, please open an issue first to discuss what you would like to change.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

Built with ❤️ by gag3301v