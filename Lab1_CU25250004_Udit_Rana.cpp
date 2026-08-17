#include <iostream>
using namespace std;

int main() {
    int arr[10] = {1, 2, 3};
    int n = 3;

    // Push
    arr[n] = 4;
    n++;

    cout << "After Push: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;

    // Pop
    n--;

    cout << "After Pop: ";
    for (int i = 0; i < n; i++)
        cout << arr[i] << " ";
    cout << endl;

    // Pop all elements
    int arr2[10] = {10, 20, 30, 40, 50};
    int size = 5;

    while (size > 0) {
        cout << "Popping this item: " << arr2[size - 1] << endl;
        size--;

        cout << "Array after pop: ";
        for (int i = 0; i < size; i++)
            cout << arr2[i] << " ";
        cout << endl;
    }

    return 0;
}




// code 2 

#include <iostream>
using namespace std;

int main() {
    int queue[10] = {10, 20, 30};
    int n = 3;

    cout << "Original Queue: ";
    for (int i = 0; i < n; i++)
        cout << queue[i] << " ";
    cout << endl;

    // Enqueue Operation
    queue[n] = 40;
    n++;

    cout << "After Enqueue: ";
    for (int i = 0; i < n; i++)
        cout << queue[i] << " ";
    cout << endl;

    // Dequeue Operation
    int dequeued_item = queue[0];
    cout << "Dequeued Item: " << dequeued_item << endl;

    for (int i = 0; i < n - 1; i++)
        queue[i] = queue[i + 1];

    n--;

    cout << "After Dequeue: ";
    for (int i = 0; i < n; i++)
        cout << queue[i] << " ";
    cout << endl;

    return 0;
}
