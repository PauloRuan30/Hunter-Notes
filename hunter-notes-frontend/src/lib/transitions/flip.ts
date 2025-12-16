// src/lib/transitions/flip.ts
import { cubicOut } from 'svelte/easing';

export function flip(node, { duration = 600, delay = 0, axis = 'y' }) {
    const isX = axis === 'x';
    const isY = axis === 'y';

    return {
        delay,
        duration,
        easing: cubicOut,
        css: (t, u) => {
            const opacity = t;
            const transform = `perspective(1000px) rotate${axis.toUpperCase()}(${u * 180}deg)`;
            return `
                opacity: ${opacity};
                transform: ${transform};
                transform-origin: ${isX ? 'center bottom' : isY ? 'center center' : 'center center'};
            `;
        }
    };
}
