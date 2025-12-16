<script lang="ts">
    import type { PageData } from './$types';

    export let data: PageData;
</script>

<h1 class="text-3xl font-bold mb-4">{data.monster.name}</h1>
<p>Type: {data.monster.type}</p>
<p>Elements: {data.monster.elements ? data.monster.elements.join(', ') : 'None'}</p>
<p>Weakness: {data.monster.weakness ? data.monster.weakness.join(', ') : 'None'}</p>

{#if data.monster.games && data.monster.games.length > 0}
    <div class="mt-4">
        <img src="/icons/{data.monster.games[0].image}" alt="{data.monster.name} icon" class="w-32 h-32 object-contain" />
        <p class="text-sm text-gray-400 mt-2">Source: {data.monster.games[0].game}</p>
    </div>
{/if}

<a href="/" class="mt-6 inline-block bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded">
    Back to Monster List
</a>
