class Node {
    private value: any;
    private key: any;
    constructor(key, value) {
        this.key = key;
        this.value = value;
    }
}
class LRUCache {
    private capacity: number;
    private cache: Map<any, Node>;
    private mru_ptr: Node;
    constructor(capacity : number) {
        this.capacity = capacity
        this.cache = new Map();
        this.lru_ptr, this.mru_ptr = new Node(0, 0), new Node(0, 0);
    }

    remove() {

    }

    insert() {

    }

    get() {

    }

    put() {

    }
}