import osmium as osm
import pandas as pd


class OSMHandler(osm.SimpleHandler):
    def __init__(self):
        osm.SimpleHandler.__init__(self)
        self.osm_data = []

    def tag_inventory(self, elem, elem_type):
        for tag in elem.tags:
            self.osm_data.append([elem_type,
                                  elem.id,
                                  elem.version,
                                  elem.visible,
                                  pd.Timestamp(elem.timestamp),
                                  elem.uid,
                                  elem.user,
                                  elem.changeset,
                                  len(elem.tags),
                                  tag.k,
                                  tag.v])

    def node(self, n):
        self.tag_inventory(n, "node")

    def way(self, w):
        self.tag_inventory(w, "way")

    def relation(self, r):
        self.tag_inventory(r, "relation")


osmhandler = OSMHandler()
osmhandler.apply_file("1.osm")
df_osm = pd.DataFrame(osmhandler.osm_data)
banks = df_osm[df_osm[10] == 'bank']

result = df_osm[(df_osm[9] == 'opening_hours') & (df_osm[10].str.contains('09:00-')) & (df_osm[1].isin(banks[1]))]
print(result)

# Вариант 1 Найти количество банков, вывести их в алфавитном порядке,
# а также найти количество банков, работающих с 9:00.
