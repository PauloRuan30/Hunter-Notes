// src/routes/[monsterName]/+page.ts
import type { PageLoad } from './$types';
import type { Monster } from '$lib/types';

export const load: PageLoad = async ({ fetch, params }) => {
    const { monsterName } = params;

    const response = await fetch('/monsters.json');
    const data = await response.json();
    const monsters: Monster[] = data.monsters;

    const monster = monsters.find(m => m.name.toLowerCase().replace(/\s/g, '-') === monsterName);

    if (!monster) {
        // Handle case where monster is not found, maybe redirect to a 404 page
        // For now, we'll just return an empty object or throw an error
        return {
            monster: null // Or throw error(404, 'Not Found')
        };
    }

    return {
        monster
    };
};
