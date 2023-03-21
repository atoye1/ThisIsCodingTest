function validAnagram(w1, w2) {
    if (w1.length !== w2.length) return false;
    const counter1 = {};
    const counter2 = {};
    for (let i = 0; i < w1.length; i++) {
        counter1[w1[i]] = (counter1[w1[i]] || 0) + 1;
        counter2[w2[i]] = (counter2[w2[i]] || 0) + 1;
    }
    console.log(counter1, counter2);
    for (let key in counter1) {
        if (counter1[key] !== counter2[key]) return false;
    }
    return true;
}
console.log(validAnagram('', '')); // true
console.log(validAnagram('aaz', 'zza')); // false
console.log(validAnagram('anagram', 'nagaram')); // true
console.log(validAnagram("rat", "car")); // false) // false
console.log(validAnagram('awesome', 'awesom')); // false
console.log(validAnagram('amanaplanacanalpanama', 'acanalmanplanpamana')); // false
console.log(validAnagram('qwerty', 'qeywrt')); // true
console.log(validAnagram('texttwisttime', 'timetwisttext')); // true