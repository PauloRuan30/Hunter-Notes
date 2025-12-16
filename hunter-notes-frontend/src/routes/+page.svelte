<script lang="ts">
    import { onMount } from 'svelte';
    import type { Monster } from '$lib/types';

    let monsters: Monster[] = [];

    onMount(async () => {
        const response = await fetch('/monsters.json');
        const data = await response.json();
        monsters = data.monsters;
    });

    function getMonsterSlug(name: string): string {
        return name.toLowerCase().replace(/\s/g, '-');
    }
</script>

<h1 class="text-3xl font-bold mb-6">Monster List</h1>

<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
    {#each monsters as monster (monster.name)}
        <a href="/{getMonsterSlug(monster.name)}" class="block bg-gray-800 text-white p-4 rounded-lg shadow-lg hover:bg-gray-700 transition-colors duration-200">
            <h2 class="text-xl font-semibold">{monster.name}</h2>
            <p>Type: {monster.type}</p>
            {#if monster.games && monster.games.length > 0}
                <img src="/icons/{monster.games[0].image}" alt="{monster.name} icon" class="w-16 h-16 object-contain" />
            {/if}
        </a>
    {/each}
</div>
