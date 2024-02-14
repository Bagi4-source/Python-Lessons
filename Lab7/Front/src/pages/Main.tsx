import {Tab, Tabs} from "@nextui-org/react";
import {SpaceTable} from ".";

export const Main = () => {
    return <div className="flex w-full flex-col">
        <h1>Таблички</h1>
        <Tabs aria-label="Options" size={"md"}>
            <Tab key="planets" title="Планеты">
                <SpaceTable
                    columns={{
                        "pk": {
                            name: "ID",
                            type: Number
                        },
                        "name": {
                            name: "Название",
                            type: String
                        },
                        "radius": {
                            name: "Радиус",
                            type: Number
                        },
                        "star_id": {
                            name: "ID звезды",
                            type: Number
                        }
                    }}
                    route={"api/Planets/"}/>
            </Tab>
            <Tab key="moons" title="Спутники">
                <SpaceTable
                    columns={{
                        "pk": {
                            name: "ID",
                            type: Number
                        },
                        "name": {
                            name: "Название",
                            type: String
                        },
                        "planet_id": {
                            name: "ID планеты",
                            type: Number
                        }
                    }}
                    route={"api/Moons/"}/>
            </Tab>
            <Tab key="stars" title="Звезды">
                <SpaceTable
                    columns={{
                        "pk": {
                            name: "ID",
                            type: Number
                        },
                        "name": {
                            name: "Название",
                            type: String
                        },
                        "mass": {
                            name: "Масса",
                            type: Number
                        }
                    }}
                    route={"api/Stars/"}/>
            </Tab>
        </Tabs>
    </div>
}