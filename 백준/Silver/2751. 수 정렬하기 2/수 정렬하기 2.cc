#include<stdio.h>

int number, data[1000001];

void merge(int a[], int m, int middle, int n) {
    int i = m;
    int j = middle + 1;
    int k = m;
    while(i <= middle && j <= n){
        if(a[i] <= a[j]){
            data[k] = a[i];
            i++;
        } else {
            data[k] = a[j];
            j++;
        }
        k++;
    }
    if(i > middle){
        for(int temp = j; temp <= n; temp++){
            data[k] = a[temp];
            k++;
        }
    } else {
        for(int temp = i; temp <= middle; temp++){
            data[k] = a[temp];
            k++;
        } 
    }
    for(int t = m; t <= n; t++) {
        a[t] = data[t];
    }
}

void mergeSort(int a[], int m, int n) {
    if(m < n) {
        int middle = (m + n) / 2;
        mergeSort(a, m, middle);
        mergeSort(a, middle + 1, n);
        merge(a, m, middle, n);
    }
}

int main(void) {
    int array[1000001];
    
    scanf("%d", &number);
    for(int i = 0; i < number; i++){
        scanf("%d", &array[i]);
    }
    
    mergeSort(array, 0, number - 1);
    for(int i = 0; i < number; i++){
        printf("%d\n", array[i]);
    }
}