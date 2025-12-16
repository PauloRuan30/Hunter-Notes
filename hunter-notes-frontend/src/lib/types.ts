// src/lib/types.ts
export interface GameInfo {
    game: string;
    image: string;
    info: string;
    danger?: string;
}

export interface Monster {
    _id: {
        $oid: string;
    };
    name: string;
    type: string;
    isLarge: boolean;
    subSpecies?: string[];
    elements?: string[];
    ailments?: string[];
    weakness?: string[];
    games: GameInfo[];
}
