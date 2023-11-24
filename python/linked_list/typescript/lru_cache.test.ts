import {LRUCache} from "./lru_cache";

describe('simple tests', () => {
    test('get simple', () => {
        const lRUCache = new LRUCache(2);
        lRUCache.put(1, 1);
        lRUCache.put(2, 2);
        expect(lRUCache.get_(1)).toBe(1);
        lRUCache.put(3, 3);
        expect(lRUCache.get_(2)).toBeNull();
        lRUCache.put(4, 4);
        expect(lRUCache.get_(1)).toBeNull();
        expect(lRUCache.get_(3)).toBe(3);
        expect(lRUCache.get_(4)).toBe(4);
    });
})