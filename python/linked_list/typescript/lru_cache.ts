class Node_ {
    get prev(): Node_ {
        return this._prev;
    }

    set prev(value: Node_) {
        this._prev = value;
    }
    private _prev: Node_;
    get next(): Node_ {
        return this._next;
    }

    set next(value: Node_) {
        this._next = value;
    }
    private _next: Node_;
    get key(): any {
        return this._key;
    }

    set key(value: any) {
        this._key = value;
    }
    get value(): any {
        return this._value;
    }

    set value(value: any) {
        this._value = value;
    }
    private _value: any;
    private _key: any;
    constructor(key : any, value: any) {
        this._key = key;
        this._value = value;
        this._next = null;
        this._prev = null;
    }
}

export class LRUCache {
    private capacity: number;
    private cache: Map<any, Node_>;
    private mru_ptr: Node_;
    private lru_ptr: Node_;

    constructor(capacity: number) {
        this.capacity = capacity
        this.cache = new Map();
        [this.lru_ptr, this.mru_ptr] = [new Node_(0, 0), new Node_(0, 0)];
        [this.lru_ptr.next, this.mru_ptr.prev] = [this.mru_ptr, this.lru_ptr];
    }

    public remove(node: Node_) {
        const [prev_node, next_node] = [node.prev, node.next];
        [prev_node.next, next_node.prev] = [next_node, prev_node];
    }

    public insert(node: Node_) {
        const [prev_node, next_node] = [this.mru_ptr.prev, this.mru_ptr];
        [prev_node.next, next_node.prev] = [node, node];
        [node.prev, node.next] = [prev_node, next_node];

    }

    public get_(key: any): any {
        if (this.cache.has(key)) {
            //     cache hit
            let node = this.cache.get(key);
            this.remove(node);
            this.insert(node);
            return node.value;
        }
        // cache miss
        return null;
    }

    public put(key: any, value: any) {
        if (this.cache.has(key)) {
            this.remove(this.cache.get(key));
        }
        //     determine whether cache eviction is necessary
        const new_node = new Node_(key, value);
        this.insert(new_node);
        if (this.cache.size > this.capacity) {
            let evict_node = this.lru_ptr.next;
            this.remove(evict_node)
            this.cache.delete(evict_node.key)
        }
    }
}
