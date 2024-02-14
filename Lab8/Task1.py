from pyrosm import OSM
from pyrosm import get_data

# Pyrosm comes with a couple of test datasets
# that can be used straight away without
# downloading anything
fp = get_data("test_pbf")

# Initialize the OSM parser object
osm = OSM(fp)

# Read all drivable roads
# =======================
drive_net = osm.get_network(network_type="driving")
drive_net.plot()