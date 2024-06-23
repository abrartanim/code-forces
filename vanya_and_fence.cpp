#include <bits/stdc++.h>

using namespace std;

int main()
{
    int count, fence_height;
    cin >> count;
    cin >> fence_height;
    int total = 0;
    int temp;
    for (int i = 0; i < count; i++)
    {
        cin >> temp;
        if (temp > fence_height)
            total += 2;
        else
            total += 1;
    }

    cout << total;
}