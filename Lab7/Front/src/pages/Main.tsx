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
                            typeCheck: (str: string) => !isNaN(parseInt(str))
                        },
                        "name": {
                            name: "Название",
                            typeCheck: (_: string) => true
                        },
                        "radius": {
                            name: "Радиус",
                            typeCheck: (str: string) => !isNaN(parseInt(str))
                        },
                        "star_id": {
                            name: "ID звезды",
                            typeCheck: (str: string) => !isNaN(parseInt(str))
                        }
                    }}
                    route={"api/Planets/"}/>
            </Tab>
            <Tab key="moons" title="Спутники">
                <SpaceTable
                    columns={{
                        "pk": {
                            name: "ID",
                            typeCheck: (str: string) => !isNaN(parseInt(str))
                        },
                        "name": {
                            name: "Название",
                            typeCheck: (_: string) => true
                        },
                        "planet_id": {
                            name: "ID планеты",
                            typeCheck: (str: string) => !isNaN(parseInt(str))
                        }
                    }}
                    route={"api/Moons/"}/>
            </Tab>
            <Tab key="stars" title="Звезды">
                <SpaceTable
                    columns={{
                        "pk": {
                            name: "ID",
                            typeCheck: (str: string) => !isNaN(parseInt(str))
                        },
                        "name": {
                            name: "Название",
                            typeCheck: (_: string) => true
                        },
                        "mass": {
                            name: "Масса",
                            typeCheck: (str: string) => !isNaN(parseInt(str))
                        }
                    }}
                    route={"api/Stars/"}/>
            </Tab>
        </Tabs>
    </div>
}