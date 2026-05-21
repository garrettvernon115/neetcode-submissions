class DynamicArray {

    private int length;
    private int capacity;
    private int[] arr;
    
    // Constructor to initialize the dynamic array
    // O(n) n = capacity;
    public DynamicArray(int capacity) {
        this.length = 0;
        this.capacity = capacity;
        this.arr = new int[this.capacity];
       

    }
    // Get the value at the i-th index 
    // get will be O(1) or constant time, retrieving an element from an array is constant time
    public int get(int i) {
    return arr[i];

    }
    // Insert value n at the i-th index
    // Set will be O(1) or constant time, inserting an element into an array is constant time
    public void set(int i, int n) {
        arr[i] = n;
        

    }
    // Insert n in the last position of the array
    // // O(1) Avg case/ Ammoritized
    public void pushback(int n) {
        if (length == capacity) {
            resize();
        }
        arr[length] = n;
        length++;
        
    }

    // Remove the last element in the array
    //O(1) 
    public int popback() {
        if(length > 0) {
            length--;
        }
        return arr[length];
        
    }

    // Resize the array
    // O(n)
     private void resize() {
        capacity *= 2;
        int[] newArr = new int[capacity];

        for(int i = 0;i < length;i++) {
            newArr[i] = arr[i];
        }
        arr = newArr;
       
    } 
    // Get the size of the array
    // O(1)
    public int getSize() {
        return length;
        

    }
    // Get the capacity of the array
    // O(1)
    public int getCapacity() {
        return capacity;
        
    }
}
