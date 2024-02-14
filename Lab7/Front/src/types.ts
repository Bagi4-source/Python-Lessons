export interface PlanetData {
    pk: number
    name: string
    radius: number
    star_id: number
}

export interface MoonData {
    pk: number
    name: string
    planet_id: number
}

export interface StarData {
    pk: number
    name: string
    planet_id: number
}

export interface Response<T> {
    count: number
    next?: string
    previous?: string
    results: T[]
}