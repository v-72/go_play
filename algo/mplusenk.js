function getSet(arr, k) {
    let x = new Set();
    let ans = [];
    for (let i = 0; i < arr.length; i++) {
        let diff = k - arr[i];
        if (x.has(diff)) {
            ans = [arr[i], diff];
            break;
        }
        x.add(arr[i]);
    }
    return ans;
}

console.log(getSet([2, 3, 4, 1, 7, 6], 5));

