<!-- src/routes/+layout.svelte -->
<script lang="ts">
    import { flip } from '$lib/transitions/flip';
    import { page } from '$app/stores';
</script>

<div class="container mx-auto p-4">
    {#key $page.url.pathname}
        <div in:flip={{ delay: 200, duration: 600, axis: 'y' }} out:flip={{ duration: 600, axis: 'y' }}>
            <slot />
        </div>
    {/key}
</div>